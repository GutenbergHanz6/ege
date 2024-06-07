from string import ascii_lowercase , ascii_uppercase

# если система счисление улетает в космос
for x in range(0,68):
    a = 1*68**4 + 2*68**3 + 3*68**2 + x*68**1 + 5*68**0
    b = 1*68**4 + x*68**3 + 2*68**2 + 3*68**1 + 3*68**0
    if (a+b) % 12 == 0:
        print((a+b) // 12)


a = 2 * 729**2014 + 2 * 243**2016 - 2 * 81**2018 + 2 * 27**2020 - 2 * 9**2022 - 2024
res=[]
base = 27
cnt = 0
while a > 0:
    res.append(a % base)
    a //=base


alp = '0123456789' + ascii_lowercase
base = 19
for x in alp:
    a1 = int('98' + x + '79641' , base)
    a2 = int('36' + x + '14' , base)
    a3 = int('73' + x + '4' ,base)
    if (a1+a2+a3) % 18 == 0:
        print((a1+a2+a3) //18)


# если в заданиях присудствут x И y 
alp = '0123456789' + ascii_lowercase + ascii_uppercase
base = 26 
for x in alp:
    y = '2'
    a1 = int('13' + y + x + '5' , base)
    a2 = int('24' + y + '13' , base)
    if (a1+a2) % 8 == 0:
        print((a1+a2) // 8)
