#!/bin/bash
#script that lists allowed methods.
curl -Is "$1" | grep "Allow" | cut -d " " -f 2-
