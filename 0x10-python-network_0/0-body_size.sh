#!/usr/bin/bash
#Script that counts the size of url body.
curl -s "$1" | wc -c
