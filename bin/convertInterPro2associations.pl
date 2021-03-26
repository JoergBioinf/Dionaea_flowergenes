#!/usr/bin/perl -w
use strict;
use warnings;
use autodie;

=pod

Take the output of interproscan and generate a geneOntology
associations file as needed for Ontologizer
Writes results to stdout
results file has to end with '_simple-assoc-file.ids'
format of assoc file is:

GoStat IDs Format Version 1.0
TRINITY_DN55158_c3_g1   GO:0003735,GO:0005840,GO:0006412,GO:0005622
TRINITY_DN62761_c0_g1   GO:0008113,GO:0055114

=cut

my $interProFile = "/storage/compevolbiol/projects/carnivores/RESULTS/Dm_Interproscan.tsv";
my %annotations;
open(my $ipHandle, "<", $interProFile);
while(<$ipHandle>){
  chomp;
  my ($protein, $db, $gos) = (split(/\t/, $_))[0,3,13];
  next unless $db eq 'Pfam';
  next unless $gos;
  map {$annotations{$protein}{$_}++} split(/\|/,$gos);
}

print "GoStat IDs Format Version 1.0\n";
foreach my $protein (keys %annotations){
  print "$protein\t", join(",",keys %{$annotations{$protein}}), "\n";
}
