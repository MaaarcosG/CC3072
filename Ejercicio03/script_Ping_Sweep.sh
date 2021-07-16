#!/bin/bash

for ip  in `seq 1 255` ; do
ping $1.$ip -c 1| grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

