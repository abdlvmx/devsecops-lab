#!/bin/sh

if [ "$#" -ne 2 ]; then
echo "Usage: $0 PATTERN FILE" >&2
exit 2
fi

pattern=$1
file=$2

grep -q "$pattern" "$file"
grep_status=$?

if [ "$grep_status" -eq 0 ]; then
echo "MATCH"
exit 0
elif [ "$grep_status" -eq 1 ]; then
echo "NO_MATCH"
exit 1
else
echo "ERROR: grep failed with status $grep_status" >&2
exit "$grep_status"
fi
