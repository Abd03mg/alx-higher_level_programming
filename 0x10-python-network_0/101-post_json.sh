#!/bin/bash
#script tha send Header with json type.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
