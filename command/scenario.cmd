< < < | <<EOF |  ls > outfile
<<EOF | < < < |<EOF2 | ls >outfile
<<EOF |<<EOF2 < < < |<EOF3 | ls >outfile
sleep 5 | <<EOF |<<EOF2 < < < |<EOF3 | ls >outfile
$NOT_EXIST_ENV | $NOT_EXIST_ENV | ls
mkdir TEST | ls ; rm -r TEST
touch TEST | ls ; rm TEST
touch TEST | mv TEST ../ ; rm TEST ../TEST
ls > TEST ; cat TEST | cat > TEST2 ; cat TEST ; cat TEST2 ; rm TEST TEST2
cat << EOF > TEST >TEST2 >TEST3 ; cat TEST ; cat TEST2 ; cat TEST3; rm TEST TEST2 TEST3
echo 123 > TEST ; echo 456 > TEST ; echo 789 >> TEST ; cat TEST ; rm TEST
echo 123 > TEST ; echo 456 > TEST ; echo 789 >> TEST ; echo 000 > TEST ; cat TEST ; rm TEST
