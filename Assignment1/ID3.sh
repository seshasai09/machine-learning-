#!/bin/sh
depth=$1
trainFileName=$2
testFileName=$3
python run_dt.py $depth $trainFileName $testFileName
