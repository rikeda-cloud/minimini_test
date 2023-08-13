export SP="a   b" ; export TEST="a"$SP'b' ; export | grep TEST=
export SP="  a   b  " ; export TEST="a"$SP'b' ; export | grep TEST=
export SP="       " ; export TEST="a"$SP'b' ; export | grep TEST=
export SP="  SP    " ; export TEST="a"$SP'b' ; export | grep TEST=
export SP=" 1 2 3 4 5 6 7 8 9 " ; export TEST="a"$SP'b' ; export | grep TEST=
export SP="1 2 3 4 5 6 7 8 9" ; export TEST="a"$SP'b' ; export | grep TEST=
export SP="1 2 3 4 5 6 7 8 9" ; export TEST=""$SP'' ; export | grep TEST=
export SP="a   b" ; export $SP="LEFT  RIGHT" ; export
export SP=" a   b " ; export $SP="LEFT  RIGHT" ; export
export SP="  b " ; export $SP="LEFT  RIGHT" ; export
export SP=" 1 2 3 4 5 6 7 8 9 " ; export $SP="LEFT  RIGHTH" ; export
export A="a  b" ; B="$A" ; C='$B' ; echo $A $B $C
