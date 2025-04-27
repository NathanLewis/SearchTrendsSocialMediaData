#!/usr/bin/env python3
import csv
import sys


def fix_volume(row: dict[str, str]):
    volume = row['Search volume']
    volume = volume.replace('+', '')
    volume = volume.replace('K', '000')
    volume = volume.replace('M', '000000')
    row['Search volume'] = volume
    return row

def fix_csvfile(fname: str, inputname: str, outputname: str):
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        row1 = next(reader)
        sheetheader = list(row1.keys())
        #print(sheetheader)
        #newsheetheader = sheetheader[0:2] + ['volume +'] + sheetheader[2:]
        #print(newsheetheader)
        #print(row1.values())
        with open(fname.replace(inputname, outputname), 'w') as outputcsv:
            writer = csv.DictWriter(outputcsv, fieldnames=sheetheader)
            writer.writeheader()
            row1 = fix_volume(row1)
            #print(row1)
            writer.writerow(row1)
            for row in reader:
                row = fix_volume(row)
                #print(row.values())
                writer.writerow(row)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        fname = sys.argv[1]
        #print(fname)
        fix_csvfile(fname, 'watchdog', 'processed')
    else:
        print('Usage: ./modcsv.py <csv filename>')
        exit(-1)

