
# CREATE
a = 'привет' # Одинарные кавычки
b = "привет" # Двойные кавычки
с = "я'знаю'Python" #Комбинированные кавычки
d = 'я"знаю"Python' # Можно и так
e = 'я"знаю'Python"  # А так нельзя( кавычки вперемешку)
a = 123 # Целочисленный тип
a = str(a) # Результат '123'
str([1, 1.1, 'a']) #Результат "[1, 1.1, 'a']"
str(True) # Рузультат 'True'
str(None) # Результат 'None'
a = 'привет'
b = 'Иван'
c = f"{a} я {b}" # "привет я Иван"
#RETRIVE(READ)
a = 'привет'
print(a)
print('Иван')
a = 'привет'
a = [0] # 'п'
a = [1] # 'р'
a = [2] # 'и'
a = [3] # 'в'
a = [4] # 'е'
a = [5] # 'т'
a = [6] # Ошибка, вышли за границы
a = [-1] # 'т'
a = [-2] # 'е'
a = [-3] # 'в'
a = [-4] # 'и'
a = [-5] # 'р'
a = [-6] # 'п'
a = [- 7] # Ошибка, вышли за границы
# UPDATE
a = 'привет'
a[0] ='б' # Хотели получить 'бривет', а получили ошибку, что строку нельзя изменять
a = 'бривет' # Для изменения придется полностью присвоить новое значение
# DELETE
