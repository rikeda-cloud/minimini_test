export TEST ; export | grep TEST= ; unset TEST ; export | grep TEST= 
export TEST= ; export | grep TEST= ; unset TEST ; export | grep TEST= 
export TEST=test ; export | grep TEST= ; unset TEST ; export | grep TEST= 
export TEST ; export | grep TEST= ; unset TEST NOT_EXIST_ENV ; export | grep TEST= 
export TEST ; export | grep TEST= ; unset TEST NOT_EXIST_ENV ; export | grep NOT_EXIST_ENV= 
