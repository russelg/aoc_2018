#!/usr/bin/env bash

DAY=`printf "%02d" $1`
mkdir "day$DAY";
touch "day$DAY/input.txt";
touch "day$DAY/test.txt";
cp "template.py" "day$DAY/day$DAY.py";