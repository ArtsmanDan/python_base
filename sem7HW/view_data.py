import model_data as model


def draw_menu():
    print('1 - просмотр полного списка; 2 - добавления контакта; 3 - редактирование контакта'
          ' 4 - удаление контакта; 5 - поиск контакта; 0 - выход')
    print('6 - экспорт в txt; 7 - экспорт в csv; 8 - экспорт в json')
    x = int(input())
    if x == 0: exit()
    if x == 1:
        model.get_data()
        draw_full_list_contact()
    if x == 2:
        add_person()
    if x == 3:
        set_person_by_id()
    if x == 4:
        del_person_by_id()
    if x == 5:
        find_persons_by_name()
    if x == 6:
        set_data_to_file_txt()
    if x == 7:
        set_data_to_file_csv()
    if x == 8:
        set_data_to_file_json()


def set_data_to_file_txt():
    print('Введите имя файла для экспорта')
    name_file = input()
    model.set_data_to_file_txt(name_file + ".txt")


def set_data_to_file_csv():
    print('Введите имя файла для экспорта')
    name_file = input()
    model.set_data_to_file_csv(name_file + ".csv")


def set_data_to_file_json():
    print('Введите имя файла для экспорта')
    name_file = input()
    model.set_data_to_file_json(name_file + ".json")


def draw_full_list_contact():
    data = model.get_data()
    draw_data(data)


def draw_data(data):
    for item in range(len(data)):
        print(f'{item}. {data[item]["fio"]} -> {data[item]["phone"]}')


def add_person():
    print('Добавление контакта')
    fio, phone = input_person_data()
    if check_input_person_data(fio, phone):
        model.add_person(fio, phone)
        return True
    else:
        print("Ошибка")
        return False


def set_person_by_id():
    print('Изменение контакта')
    print('Введите номер контакта для изменения')
    id_person = int(input())
    fio, phone = input_person_data()
    if check_input_person_data(fio, phone) and 0 <= id_person < len(model.data):
        model.set_person_by_id(id_person, fio, phone)
        return True
    else:
        print("Ошибка")
        return False


def del_person_by_id():
    print('Удаление контакта')
    print('Введите номер контакта для удаления')
    id_person = int(input())
    if 0 <= id_person < len(model.data):
        model.del_person_by_id(id_person)
        return True
    else:
        print("Ошибка")
        return False


def check_input_person_data(fio, phone):
    result = True
    return result


def input_person_data():
    print('Введите имя')
    fio = input()
    print('Введите номер телефона')
    phone = input()
    return fio, phone


def find_persons_by_name():
    print('Введите поисковую строку')
    fio = input()
    data = model.find_persons_by_name(fio)
    draw_data(data)
