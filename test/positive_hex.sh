#!/bin/bash

if [ -f "$1" ]; then
  x=$RANDOM
  d2h=`echo "ibase=10; obase=16; $x"|bc`
  eh=`echo "${d2h}" | sed 's/^0x//'`
  LENGTH=`echo $INPUT | wc -c`
  eb=$(echo "ibase=16; obase=2; $eh" | bc)
  padding=$(( 8 - ${#eh}))
  for i in $( seq 1 ${padding} )
  do
    eh="0${eh}"
  done

  padding=$(( 32 - ${#eb}))
  for i in $( seq 1 ${padding} )
  do
    eb="0${eb}"
  done

  ab=`./$1 $x`
  if [[ "${ab}" == "${eh}" ]]; then
    echo "$2 passes"
  else
    echo "Random number: " $x
    echo "Expected binary representation: " ${eb}
    echo "Expected hex representation   : " ${eh}
    echo "Actual hex representation     : " ${ab}
  fi
else
  echo "$1 does not exists. $2 fails"
fi
