#!/bin/sh

my_dir=$(dirname $(readlink -f $0))
cd $my_dir
./main