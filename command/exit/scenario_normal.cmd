bash ; exit
bash ; bash ; exit
bash ; bash ; bash exit
bash ; exit 1
bash ; bash ; exit 1
bash ; bash ; bash exit 1
bash ; exit -- 1
bash ; bash ; exit -- 1
bash ; bash ; bash exit -- 1
bash ; exit -- 1 2
bash ; bash ; exit -- 1 2
bash ; bash ; bash exit -- 1 2
bash ; exit -- a 2
bash ; bash ; exit -- a 2
bash ; bash ; bash exit -- a 2
export PATH ; bash ; exit ; export | grep PATH=
export PATH= ; bash ; exit ; export | grep PATH=
export PATH="/NOT_EXIST_PATH" ; bash ; exit ; export | grep PATH=
echo $SHLVL ; bash ; echo $SHLVL ; exit 1 1 ; echo $SHLVL
echo $SHLVL ; bash ; echo $SHLVL ; exit a 1 ; echo $SHLVL
echo $SHLVL ; bash ; echo $SHLVL ; unset HSLVL ; echo $SHLVL ; exit 1 ; echo $SHLVL
echo $SHLVL ; bash ; echo $SHLVL ; bash ; echo $SHLVL ; exit 1 1 ; echo $SHLVL
