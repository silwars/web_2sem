# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""





ip = input("Введите IP: ")
ipaddress = ip.split(".")

   
   
if len(ipaddress)==4:
   for i in range(0,len(ipaddress)):
      if ipaddress[i].isdigit() and 0<=int(ipaddress[i])<=255:
         pass
      else:
         print("Неправильный IP")
         raise SystemExit
else:
   print("Неправильный IP")
   raise SystemExit


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