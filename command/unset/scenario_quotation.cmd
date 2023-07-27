export TEST ; unset "TEST" ; export | grep TEST=
export TEST=1 ; export TEST_NAME="TEST" ; unset $TEST_NAME ; export | grep TEST=
export TEST=1 ; export TEST_NAME="TEST" ; unset "$TEST_NAME" ; export | grep TEST=
export TEST=1 ; export TEST_NAME="TEST" ; unset '$TEST_NAME' ; export | grep TEST=
