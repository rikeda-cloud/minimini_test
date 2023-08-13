pwd ; pwd ; pwd
cd .. ; pwd
cd NOT_EXIST_DIR ; pwd
mkdir test ; cd test ; pwd
mkdir test ; cd test ; rm -r ../test ; pwd
mkdir test ; cd test ; rm -r ../test ; cd . ; pwd
mkdir test ; cd test ; rm -r ../test ; cd .. ; pwd
mkdir test ; cd test ; rm -r ../test ; cd NOT_EXIST_DIR ; pwd
mkdir test ; chmod 000 test ; cd test ; pwd
unset PWD ; pwd
unset PWD ; cd . ; pwd
unset PWD ; cd .. ; pwd
unset PWD ; cd / ; pwd
unset OLDPWD ; pwd
unset OLDPWD ; cd . ; pwd
unset OLDPWD ; cd .. ; pwd
unset OLDPWD ; cd / ; pwd
export PWD ; pwd
export PWD ; cd . ; pwd
export PWD ; cd .. ; pwd
export PWD ; cd / ; pwd
export PWD= ; pwd
export PWD= ; cd . ; pwd
export PWD= ; cd .. ; pwd
export PWD= ; cd / ; pwd
export PWD="/NOT_EXIST_DIR" ; pwd
export PWD="/NOT_EXIST_DIR" ; cd . ; pwd
export PWD="/NOT_EXIST_DIR" ; cd .. ; pwd
export PWD="/NOT_EXIST_DIR" ; cd / ; pwd
