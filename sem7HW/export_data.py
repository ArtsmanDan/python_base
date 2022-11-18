import json

DEFAULT_NAME_FILE = "data_file.json"


def set_data_to_file(data):
    set_data_to_file_json(data, DEFAULT_NAME_FILE)


def set_data_to_file_json(data, name_file):
    with open(name_file, "w") as write_file:
        json.dump(data, write_file)
        write_file.close()


def set_data_to_file_txt(data, name_file):
    with open(name_file, "w") as write_file:
        for item in data:
            s = f'"{item["fio"]}";"{item["phone"]}"\n'
            write_file.write(s)
        write_file.close()


def set_data_to_file_csv(data, name_file):
    with open(name_file, "w") as write_file:
        for item in data:
            write_file.write(f'"{data[item]["fio"]}";"{data[item]["phone"]}"\n')
        write_file.close()


