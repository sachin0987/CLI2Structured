#!/bin/bash

current_date=$(date +"%Y-%m-%d")
oper_audit_directory="/path/to/oper_audit_splunk/"
allchecks_directory="/path/to/allchecks_splunk/"
output_directory="/path/to/output/directory/"

oper_audit_file="${oper_audit_directory}oper_audit_splunk_${current_date}.csv"
allchecks_file="${allchecks_directory}allchecks_splunk.csv"
output_file="${output_directory}merged_data_${current_date}.csv"

if [[ -f "$oper_audit_file" && "$oper_audit_file" == *"$current_date"* ]]; then
    echo "Merging $oper_audit_file into $allchecks_file using paste command..."
    paste -d ',' "$allchecks_file" "$oper_audit_file" >> "$output_file"
    echo "Merge complete. Merged data saved to $output_file"
else
    echo "First file ($oper_audit_file) either doesn't exist or doesn't contain data for the current date ($current_date)."
fi
