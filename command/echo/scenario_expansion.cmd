export $TEST ; echo $TEST
export $TEST= ; echo $TEST
export $TEST=test ; echo $TEST
export $TEST ; echo -n $TEST
export $TEST= ; echo -n $TEST
export $TEST=test ; echo -n $TEST
export $TEST="test "; echo -n $TEST
export $TEST="-n"; echo $TEST
export $TEST='-n'; echo $TEST
export $TEST="      -n       "; echo $TEST
export $TEST='      -n       '; echo $TEST
export $TEST="-n       "; echo $TEST
export $TEST='-n       '; echo $TEST
export $TEST="''" ; echo $TEST
export $TEST='""' ; echo $TEST
export $TEST="a     b" ; echo $TEST
export $TEST='a     b' ; echo $TEST
export $TEST="a     b" ; export $TEST2=$TEST ; echo $TEST $TEST2
export $TEST="a     b" ; export $TEST2="$TEST" ; echo $TEST $TEST2
export $TEST="a     b" ; export $TEST2='$TEST' ; echo $TEST $TEST2
