import hashlib
import json
import os

RECORD_FILE = "checksums.json"

if os.path.exists(RECORD_FILE):
    with open(RECORD_FILE, "r") as file:
        old_record = json.load(file)
else:
    old_record = {}

files = input("Enter file names separated by comma: ").split(",")
files = [filename.strip() for filename in files if filename.strip()]

new_record = {}

print("\n----- FILE INTEGRITY REPORT -----")

for filename in files:
    if os.path.exists(filename):
        with open(filename, "rb") as file:
            checksum = hashlib.md5(file.read()).hexdigest()

        new_record[filename] = checksum

        if filename not in old_record:
            print(filename, ": New File")
        elif old_record[filename] == checksum:
            print(filename, ": Not Modified")
        else:
            print(filename, ": Modified")
    else:
        print(filename, ": Missing File")

for filename in old_record:
    if filename not in files:
        print(filename, ": Missing File")

with open(RECORD_FILE, "w") as file:
    json.dump(new_record, file, indent=4)

print("\nChecksum record updated.")
