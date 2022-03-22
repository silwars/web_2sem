# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate


q = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
z = ["10.10.2.1", "10.10.1.2"]


def print_ip_table(reach,unreach):
    q={"Reachable":[],"Unreachable":[]}
    for i in reach:
        q["Reachable"].append(i)
    for i in unreach:
        q["Unreachable"].append(i)
    print(tabulate(q,headers="keys"))

print_ip_table(q,z)