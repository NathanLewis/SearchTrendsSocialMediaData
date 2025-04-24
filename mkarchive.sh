#!/usr/bin/bash

set -eu

cp *.csv original
# repack them
for file in original/*.csv; do ./modcsv.py $file; done

cd modified
echo $PWD

list=( $(ls -1 *.csv) ) 
echo ${list[0]}
echo ${list[-1]}

echo ${list[0]:0:12}
echo ${list[0]: -17:-4}
tarfile=${list[0]:0:12}${list[0]: -17:-4}_${list[-1]: -17:-4}.tar.gz
echo $tarfile
#echo ${list[0]:0:12}${list[0]: -17:-4}
echo tar -zcvf $tarfile \*\.csv
tar -zcvf $tarfile *.csv
country=${tarfile:9:2}
aws s3 cp $tarfile s3://searchtrendssocialmediadata/${country}/
tar -ztvf $tarfile | awk '{ print $6 }' | xargs rm
tar -ztvf $tarfile | awk '{ print "../original/"$6 }' | xargs rm
tar -ztvf $tarfile | awk '{ print "../"$6 }' | xargs rm
