# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
list = []
vlanlist = []
vlan = input("Enter VLAN number: ")
with open('07_files\CAM_table.txt', 'r') as start:
    for line in start:
        if line.count('.') is 2:
            a = line.strip('\n').split()
            b = a.pop(-2)
            list.append(a)
            if a[0]==vlan:
                print(f"{a[0]:<8}{a[1]:<18}{a[2]:<8}")
