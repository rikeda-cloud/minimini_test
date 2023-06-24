import os
import json
from datetime import datetime


LOG_DIR = './log/'


def get_format_now_time():
    d = datetime.now()
    return [d.strftime('%Y_%m_%d_%H_%M_%S'), d.strftime('%Y年%m月%d日%H時%M分%S秒')]


class Log:
    def __init__(self):
        self.start_time = get_format_now_time()
        self.log_file = LOG_DIR + 'result_' + self.start_time[0] + '.txt'
        if not os.path.isdir(LOG_DIR):
            os.mkdir(LOG_DIR)
        with open(self.log_file, 'w'):
            pass
        self.__start({'start': self.start_time[1]})

    def __start(self, result: dict):
        with open(self.log_file, 'a') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    def add(self, result: dict):
        with open(self.log_file, 'r') as f:
            data = json.load(f)
            data.update(result)
        with open(self.log_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self):
        with open(self.log_file, 'r') as f:
            data = json.load(f)
        return data

    def search(self, label: str, status: str):
        json_load = self.load()
        search_result_list = []
        for command, data in json_load.items():
            if type(data) == dict:
                [search_result_list.append({command: data}) for key, value in data.items() if key == label and value == status]
        return search_result_list


def main():
    log = Log()
    log.add({"ls -la": {'bash_status': 'KO', 'minishell_status': 'KO'}})
    log.add({"echo": {'bash_status': 'OK', 'minishell_status': 'OK'}})
    # print([print(key, value) for key, value in log.load().items()])
    print(log.search('bash_status', 'OK'))
    print(log.search('bash_status', 'KO'))


if __name__ == '__main__':
    main()
