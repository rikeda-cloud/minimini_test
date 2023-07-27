cd ../ | echo $PWD
cd ../ | echo $OLDPWD
cd ../ | sleep 1 ; echo $PWD
cd ../ | sleep 1; echo $OLDPWD
sleep 1 | cd .. ; echo $PWD
sleep 1 | cd .. | sleep 1 ; echo $PWD
