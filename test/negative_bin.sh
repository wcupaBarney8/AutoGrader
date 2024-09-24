#!/bin/bash

if [ -f "$1" ]; then
  x=$(( $RANDOM * -1 ))
  d2h=`echo "ibase=10; obase=16; 2^32+$x"|bc`
  INPUT=`echo "${d2h^^}" | sed 's/^0X//'`
  LENGTH=`echo $INPUT | wc -c`
  eb=$(echo "ibase=16; obase=2; $INPUT" | bc)
  ab=`./$1 $x`
  if [[ "${ab}" == "${eb}" ]]; then
    echo "$2 passes"
  else
    echo "Random number: " $x
    echo "Expected binary representation: " ${eb}
    echo "Actual binary representation  : " ${ab}
  fi
else
  echo "$1 does not exists. $2 fails"
fi
