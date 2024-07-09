#!/bin/bash

for i in $(ls $PWD); do s=$i; cat $i > tmp; rm $i; mv tmp $s ; done;
