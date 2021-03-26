#!/usr/bin/perl -w
use strict;
use warnings;
use autodie;

open(my $table,"<", $ARGV[0]);
<$table>; #omit header
while(<$table>){
  my $genes = (split(/\t/,$_))[2];
  $genes =~ s/, /\n/g;
  print $genes;
}
close $table;
