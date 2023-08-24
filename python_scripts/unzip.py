"""This code extracts the .rar file to the current directory."""

import rarfile

# Open the RAR file
with rarfile.RarFile(
    "/home/galvsoliveira/data-analytics-engineer-test/data/Data.rar"
) as rf:
    # Extract all files to the current directory
    rf.extractall()
