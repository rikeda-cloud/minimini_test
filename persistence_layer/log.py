import os
import json
from datetime import datetime


def get_format_now_time(file_format):
    d = datetime.now()
    return d.strftime(file_format)


class Log:
    def __init__(self, setting):
        self.start_time = get_format_now_time(setting.log_file_format)
        self.log_file = setting.log_dir + 'log_' + self.start_time + '.json'
        if not os.path.isdir(setting.log_dir):
            os.mkdir(setting.log_dir)
        with open(self.log_file, 'w'):
            pass
        self.__json_init()

    def __json_init(self):
        with open(self.log_file, 'a') as f:
            json.dump({}, f, indent=2, ensure_ascii=False)

    def add(self, result: dict):
        try:
            with open(self.log_file, 'r+') as f:
                try:
                    data = json.load(f)
                except json.decoder.JSONDecodeError:
                    data = {}
                data.update(result)
                f.seek(0)
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.truncate()
        except FileNotFoundError:
            with open(self.log_file, 'w') as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

    def load(self):
        with open(self.log_file, 'r') as f:
            data = json.load(f)
        return data

    def search(self, label: str, status: str):
        json_load = self.load()
        search_result_list = []
        for command, data in json_load.items():
            for key, value in data.items():
                if key == label and value == status:
                    search_result_list.append({command: data})
        return search_result_list
