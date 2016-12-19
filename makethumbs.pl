#!/usr/bin/env perl

use warnings;
use strict;
use Image::Magick;
use File::Copy;


my $dir = 'pics/input/';
my %file;

chdir $dir;
foreach my $item (<*>)
{
    next if $item eq 'processed';
    my ($name, $ext) = split /\./, $item;
    $item =~ /^(.+)\.(\w+)$/;

    $file{'filename'} = $item;
    $file{'name'}     = $1;
    $file{'ext'}      = $2;
    print "Processing $item\n";
    make_icon(%file);
    make_inline(%file);
    copy ($item, "../../static/pics/");
    move ($item, "../processed/");
}


#my $img = $ARGV[0];
#print "$img\n";
#exit;

sub make_inline
{
    my (%file) = @_;

    my $magick = new Image::Magick;
    $magick->Read("$file{filename}");
    #$magick->Resize(width=>'320', height=>'200');
    $magick->Resize(geometry=>'x200');
    $magick->Write("../../static/pics/inline_$file{name}.$file{ext}");
}

sub make_icon
{
    my (%file) = @_;

    my $magick = new Image::Magick;
    $magick->Read("$file{filename}");
    my ($width, $height) = $magick->Get('width', 'height');

    $magick->Resize(geometry => int($width/2).'x'.int($height/2));
    $magick->Resize(geometry => '180x');
    $magick->Resize(geometry => 'x180<');

    my($nwidth, $nheight) = $magick->Get('width', 'height');
    my $xpos = int(( $nwidth - 120 ) / 2) - 60;
    my $ypos = int(( $nheight - 120 ) / 2) - 60;
    $magick->Crop(geometry => "120x120+$xpos+$ypos", gravity => 'Center');
    my $thumb_mask = $magick->Clone();
    $thumb_mask->Set('alpha' => 'Off');
    $thumb_mask->Colorize( fill => 'white', opacity => '100%' );

    $thumb_mask->Draw( fill => 'black',
                       primitive => 'polygon',
                       points => '0,0 0,15 15,0');
    $thumb_mask->Draw( fill => 'white',
                       primitive => 'circle',
                       points => '15,15 15,0');
    my $new_2 = $thumb_mask->Clone();
    $new_2->Flip();
    $thumb_mask->Composite( compose => 'Multiply', 'image' => $new_2 );

    my $new_3 = $thumb_mask->Clone();
    $new_3->Flop();
    $thumb_mask->Composite( compose => 'Multiply', 'image' => $new_3 );

    $thumb_mask->Set('background' => 'Gray50');
    $thumb_mask->Set('alpha' => 'Shape');

    $thumb_mask->Raise(raise => 'True', geometry => '4x4');
    my $thumb_lighting = $thumb_mask->Clone();
    $thumb_lighting->Set('bordercolor' => 'None');
    $thumb_lighting->Set('border'      => '1x1');
    $thumb_lighting->Set('alpha'       => 'Extract');
    $thumb_lighting->Blur('geometry'       => '0x10');
    $thumb_lighting->Shade(geometry => '80x40');
    $thumb_lighting->Set('alpha'       => 'On');
    $thumb_lighting->Set('background'  => 'Gray50');
    $thumb_lighting->Set('alpha'       => 'Background');
    $thumb_lighting->AutoLevel(channel => 'alpha');
    $thumb_lighting->[-1]->Function(function => 'polynomial', parameters => [3.5, -5.05, 2.05, 0.3]);

    my $new_4 = $thumb_lighting->Clone();
    $new_4->Set(alpha => 'Extract');
    $new_4->Blur(geometry => '0x2');

    $thumb_lighting->Composite(compose => 'Multiply', image => $new_4);

    $magick->Set('alpha' => 'On');
    $magick->Composite(compose => 'HardLight', image => $thumb_lighting);
    $magick->Set('alpha' => 'Copy');
    $magick->Composite(compose => 'CopyOpacity', image => $thumb_mask);
    $magick->Write("../../static/pics/icon_$file{name}.png");
}


