#!/usr/bin/env python3
"""
fetch_enrollment.py — Download and process NCES CCD LEA membership data
into per-county enrollment JSON files for the Hugo site.

Usage:
    python3 scripts/fetch_enrollment.py

Output: data/enrollment/<fips>.json for each target county
        data/enrollment/45045+45083.json for Greenville-Spartanburg merged

Data source: NCES Common Core of Data (CCD), public schools only
  - Wide format (2010-15): CONUM embedded in LEA file, per-grade columns PK/KG/G01-G12
  - Long format (2016-24): LEAID -> CONUM via EDGE geocode file, TOTAL_INDICATOR='Subtotal 4 - By Grade'
  - 2022-23 skipped (file is anomalously 1.3GB, corrupt/mislabeled on NCES server)
"""

import csv
import io
import json
import os
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

CACHE_DIR = Path("/tmp/ccd_cache")
CACHE_DIR.mkdir(exist_ok=True)

# Resolve output dir relative to script location (works from any cwd)
SCRIPT_DIR = Path(__file__).parent
SITE_ROOT = SCRIPT_DIR.parent
OUT_DIR = SITE_ROOT / "data" / "enrollment"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ALL_TARGET_FIPS = {
    "48453", "37119", "47065", "39049", "39061", "08031", "48141", "13051",
    "45045", "45083", "01089", "12057", "12086", "01097", "47037",
    "22071", "35001", "48029", "45019", "51059", "53033"
}

FIPS_META = {
    "48453": {"city": "Austin, TX",                  "county": "Travis County, TX"},
    "37119": {"city": "Charlotte, NC",               "county": "Mecklenburg County, NC"},
    "47065": {"city": "Chattanooga, TN",             "county": "Hamilton County, TN"},
    "39049": {"city": "Columbus, OH",                "county": "Franklin County, OH"},
    "39061": {"city": "Cincinnati, OH",              "county": "Hamilton County, OH"},
    "08031": {"city": "Denver, CO",                  "county": "Denver County, CO"},
    "48141": {"city": "El Paso, TX",                 "county": "El Paso County, TX"},
    "13051": {"city": "Savannah, GA",                "county": "Chatham County, GA"},
    "45045": {"city": "Greenville-Spartanburg, SC",  "county": "Greenville County, SC"},
    "45083": {"city": "Greenville-Spartanburg, SC",  "county": "Spartanburg County, SC"},
    "01089": {"city": "Huntsville, AL",              "county": "Madison County, AL"},
    "12057": {"city": "Tampa, FL",                   "county": "Hillsborough County, FL"},
    "12086": {"city": "Miami, FL",                   "county": "Miami-Dade County, FL"},
    "01097": {"city": "Mobile, AL",                  "county": "Mobile County, AL"},
    "47037": {"city": "Nashville, TN",               "county": "Davidson County, TN"},
    "22071": {"city": "New Orleans, LA",             "county": "Orleans Parish, LA"},
    "35001": {"city": "Albuquerque, NM",             "county": "Bernalillo County, NM"},
    "48029": {"city": "San Antonio, TX",             "county": "Bexar County, TX"},
    "45019": {"city": "Charleston, SC",              "county": "Charleston County, SC"},
    "51059": {"city": "Herndon, VA",                 "county": "Fairfax County, VA"},
    "53033": {"city": "Seattle, WA",                 "county": "King County, WA"},
}

# Files to process — wide format (CONUM embedded) and long format (needs EDGE join)
# Tuple: (year_label, format, membership_zip, edge_lea_zip, mem_url, edge_url)
YEARS = [
    ("2010-11", "wide",  "ag102a_txt.zip",                      None,
     "https://nces.ed.gov/ccd/data/zip/ag102a_txt.zip", None),
    ("2011-12", "wide",  "ag111a_txt.zip",                      None,
     "https://nces.ed.gov/ccd/data/zip/ag111a_txt.zip", None),
    ("2012-13", "wide",  "ag121a_supp_txt.zip",                 None,
     "https://nces.ed.gov/ccd/data/zip/ag121a_supp_txt.zip", None),
    ("2013-14", "wide",  "ag131a_supp_txt.zip",                 None,
     "https://nces.ed.gov/ccd/data/zip/ag131a_supp_txt.zip", None),
    ("2014-15", "wide",  "ccd_lea_052_1415_w_0216161a_txt.zip", None,
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1415_w_0216161a_txt.zip", None),
    ("2015-16", "wide",  "ccd_lea_052_1516_w_1a_011717_csv.zip", None,
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1516_w_1a_011717_csv.zip", None),
    ("2016-17", "long",  "ccd_lea_052_1617_l_2a_11212017.zip",  "EDGE_GEOCODE_PUBLICLEA_1617.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1617_l_2a_11212017.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1617.zip"),
    ("2017-18", "long",  "ccd_lea_052_1718_l_1a_083118.zip",    "EDGE_GEOCODE_PUBLICLEA_1718.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1718_l_1a_083118.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1718.zip"),
    ("2018-19", "long",  "ccd_lea_052_1819_l_1a_091019.zip",    "EDGE_GEOCODE_PUBLICLEA_1819.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1819_l_1a_091019.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1819.zip"),
    ("2019-20", "long",  "ccd_lea_052_1920_l_1a_082120.zip",    "EDGE_GEOCODE_PUBLICLEA_1920.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_1920_l_1a_082120.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1920.zip"),
    ("2020-21", "long",  "ccd_lea_052_2021_l_1a_080621.zip",    "EDGE_GEOCODE_PUBLICLEA_2021.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_2021_l_1a_080621.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_2021.zip"),
    ("2021-22", "long",  "ccd_lea_052_2122_l_1a_071722.zip",    "EDGE_GEOCODE_PUBLICLEA_2122.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_2122_l_1a_071722.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_2122.zip"),
    # 2022-23 SKIPPED — file is ~1.3GB (anomalously large, likely corrupt on NCES server)
    ("2023-24", "long",  "ccd_lea_052_2324_l_1a_073124.zip",    "EDGE_GEOCODE_PUBLICLEA_2324.zip",
     "https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_2324_l_1a_073124.zip",
     "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_2324.zip"),
]

GRADE_ELEM = {"PK", "KG", "G01", "G02", "G03", "G04", "G05"}
GRADE_MID  = {"G06", "G07", "G08"}
GRADE_HIGH = {"G09", "G10", "G11", "G12"}


def load_edge_lea(zip_path):
    """Return LEAID -> county FIPS mapping. EDGE LEA file: pipe-delimited, no header.
    Col 0 = LEAID, col 8 = CONUM (5-digit county FIPS)."""
    zf = zipfile.ZipFile(zip_path)
    txt = next(n for n in zf.namelist() if n.upper().endswith(".TXT"))
    m = {}
    with zf.open(txt) as f:
        for line in f:
            parts = line.decode("latin-1").strip().split("|")
            if len(parts) >= 9 and parts[0].strip() and parts[8].strip():
                m[parts[0].strip()] = parts[8].strip()
    return m


def grade_long_to_level(grade):
    """Map long-format grade label to enrollment level. Returns None for non-standard grades.
    Uses exact set membership (not substring matching) to avoid 'GRADE 1' matching 'GRADE 10'."""
    g = grade.strip().upper()
    ELEM = {"PRE-KINDERGARTEN", "PREKINDERGARTEN", "KINDERGARTEN",
            "GRADE 1", "GRADE 2", "GRADE 3", "GRADE 4", "GRADE 5"}
    MID  = {"GRADE 6", "GRADE 7", "GRADE 8"}
    HIGH = {"GRADE 9", "GRADE 10", "GRADE 11", "GRADE 12"}
    if g in ELEM: return "Elementary"
    if g in MID:  return "Middle"
    if g in HIGH: return "High"
    return None  # ungraded, adult education, etc.


def process_long_format(zip_path, lea_county):
    """Process long-format LEA membership file. Returns {county_fips: {level: count}}."""
    zf = zipfile.ZipFile(zip_path)
    csv_name = next(n for n in zf.namelist() if n.lower().endswith(".csv"))
    results = defaultdict(lambda: defaultdict(int))
    with zf.open(csv_name) as f:
        reader = csv.DictReader(io.TextIOWrapper(f, encoding="latin-1"))
        for row in reader:
            # Filter to grade-level subtotals only (excludes race/sex breakdowns)
            if "Subtotal 4 - By Grade" not in row.get("TOTAL_INDICATOR", ""):
                continue
            leaid = row.get("LEAID", "").strip()
            county = lea_county.get(leaid)
            if not county or county not in ALL_TARGET_FIPS:
                continue
            level = grade_long_to_level(row.get("GRADE", ""))
            if not level:
                continue
            try:
                count = int(float(row.get("STUDENT_COUNT", "0").strip()))
            except (ValueError, AttributeError):
                continue
            if count > 0:
                results[county][level] += count
    return results


def process_wide_format(zip_path):
    """Process wide-format LEA membership file. Returns {county_fips: {level: count}}."""
    zf = zipfile.ZipFile(zip_path)
    data_file = next(n for n in zf.namelist() if n.lower().endswith((".csv", ".txt")))
    # Detect delimiter from first chunk
    with zf.open(data_file) as f:
        sample = f.read(1000).decode("latin-1", "replace")
    sep = "\t" if sample.count("\t") > sample.count(",") else ","

    results = defaultdict(lambda: defaultdict(int))
    with zf.open(data_file) as f:
        reader = csv.DictReader(io.TextIOWrapper(f, encoding="latin-1"), delimiter=sep)
        # Normalize header keys to uppercase for consistent lookup
        raw_headers = reader.fieldnames or []
        hmap = {h.strip().upper(): h for h in raw_headers}

        def get_col(row, key):
            actual = hmap.get(key)
            return (row.get(actual, "") or "0").strip() if actual else "0"

        def safe_int(v):
            try:
                n = int(float(v))
                return max(n, 0)
            except (ValueError, TypeError):
                return 0

        for row in reader:
            county = get_col(row, "CONUM").strip()
            if not county or county not in ALL_TARGET_FIPS:
                continue
            elem = sum(safe_int(get_col(row, g)) for g in GRADE_ELEM)
            mid  = sum(safe_int(get_col(row, g)) for g in GRADE_MID)
            high = sum(safe_int(get_col(row, g)) for g in GRADE_HIGH)
            if elem: results[county]["Elementary"] += elem
            if mid:  results[county]["Middle"]     += mid
            if high: results[county]["High"]       += high
    return results


def build_json(meta, year_data):
    years = sorted(year_data.keys())
    levels = ["Elementary", "Middle", "High"]
    series = {lvl: [year_data.get(y, {}).get(lvl, 0) for y in years] for lvl in levels}
    return {
        "city": meta["city"],
        "county": meta["county"],
        "source": ("NCES Common Core of Data (CCD), public schools only. "
                   "Grades PK-5=Elementary, 6-8=Middle, 9-12=High."),
        "years": years,
        "series": series,
    }


def main():
    # Accumulate: all_data[fips][year_label] = {level: count}
    all_data = defaultdict(dict)

    for entry in YEARS:
        year_label, fmt, mem_file, edge_file = entry[0], entry[1], entry[2], entry[3]
        mem_path = CACHE_DIR / mem_file

        if not mem_path.exists():
            print(f"SKIP {year_label}: {mem_file} not in cache")
            continue
        try:
            zipfile.ZipFile(mem_path).namelist()
        except Exception as e:
            print(f"SKIP {year_label}: bad zip — {e}")
            continue

        print(f"Processing {year_label} ({fmt})...", end=" ", flush=True)
        try:
            if fmt == "wide":
                year_result = process_wide_format(mem_path)
            else:
                edge_path = CACHE_DIR / edge_file
                lea_county = load_edge_lea(edge_path)
                year_result = process_long_format(mem_path, lea_county)

            for fips, levels in year_result.items():
                all_data[fips][year_label] = dict(levels)

            total = sum(sum(v.values()) for v in year_result.values())
            print(f"{len(year_result)} counties, {total:,} students")
        except Exception as e:
            import traceback
            print(f"ERROR — {e}")
            traceback.print_exc()

    # Merge Greenville + Spartanburg
    gs_merged = {}
    for entry in YEARS:
        year_label = entry[0]
        g = all_data.get("45045", {}).get(year_label, {})
        s = all_data.get("45083", {}).get(year_label, {})
        if g or s:
            merged = defaultdict(int)
            for level, n in g.items(): merged[level] += n
            for level, n in s.items(): merged[level] += n
            gs_merged[year_label] = dict(merged)

    # Write individual county files
    written = []
    for fips, meta in FIPS_META.items():
        if fips in ("45045", "45083"):
            continue
        yd = all_data.get(fips)
        if not yd:
            print(f"WARNING: no data for {fips} ({meta['city']})")
            continue
        out_path = OUT_DIR / f"{fips}.json"
        out_path.write_text(json.dumps(build_json(meta, yd), indent=2))
        written.append(fips)

    # Write merged Greenville-Spartanburg
    if gs_merged:
        meta = {
            "city": "Greenville-Spartanburg, SC",
            "county": "Greenville + Spartanburg Counties, SC"
        }
        (OUT_DIR / "45045_45083.json").write_text(
            json.dumps(build_json(meta, gs_merged), indent=2)
        )
        written.append("GS(45045_45083)")

    print(f"\nWrote {len(written)} JSON files to {OUT_DIR}")

    # Sanity check on Travis County (Austin)
    sample_path = OUT_DIR / "48453.json"
    if sample_path.exists():
        sample = json.loads(sample_path.read_text())
        print(f"\nSanity check — Austin (Travis Co):")
        print(f"  Years: {sample['years']}")
        for lvl in ["Elementary", "Middle", "High"]:
            print(f"  {lvl}: {sample['series'][lvl]}")


if __name__ == "__main__":
    main()
