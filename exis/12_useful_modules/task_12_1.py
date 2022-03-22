# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
list_of_av=[]
list_of_unav=[]
list_of_ip=["a", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
def ping_ip_addresses(ip_addres):

    for ip in ip_addres:
        reply = subprocess.run(['ping', ip],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if reply.returncode == 0:
            list_of_av.append(ip)
        else:
            list_of_unav.append(ip)
    return (list_of_av, )+(list_of_unav, )


print(ping_ip_addresses(list_of_ip))
