#!/bin/bash
#HTTP statis code.
curl -sw "%{http_code}" "$1" -o /dev/null
