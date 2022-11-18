import import_data as idata
import export_data as edata

contacts = [
    {"fio": "ivan petrov", "phone": "12345"},
    {"fio": "max petrov", "phone": "12333345"},
]
data = []


def set_data_to_file_txt(name_file):
    data_export = data
    edata.set_data_to_file_txt(data_export, name_file)


def set_data_to_file_csv(name_file):
    data_export = data
    edata.set_data_to_file_csv(data_export, name_file)


def set_data_to_file_json(name_file):
    data_export = data
    edata.set_data_to_file_json(data_export, name_file)


def data_init():
    get_data()


def get_data():
    global data
    data = idata.get_data_from_file()
    return data


def set_data(data):
    edata.set_data_to_file(data)


def add_person(fio, phone):
    data.append({'fio': fio, 'phone': phone})
    set_data(data)


def set_person_by_id(id_person, fio, phone):
    data[id_person].update({'fio': fio, 'phone': phone})
    set_data(data)


def del_person_by_id(id_person):
    data.pop(id_person)
    set_data(data)


def find_persons_by_name(param):
    data_filter = list(filter(lambda x: param in x['fio'], data))
    return data_filter


def set_data_to_file_csv(file_name):
    return None
