# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
x = 0
while x == 0:
    ip = input("Введите IP: ")
    ipaddress = ip.split(".")



    for i in range(0,len(ipaddress)):
        if ipaddress[i].isdigit() and 0<=int(ipaddress[i])<=255 and len(ipaddress)==4:
            x+=1
        else:
            print("Неправильный IP")
            x = 0

if 0<int(ipaddress[0])<224:
    print("unicast")
elif 223<int(ipaddress[0])<240:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")