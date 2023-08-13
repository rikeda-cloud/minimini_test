export TEST ; export | grep TEST=
export TEST=1 ; export | grep TEST=
export TEST=a ; export | grep TEST=
export TEST='1' ; export | grep TEST=
export TEST='a' ; export | grep TEST=
export TEST=1 TEST2=2 TEST3=3 ; export | grep TEST
export TEST TEST2=2 TEST3 ; export | grep TEST
export TEST= TEST2= TEST3= ; export | grep TEST
export TEST=1 TEST2= TEST3= ; export | grep TEST
export TEST=1 TEST2=2$TEST TEST3=3$TEST2 ; export | grep TEST
export TEST=1 TEST= TEST ; export | grep TEST
export TEST TEST=1 TEST= ; export | grep TEST
export TEST=1 TEST=2 TEST=3 ; export | grep TEST
export TEST=1 TEST=2 TEST ; export | grep TEST
export PATH= ; pwd ; /bin/bash ; exit ; export
export TEST=1 ; export TEST+=2 ; export | grep TEST=
export TEST="cho -n"  ; e$TEST hello
