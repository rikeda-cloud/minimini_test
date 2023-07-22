from business_logic_layer.utils.diff import diff
from business_logic_layer import commands

def json_sirialize(command_line, proc1, proc2):
    nest_result = {}
    result_dict = {}
    result_dict['diff_exit_status'] = diff(proc1.returncode, proc2.returncode)
    result_dict['diff_stdout'] = diff(proc1.stdout, proc2.stdout)
    result_dict['diff_stderr'] = diff(proc1.stderr, proc2.stderr)
    p1_retcode, p2_retcode = proc1.returncode, proc2.returncode
    result_dict['exit_status'] = {commands.BASH: p1_retcode, commands.MINISHELL: p2_retcode}
    result_dict['stdout'] = {commands.BASH: proc1.stdout, commands.MINISHELL: proc2.stdout}
    result_dict['stderr'] = {commands.BASH: proc1.stderr, commands.MINISHELL: proc2.stderr}
    nest_result[command_line] = result_dict
    return nest_result
