#!/usr/bin/env python3
#import json
import csv
#import argparse
import sys

contents = {}
if len(sys.argv) > 1:
    fname = sys.argv[1]
    #print(fname)
    print(fname.replace('original', 'modified'))
else:
    print('Usage: ./modcsv.py <csv filename>')
    exit(-1)

def fix_volume(row: dict[str, str]):
    volume = row['Search volume']
    volume = volume.replace('+', '')
    volume = volume.replace('K', '000')
    volume = volume.replace('M', '000000')
    row['Search volume'] = volume
    return row

with open(fname) as csvfile:
    reader = csv.DictReader(csvfile)
    row1 = next(reader)
    sheetheader = list(row1.keys())
    #print(sheetheader)
    #newsheetheader = sheetheader[0:2] + ['volume +'] + sheetheader[2:]
    #print(newsheetheader)
    #print(row1.values())
    with open(fname.replace('original', 'modified'), 'w') as outputcsv:
        writer = csv.DictWriter(outputcsv, fieldnames=sheetheader)
        writer.writeheader()
        row1 = fix_volume(row1)
        #print(row1)
        writer.writerow(row1)
        for row in reader:
            row = fix_volume(row)
            #print(row.values())
            writer.writerow(row)
