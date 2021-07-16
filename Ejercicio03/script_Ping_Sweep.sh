#!/bin/bash
 
ip=192.168.0.

for i in "$ip"{0..255}; do
    ping $i -c 1 | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

