#!/bin/bash
#Script tha sends POST request.
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
