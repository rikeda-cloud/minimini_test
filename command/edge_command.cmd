< < < |<<EOF |  ls > outfile
<<EOF | < < < |<EOF2 | ls >outfile
<<EOF |<<EOF2 < < < |<EOF3 | ls >outfile
sleep 5 | <<EOF |<<EOF2 < < < |<EOF3 | ls >outfile

