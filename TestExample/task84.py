# Пользователь вводит курс доллара в рублях. Показать таблицу цен 1$, 2$, ..., 100$ в рублях,
# третьим столбцом добавить количество кг конфет, которые можно купить на данные суммы, если цена 1 кг
# конфет равна 20 руб. Пример: 1$ - 70 р - 3.5 кг и так далее (всего 100 строк).

swity = 250
baks = 1
coll = 100
step = 1
course = 70
summ_rub = 0
summ_swity = 0

for i in range(baks, coll + 1):
    print(i, end=" - ")
    summ_rub = baks * course
    print(summ_rub, end=" - ")
    summ_swity = summ_rub / swity
    print(summ_swity)
    baks = baks + 1










