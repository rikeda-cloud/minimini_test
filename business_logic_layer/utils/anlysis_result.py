def anlysis_result(results: dict[str, str]):
    after_anlysis_result = {
            'total_exit_status_faild': 0,
            'total_stdout_faild': 0,
            'total_stderr_faild': 0
    }
    for result in results.values():
        if result['diff_exit_status'] == 'KO':
            after_anlysis_result['total_exit_status_faild'] += 1
        if result['diff_stdout'] == 'KO':
            after_anlysis_result['total_stdout_faild'] += 1
        if result['diff_stderr'] == 'KO':
            after_anlysis_result['total_stderr_faild'] += 1
    return after_anlysis_result

