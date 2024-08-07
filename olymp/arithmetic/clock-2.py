# Задача №2948. Электронные часы - 2

# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов, потом обязательно
# двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при
# необходимости дополняются до двузначного числа нулями.
#
# С начала суток прошло n секунд. Выведите, что покажут часы.
#
# Входные данные
# Вводится целое число n.
#
# Выходные данные
# Выведите ответ на задачу, соблюдая требуемый формат.
#
# Примеры
# входные данные
# 3602
# выходные данные
# 1:00:02
# входные данные
# 129700
# выходные данные
# 12:01:40

n = int(input('Enter the amount of seconds: '))

# сколько часов
total_h = n // 3600 % 24
# оставшиеся секунды
rem_sec = n % 3600

# из оставшихся секунд получаем минуты
total_mm = rem_sec // 60
# преобразуем минуты в строку
total_mm_str = str(total_mm)
if total_mm < 10:
    total_mm_str = '0' + total_mm_str

# из оставшихся секунд получаем секунды
total_ss = rem_sec % 60
# преобразуем секунды в строку
total_ss_str = str(total_ss)
if total_ss < 10:
    total_ss_str = '0' + total_ss_str

print(total_h, ':', total_mm_str, ':', total_ss_str)