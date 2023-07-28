from business_logic_layer.utils.diff import diff
from business_logic_layer import commands

def json_sirialize(command_line, result1, result2):
    bash= list(result1)
    mini= list(result2)
    nest_result = {}
    result_dict = {}
    result_dict['diff_stdout'] = diff(bash[0], mini[0])
    result_dict['diff_stderr'] = diff(bash[1], mini[1])
    result_dict['diff_exit_status'] = diff(bash[2], mini[2])
    result_dict['stdout'] = {commands.BASH: bash[0], commands.MINISHELL: mini[0]}
    result_dict['stderr'] = {commands.BASH: bash[1], commands.MINISHELL: mini[1]}
    result_dict['exit_status'] = {commands.BASH: bash[2], commands.MINISHELL: mini[2]}
    nest_result[command_line] = result_dict
    return nest_result
