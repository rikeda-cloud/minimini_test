mkdir test ; cd test ; echo $PWD
mkdir test ; cd test ; cd NOT_EXIST_FILE ; echo $PWD
mkdir test ; cd test ; cd .. ; echo $PWD
mkdir test ; cd test ; cd ... ; echo $PWD
mkdir test ; cd test ; cd ../../../../../ ; echo $PWD
mkdir test ; cd test ; cd ./././././ ; echo $PWD
mkdir test ; chmod 000 test ; cd test ; echo $PWD
mkdir test ; chmod 000 test ; chmod 777 ; cd test ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; cd test2 ; cd NOT_EXIST_FILE ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; cd test2 ; cd .. ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; cd test2 ; cd ... ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; cd test2 ; cd ../../../../../ ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; cd test2 ; cd ./././././ ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; chmod 000 test2 ; cd test2 ; echo $PWD
mkdir test ; cd test ; mkdir test2 ; chmod 000 test2 ; chmod 777 ; cd test2 ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; cd NOT_EXIST_FILE ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; cd . ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; cd .. ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; mkdir ../test ; cd . ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; export | grep PWD= ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; cd . ; export | grep PWD= ; echo $PWD
mkdir test ; cd test ; rm -r ../test ; cd NOT_EXIST_FILE ; export | grep PWD= ; echo $PWD
echo $PWD ; cd ../ ; echo $PWD $OLDPWD ; cd ../ ; echo $PWD $OLDPWD ; echo $PWD
unset PWD ; cd ../ ; export | grep PWD ; cd ../ ; export | grep PWD
