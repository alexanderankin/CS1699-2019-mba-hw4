#!/usr/bin/env bash


source_dir=inputData
rm -rf $soure_dir
mkdir -p $source_dir
input_files='shakespeare.tar.gz'

for file in $input_files; do
  echo "cp $file $source_dir"
  cp $file $source_dir
  echo "(cd $source_dir; tar xvzf $file)"
  (cd $source_dir; tar xvzf $file; find . -mindepth 2 -type f -exec mv -f '{}' . ';'; find . -type d -delete)
  echo "rm $source_dir/$file"
  rm $source_dir/$file
done

