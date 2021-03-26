#!/bin/bash

java -jar ../bin/Ontologizer.jar --go ../data/go.obo -a ../data/Dm_simple-assoc-file.ids -p ../data/Dm.popset -s reusedGenes.list -d 0.05 --mtc "Benjamini-Hochberg" --annotation
