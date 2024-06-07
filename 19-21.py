# типы с 2 кучами
# задание 19
def main(x,y,p):
    if x + y >= 99 or p >3:
        return x +y >= 99 and p == 3 
    
    return main(x+1,y,p+1) or main(x , y + 1 , p +1) or \
    main(x * 3 ,y , p +1) or main(x , y * 3 , p + 1)

for s in range(1,90 + 1):
    if main(8 , s , 1):
        print(s)
        break

# задание 20

def main(x,y,p):
    if x+y>= 77 or p > 4:
        return x + y >= 77 and p == 4
    
    if p % 2 == 1:
        return main(x + 1 , y , p + 1) or main(x * 2 , y , p +1 ) or \
        main(x, y + 1 , p + 1) or main(x , y * 2 , p + 1)

    else:
        return main(x + 1 , y , p + 1) and main(x * 2 , y , p + 1) and \
        main(x , y + 1 , p + 1) and main(x , y * 2 , p + 1)
    
for s in range (1 , 69 + 1):
    if main(7 , s , 1):
        print(s)

# задание 21
print('полное решение при п == 3 или п == 5')
def main(x,y,p):
    if x + y >= 77 or p > 5:
        return x + y >= 77 and (p == 3 or p == 5)
    
    if  p % 2 == 0:
        return main(x + 1, y , p + 1) or main(x * 2 , y , p + 1) or \
        main(x , y + 1 , p + 1) or main(x , y * 2 , p + 1 )
    
    else:
        return main(x + 1 , y , p + 1) and main(x * 2 , y , p + 1) and \
        main(x , y + 1 , p + 1) and main(x , y * 2 , p + 1)

for s in range(1 , 69 + 1):
    if main(7 , s , 1):
        print(s)

print('иксл')
def main(x,y,p):
    if x + y >= 77 or p > 3:
        return x + y >= 77 and p == 3
    
    if p % 2 == 0:
        return main(x + 1 , y , p + 1) or main(x * 2 , y , p + 1) or \
        main(x , y + 1 , p + 1) or main(x , y * 2 , p + 1)
    else:
        return main(x + 1 , y,p +1 ) and main(x * 2 , y, p + 1) and \
        main(x , y + 1, p + 1) and main(x , y * 2 , p +1)
    
for s in range(1 , 69 + 1):
    if main(7 , s , 1):
        print(s)

# 1 куча
