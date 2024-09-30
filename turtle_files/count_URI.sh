#!/bin/bash

# Directory where script shall be executed.
DIR="./"  

# Map as container for occurences.
declare -A uri_counts

# Loop through .ttl-files in directory
for file in "$DIR"*.ttl; do
  # line by line
  while IFS= read -r line; do
    # only look into defined prefixes
    if [[ "$line" =~ ^@prefix ]]; then
      # Regex to find and extract URI between < >
      if [[ "$line" =~ \<([^\>]+)\> ]]; then
        uri="${BASH_REMATCH[1]}"
        # Increment count
        ((uri_counts["$uri"]++))
      fi
    fi
  done < "$file"
done

echo "Häufigkeit der verwendeten URIs in @prefix-Zeilen:"
for uri in "${!uri_counts[@]}"; do
  echo "$uri: ${uri_counts[$uri]}"
done
