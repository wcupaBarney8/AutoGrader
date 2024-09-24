#!/bin/bash

if [ -f "$1" ]; then
  x=$RANDOM
  d2h=`echo "ibase=10; obase=16; $x"|bc`
  INPUT=`echo "${d2h^^}" | sed 's/^0X//'`
  LENGTH=`echo $INPUT | wc -c`
  eb=$(echo "ibase=16; obase=2; $INPUT" | bc)
  padding=$(( 32 - ${#eb}))
  for i in $( seq 1 ${padding} )
  do
    eb="0${eb}"
  done

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
