#1)Создать переменную типа String
string = 'Denis'
print(type(string), string)
#2)Создать переменную типа Integer
integer = 8
print(type(integer), integer)
#3)Создать переменную типа Float
float = 5.5
print(type(float), float)
#4)Создать переменную типа Bytes
byt = bytes(255)
print(type(byt), byt)
#5)Создать переменную типа List
list = [string, float, integer]
print(type(list), list)
#6)Создать переменную типа Tuple
tuple = (8, 5.5, string)
print(type(tuple), tuple)
#7)Создать переменную типа Set
set = {8, string, 8}
print(type(set), set)
#8)Создать переменную типа Frozen set
frozen = frozenset({8, string, 5.5})
print(type(frozen), frozen)
#9)Создать переменную типа Dict
dict = {'value':31, 'key':8}
print(type(dict), dict)
#10)Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print((type(string), string), (type(integer), integer), (type(float), float), (type(byt), byt), (type(list), list), (type(tuple), tuple), (type(set), set), (type(frozen), frozen), (type(dict), dict)
#11)Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные.
str1 = "Learn, "
str2 = "Python!"
concat = str1+str2
print(concat)
#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(string, interger, sep = ',')
#13)Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(string + string(interger))

