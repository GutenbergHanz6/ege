from ipaddress import *
# задача с нахождением количества нулей  в сети
net = ip_network('123.80.87.27/255.255.240.0' , strict=0)

adress = f'{net.network_address:b}'
print(adress.count('0'))

# задача с количеством компов в сети

net = ip_network(address='123.87.81.24/255.255.252.0' , strict=0)
mun = net.num_addresses
print(mun - 2)

# номер коомпа в сети
ip = ip_address('123.87.81.24')
net = ip_network(address='123.87.81.24/255.255.240.0' , strict=0)
address = net.network_address
num = int(f'{ip:b}', 2) - int(f'{address:b}' , 2)
print(num)


# если надо кол-во адресов для которых сумма единиц в двоичной записи четна
net = ip_network(f'192.186.32.160/255.255.255.240' , 0)
for ip in net :
    if f'{ip:b}'.count('1') % 2 == 0:
        print(ip)


# # сколько существует масок сетей для которых сумма единиц в двоичной записи нечетна
k = 0
for mask in range(32):
    if mask % 2:
        k +=1
print(k)

# тип со  x + y
for x in range(256):
    for y in range(256):
        try:
            net = ip_network(address=f'85.169.154.54/255.{x}.{y}.0' , strict=0)
            address = str(net.network_address)
            s = sum(map(int,address.split('.')[:3]))
            if s == 408:
                print(x + y)
        except:
            ...

# сколько сушествует ip адресов в которых сумма единици является полным квадратом
count = 0
net = ip_network('49.154.109.10/255.255.128.0', 0)
for ip in net.hosts():
    if f'{ip:b}'.count('1') in (1,4,9,16,25):
        count +=1 
print(count)

# сколько существует значений 3 байта маски если в сети не менее 500 узлов
for mask in range(32):
    net = ip_network(f'125.28.160.73/{mask}' , 0)
    address = net.network_address
    if str(address) == '125.28.160.0' and len(list(net.hosts())) >= 500:
        print(mask)

