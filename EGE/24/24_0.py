# Текстовый файл состоит не более чем из 10^6 символов A, B и C. 
# Определите максимальное количество идущих подряд символов C.

f = open('24_0.txt')
l = f.readline()
c = 1 # с 1 из за 'ACACACACACA'
c1 = 0
for i in range(0, len(l) - 1, 1):
    if l[i] == 'C':
        if l[i] == l[i + 1]:
            c += 1
            if c > c1:
                c1 = c
    else:
        c = 1
print(c1)





    
