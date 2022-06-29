# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input("Введите ip: ")
temp = ip.split("/")
ipactet = temp[0].split(".")
adhost = f"{int(ipactet[0]):08b}{int(ipactet[1]):08b}{int(ipactet[2]):08b}{int(ipactet[3]):08b}"
adnet = adhost[0:int(temp[1])]+"0"*int(32-int(temp[1]))
mask = "1"*int(temp[1])+"0"*int(32-int(temp[1]))
print(f'''
Nemwork:
{int(adnet[0:8],2):<8}  {int(adnet[8:16],2):<8}  {int(adnet[16:24],2):<8}  {int(adnet[24:32],2):<8}
{adnet[0:8]:8}  {adnet[8:16]:8}  {adnet[16:24]:8}  {adnet[24:32]:8}

Mask:
/{temp[1]}
{int(mask[0:8],2):<8}  {int(mask[8:16],2):<8}  {int(mask[16:24],2):<8}  {int(mask[24:32],2):<8}
{mask[0:8]:8}  {mask[8:16]:8}  {mask[16:24]:8}  {mask[24:32]:8}
''')