# задание с отрезками
# если просят найти минимум
p = [i / 10 for i in range(120 , 300 + 1)]
q = [i / 10 for i in range(250 , 350 + 1)]

a = set()
b = [i / 10 for i in range(0,1000)]

for x in b:
    if not(((x not in a) <= (x not in p)) or (x in q)):
        a.add(x)
print(sorted(a))



# если просят найти максимум
p = [i / 10 for i in range(100 , 230 + 1)]
q = [i / 10 for i in range(390 , 550 + 1)]

a = set([i / 10 for i in range(0,1000)])
b = [i / 10 for i in range(0,1000)]

for x in b:
    if not(   ((x not in p) and (x in a)) <= (x in q) and (x in a)      ):
        a.remove(x)

print(sorted(a))



# тип здадания с неравенствами
for a in range(1,1000):
    a_nigger = True
    for x in range(0,1000):
        for y in range(0,1000):
            if ((x + y <= 22) or (y <= x - 6) or (y >= a)) == False:
                a_nigger = False
                break
        
        if a_nigger == False:
            break
    
    if a_nigger == True:
        print(a)



# тип задания на коньюнкцию
for a in range(0,1000):
    a_nigger = True
    for x in range(0,1000):
        if not(((x & 42 != 0) and (x & 34 == 0)) <= (not(x & a == 0))):
            a_nigger = False
            break
    if a_nigger == True:
        print(a)
        break

# тип задания на делители 
def main(m,n):
    if m % n == 0:
        return True
    else:
        return False
    
for a in range(1,1000):
    a_nigger = True
    for x in range(1,1000):
        if not((main(x,45) and (not(main(x,15)))) <= (not(main(x,a)))) == False:
            a_nigger = False
            break
    
    if a_nigger == True:
        print(a)


# смешанный тип с лелителясми и неравенством
for a in range(1,1000):
    a_nigger = 0
    for x in range(0,1000):
        if (((x % 6 == 0) <= (x % 10 != 0)) or (x + a > 121)):
            a_nigger +=1
            
    if a_nigger == 999:
        print(a)


# смешанный тип с отрезками и делителями
def check(A):
    for x in range(1, 1000):
        f = (x % A == 0) or ((50 <= x <= 70) <= (x % 21 != 0))
        if f != 1:
            return 0
    return 1


for A in range(1, 1000):
    if check(A):
        print(A)