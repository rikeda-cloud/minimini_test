from business_logic_layer.utils.diff import diff
from business_logic_layer import commands

def json_sirialize(command, proc1, proc2, setting):
    result_dict = {}
    result_dict['diff_exit_status'] = diff(proc1.returncode, proc2.returncode)
    result_dict['diff_stdout'] = diff(proc1.stdout, proc2.stdout)
    result_dict['diff_stderr'] = diff(proc1.stderr, proc2.stderr)
    result_dict['exit_status'] = {
            setting.default_shell: proc1.returncode,
            setting.minishell: proc2.returncode
    }
    result_dict['stdout'] = {
            setting.default_shell: proc1.stdout,
            setting.minishell: proc2.stdout
    }
    result_dict['stderr'] = {
            setting.default_shell: proc1.stderr,
            setting.minishell: proc2.stderr
    }
    return {command: result_dict}
