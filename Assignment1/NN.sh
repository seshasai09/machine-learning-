#!/bin/sh
k=$1
trainFileName=$2
testFileName=$3
python run_knn.py $k $trainFileName $testFileName

