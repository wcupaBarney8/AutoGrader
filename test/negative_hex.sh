#!/bin/bash

if [ -f "$1" ]; then
  x=$(( $RANDOM * -1 ))
  d2h=`echo "ibase=10; obase=16; 2^32+$x"|bc`
  eh=`echo "${d2h^^}" | sed 's/^0X//'`
  eb=$(echo "ibase=16; obase=2; $eh" | bc)
  ab=`./$1 $x`
  if [[ "${ab}" == "${eh}" ]]; then
    echo "$2 passes"
  else
    echo "Random number: " $x
    echo "Expected binary representation : " ${eb}
    echo "Expected hex representation    : " ${eh}
    echo "Actual hex representation      : " ${ab}
  fi
else
  echo "$1 does not exists. $2 fails"
fi
