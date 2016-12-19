#!/usr/bin/env perl

use Pod::Markdown;

use strict;
use warnings;

my $parser = Pod::Markdown->new;
$parser->parse_from_filehandle(\*STDIN);
print $parser->as_markdown;

