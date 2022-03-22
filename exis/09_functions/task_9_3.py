# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""



def get_int_vlan_map(path):
    text = path
    dictacces = {}
    dicttrunk = {}
    with open(text, 'r') as file:
        for line in file:
            if line.find("FastEthernet") !=-1:
                inter = line.split()[-1]
            elif  line.find("switchport access vlan")!=-1:
                dictacces[inter]=line.split()[-1]
            elif line.find("switchport trunk allowed vlan") != -1:
                dicttrunk[inter]=line.split()[-1]
        
        z = (dictacces, ) + (dicttrunk, )
        return z
         

print(get_int_vlan_map("09_functions\config_sw1.txt"))  
                
                