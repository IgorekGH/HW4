# Задача 2
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 - N кустов
# 1 2 3 4 - ягод на каждом кусте
# 9 - x максимальное количество ягод с 3х кустов


n = int(input('Введите количество кустов: '))
a = list(map(int, input('Введите количество ягод на каждом кусте: ').split()))
x = 0
for i in range (1,n-1):
    if (a[i]+a[i+1]+a[i-1] > x):
        x = a[i]+a[i+1]+a[i-1]
print(x)