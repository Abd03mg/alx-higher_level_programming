#!/bin/bash
#script that lists allowed methods.
curl -Is "$1" | grep "Alow" | sed -d " " -f 2-
