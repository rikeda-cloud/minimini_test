echo
echo                                                              
echo -n
echo -n -n -n
echo -nnn
echo abc
echo -n abc
echo -nnn abc
echo abc -n
echo abc -nnn
echo -n -n abc -n -n
echo -n abc -n
echo abc -nnn abc
echo 1 2 3 4 5 6 7 8 9
echo 1 2 3 4 5 6 7 8 9 -n
echo -n 1 2 3 4 5 6 7 8 9
echo 1  2  3  4  5  6  7  8  9
echo 1  2  3  4  5  6  7  8  9 -n
echo echo echo echo echo echo echo 
echo echo echo echo echo echo echo -n
echo ABCDEFGHIJKLMNOPQRSTUVWXYZ
echo ABCDEFGHIJKLMNOPQRSTUVWXYZ -n
echo -nvim abc
echo abc -nvim
echo abc -nvim abc
echo my name is XXX.
echo my     name          is       XXX.          -n
-n echo my     name          is       XXX.
echo $$$$
echo $$$$$
echo -n $$$$
echo -n $$$$$
echo $NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV
echo "$NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV"
echo '$NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV'
echo '$NOT_EXIST_ENV' '$NOT_EXIST_ENV' '$NOT_EXIST_ENV'
echo "$NOT_EXIST_ENV" "$NOT_EXIST_ENV" "$NOT_EXIST_ENV"
echo -n $NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV
echo -n "$NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV"
echo -n '$NOT_EXIST_ENV $NOT_EXIST_ENV $NOT_EXIST_ENV'
echo -n '$NOT_EXIST_ENV' '$NOT_EXIST_ENV' '$NOT_EXIST_ENV'
echo -n "$NOT_EXIST_ENV" "$NOT_EXIST_ENV" "$NOT_EXIST_ENV"
echo $SHELL
echo "$SHELL"
echo '$SHELL'
echo 1$SHELL2
echo 1"$SHELL"2
echo 1'$SHELL'2
echo -- abc
echo -n -- abc
echo -n abc --
