export SP_WORD="a   b" ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD="  a   b  " ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD="       " ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD="  SP    " ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD=" 1 2 3 4 5 6 7 8 9 " ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD="1 2 3 4 5 6 7 8 9" ; export TEST="a"$SP_WORD'b' | export | grep TEST=
export SP_WORD="1 2 3 4 5 6 7 8 9" ; export TEST=""$SP_WORD'' | export | grep TEST=
export SP_WORD="a   b" ; export $SP_WORD="LEFT  RIGHTH" | export | grep TEST=
export SP_WORD=" a   b " ; export $SP_WORD="LEFT  RIGHTH" | export | grep TEST=
export SP_WORD="  b " ; export $SP_WORD="LEFT  RIGHTH" | export | grep TEST=
export SP_WORD=" 1 2 3 4 5 6  7 8 9 " ; export $SP_WORD="LEFT  RIGHTH" | export | grep TEST=
