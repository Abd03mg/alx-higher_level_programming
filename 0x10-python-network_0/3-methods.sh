#!/bin/bash
#script that lists allowed methods.
curl -Is "$1" | grep "Alow" | cut -d " " -f 2-
