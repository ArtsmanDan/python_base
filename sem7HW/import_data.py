import json

DEFAULT_NAME_FILE = "data_file.json"


def get_data_from_file_json(name_file):
    with open(name_file, "r") as read_file:
        data = json.load(read_file)
        read_file.close()
    return data


def get_data_from_file():
    return get_data_from_file_json(DEFAULT_NAME_FILE)


def get_data_from_file_txt(name_file):
    with open(name_file, "r") as read_file:
        text = read_file.readlines()
        read_file.close()
        data = []
        for item in text:
            line = item.split(';')
            data.append({{'fio': line[0], 'phone': line[1]}})
        data = json.load(read_file)
    return data


def get_data_from_file_csv(name_file):
    with open(name_file, "r") as read_file:
        text = read_file.readlines()
        read_file.close()
        data = []
        for item in text:
            line = item.split(';')
            data.append({{'fio': line[0], 'phone': line[1]}})
        data = json.load(read_file)
    return data
