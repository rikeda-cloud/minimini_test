export TEST ; bash ; echo $TEST ; exit ; export | grep TEST=
bash ;export TEST=0 ; exit $TEST
bash ;export TEST=-0 ; exit $TEST
bash ;export TEST=1 ; exit $TEST
bash ;export TEST=-1 ; exit $TEST
bash ;export TEST=--1 ; exit $TEST
bash ;export TEST=255 ; exit $TEST
bash ;export TEST=--255 ; exit $TEST
bash ;export TEST=256 ; exit $TEST
bash ;export TEST=-256 ; exit $TEST
bash ;export TEST=--256 ; exit $TEST
bash ;export TEST=1111 ; exit $TEST
bash ;export TEST=-1111 ; exit $TEST
bash ;export TEST=--1111 ; exit $TEST
bash ;export TEST=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ; exit $TEST
bash ;export TEST=9223372036854775807 ; exit $TEST
bash ;export TEST=9223372036854775808 ; exit $TEST
bash ;export TEST=-9223372036854775807 ; exit $TEST
bash ;export TEST=-9223372036854775808 ; exit $TEST
bash ;export TEST=11111111111111111111111111111111111111111 ; exit $TEST
bash ;export TEST="1 2"; exit $TEST
bash ;export TEST="1 2 3"; exit $TEST
bash ;export TEST="-- 1"; exit $TEST
bash ;export TEST="-- 1 2"; exit $TEST
bash ;export TEST="-- 1 2 3"; exit $TEST
bash ;export TEST="../"; exit $TEST
