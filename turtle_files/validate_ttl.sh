#!/bin/bash

# Simple script to check the syntax of all present .ttl files in cwd.
# ttl has to be installed -> https://github.com/IDLabResearch/TurtleValidator
# Iterate through all .ttl files in the current directory
for file in *.ttl; do
    if [ -f "$file" ]; then
        echo "Checking file: $file"
        
        # Run ttl syntax checker. Last part is redirecting stderr to stdout.
        output=$(ttl "$file" 2>&1)
        echo "$output"
        echo "-----------------------------------"
    else
        echo "No .ttl files found in the current directory."
        break
    fi
done
