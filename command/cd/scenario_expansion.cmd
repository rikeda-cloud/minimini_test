cd $PATH ; echo $PWD
cd $PWD ; echo $PWD
cd $OLDPWD ; echo $PWD
cd $OLDPWD ; echo $OLDPWD
cd $NOT_EXIST_ENV
export TEST="/" ; cd $TEST
export TEST="." ; cd $TEST
export TEST=".." ; cd $TEST
export TEST="..." ; cd $TEST
export TEST="../../../../../../../" ; cd $TEST
export TEST ; cd $TEST
export TEST= ; cd $TEST
export TEST="../" ; cd $TEST"./"
export TEST="../" ; cd $TEST"../"
export TEST="../" ; cd $TEST"./NOT_EXIST_DIR"
export TEST="../" ; cd $TEST"../NOT_EXIST_DIR"
