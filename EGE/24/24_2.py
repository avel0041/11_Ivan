# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.

f = open('24_2.txt')
a = f.readline()
h = 1
h_max = 0
for i in range(0, len(a) - 1, 1):
    if (a[i] == 'K' and a[i+1] == 'L') or (a[i] == 'L' and a[i+1] == 'K'):
        h = 1
    else:
        h += 1
        if h > h_max: # или так h_max = max(h_max, h)  
            h_max=h
print(h_max)


a = a.replace('LK', 'L K') #только с двумя буквами 
a = a.replace('KL', 'K L')
a = a.split(' ')
s = max(a, key=len) #key=len макс по длине, а не по значению
print(len(s))
# ABCUGIFASBDASK LDBSOAIUHL KDSBAYD