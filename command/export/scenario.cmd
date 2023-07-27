export TEST ; grep TEST=
export TEST=1 ; grep TEST=
export TEST=a ; grep TEST=
export TEST='1' ; grep TEST=
export TEST='a' ; grep TEST=
export ; export
export TEST=1 TEST2=2 TEST3=3 ; grep TEST
export TEST TEST2=2 TEST3 ; grep TEST
export TEST= TEST2= TEST3= ; grep TEST
export TEST=1 TEST2= TEST3= ; grep TEST
export TEST=1 TEST2=2$TEST TEST3=3$TEST2 ; grep TEST
export TEST=1 TEST= TEST ; grep TEST
export TEST TEST=1 TEST= ; grep TEST
export TEST=1 TEST=2 TEST=3 ; grep TEST
export TEST=1 TEST=2 TEST ; grep TEST
export TEST ; bash ; export | grep TEST= ; exit ; export | grep TEST=
export TEST= ; bash ; export | grep TEST= ; exit ; export | grep TEST=
export TEST=1 ; bash ; export | grep TEST= ; exit ; export | grep TEST=
export PATH= ; pwd ; /bin/bash ; exit ; export
export TEST=1 ; export TEST+=2 ; export | grep TEST=
export TEST="cho -n"  ; e$TEST hello
