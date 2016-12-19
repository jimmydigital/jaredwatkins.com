#!/usr/bin/env perl

use warnings;
use strict;
use Image::Magick;
use File::Copy;
use Getopt::Long;
use Pod::Usage;

my $dir = 'pics/gallery/';  # Create one
                            # sub folder below it for each gallery.. original
                            # images to process

my $watermark = 'http://www.jaredwatkins.com/';  # Text to watermark your full size
                                                 # images that get deployed


############################

my ($man, $markdown);
GetOptions ('man'            => \$man,
            'markdown|md'    => \$markdown,
           );

if ($man)          { pod2usage( {-verbose => 2 } ); }
if ($markdown)     { system ('cat makegallery.pl | ./pod2md.pl'); }
if ($#ARGV == -1 ) { pod2usage( {-verbose => 1 } ); }


chdir $dir;
foreach my $item (<*>)
{
    next if $item eq '_processed';

    if ( -d $item)
    {
        convertGallery($item);

        move ($item, "_processed/$item") or die "Unable to move $item to _processed";

        # If it's not already there.. setup the gallery index page which you need to edit
        if (not -f "../gallery/$item/index.md")
        {
            mkdir "../gallery/$item";
            open my $MD, '>', "../gallery/index.md" or die ("Unable to write index.md");
            print $MD "---\n";
            print $MD "title: $item\n";
            print $MD "layout: page\n";
            print $MD "shortdesc: $item\n";
            print $MD "---\n";
            print $MD "{% include custom/gallery_$item.md %}\n";
            close $MD;
        }
    }
}


# This does a few things... creates the thumbnails and watermarks the full size images
# and also creats a partial gallery.md file that contains the liquid tags/links which is
# included by the gallery index page.
sub convertGallery
{
    my ($dir) = @_;
    chdir $dir;
    $outdir = '../../../static/gallery'
    mkdir "$outdir/$dir";
    open my $MD, '>', "../../../static/gallery/$dir/gallery.md" or die ("Unable to create gallery.md file for $dir");

    foreach my $item (<*>)
    {
        my %file;

        $item =~ /^(.+)\.(\w+)$/;

        $file{'filename'} = $item;
        $file{'name'}     = $1;
        $file{'ext'}      = $2;

        unlink "$outdir/$dir/gallery_$file{name}.$file{ext}" if (-f "$outdir//$dir/gallery_$file{name}.$file{ext}");
        my $magick = new Image::Magick;
        $magick->Read("$file{filename}");
        $magick->Resize(geometry=>'x80'); # Controls the size of the thumbnail
        $magick->Write("$outdir/$dir/gallery_$file{name}.$file{ext}");

        unlink "$outdir/$dir/$file{name}.$file{ext}" if (-f "$outdir/$dir/$file{name}.$file{ext}");

        my $null = new Image::Magick;
        $null->Set(size=>'1000x800');
        my $x=$null->ReadImage('xc:white');
        warn "$x" if "$x";
        $x=$null->Annotate(text=>$watermark,
                           geometry=>'+40+60',
                           font=>'../../../externals/LiberationMono-Bold.ttf',
                           fill=>'grey',
                           gravity=>'North',
                           antialias=>'1',
                           pointsize=>25);
        warn "$x" if "$x";
        $null->Rotate(degrees=>'15', background=>'white');
        $null->Set(alpha=>'Activate');
        $null->Transparent(color=>'white');

        $magick = new Image::Magick;
        $magick->Read("$file{filename}");
        $magick->Composite(image=>$null,
                           compose=>'Dissolve',
                           gravity=>'Center',
                           tile=>'1',
                           caption=>$watermark,
                           opacity=>'40%');
        $magick->Write("$outdir/$dir/$file{name}.$file{ext}");

        print $MD "[ {% img /pics/gallery/$dir/gallery_$file{name}.$file{ext} %} ](/pics/gallery/$dir/$file{name}.$file{ext})\n";
    }

    chdir "../";
}

__END__

=head1 NAME

makegallery.pl - Automate the creation of image gallery pages for octopress / jekyll

=head1 SYNOPSIS

This script makes it easier to generate image gallery pages for Octopress from a folder of random images.
I found that with Octopress the creation of image galleries was left as an exercise to the blogger.. so I came up
with this as a solution.  It's written in perl because I'm not familiar enough with ruby.  When you have the proper
directory structure this plugin will:

=over

=item

Create thumbnails for use in main gallery page

=item

Watermark your full size images with whatever text you set in the script

=item

Create a stub gallery index.md file that you can edit for title, description etc

=item

Create the partial markdown file that lists the actual linked image list with liquid macros that gets included  into the stub gallery page.

=back


=head1 USAGE

The script takes no arguments.. it depends on your directory structure being setup properly.

From your main octopress directory that structure is:

 octopress/
    |
    -/source/_gallery
     (Where you create gallery subfolders to hold original images)
        |
        |-/source/_gallery/galleryname
          (Something short and simple.. used to link to your
           gallery and name other files)
        |
        |-/source/_gallery/_processed
          (Where the original folders are moved after processing)
    |
    -/source/gallery
     (Where the markdown ends up.. similar to how pages and posts work.
      This will contain a list of folders that match your galleryname
      with a single index.md file in them.)
    |
    |-/source/_includes/custom/
      (Where the partial gallery_galleryname.md files end up.
       Contains only the linked list of images in liquid format)
    |
    |-/source/pics/galleryname
      (Where the processed images and thumbnails end up. This gets
       copied / deployed to your server.)

=head1 REQUIREMENTS

This script uses perl and the ImageMagick package.. including perl module Image::Magick

You need to create the top level directories outlined above
and the one to hold your original images when importing a
new batch.  So that would something like:
  source/_gallery/newbatch

The script will create the other directories and files during processing.

=cut
