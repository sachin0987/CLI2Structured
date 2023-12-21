#!/bin/bash

current_date=$(date +"%Y-%m-%d")
oper_audit_directory="/path/to/oper_audit_splunk/"
allchecks_directory="/path/to/allchecks_splunk/"
output_directory="/path/to/output/directory/"

# Function to find the file for the current date
find_file_for_date() {
    local dir="$1"
    local file_pattern="test_${current_date}_*_splunk.csv"
    local matching_files=($dir$file_pattern)

    if [ ${#matching_files[@]} -eq 1 ]; then
        echo "${matching_files[0]}"
    else
        echo "File for the current date not found or multiple matching files exist."
        exit 1
    fi
}

oper_audit_file=$(find_file_for_date "$oper_audit_directory")
allchecks_file="${allchecks_directory}allchecks_splunk.csv"
output_file="${output_directory}merged_data_${current_date}.csv"

if [[ -f "$oper_audit_file" ]]; then
    echo "Merging $oper_audit_file into $allchecks_file..."
    paste -d ',' "$allchecks_file" "$oper_audit_file" >> "$output_file"
    echo "Merge complete. Merged data saved to $output_file"
else
    echo "File for the current date ($current_date) not found in $oper_audit_directory."
fi
