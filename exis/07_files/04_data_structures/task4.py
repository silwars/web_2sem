# Task1
# nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
# nat = nat.replace('Fast', 'Gigabit')
# print(nat)


# Task2
# mac = "AAAA:BBBB:CCCC"
# mac = mac.replace(':', '.')
# print(mac)


# Task3
# config = "switchport trunk allowed vlan 1,3,10,20,30,100"
# commands = config.split()
# vlans = commands[-1].split(',')
# print(vlans)


# Task4
# vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
# result = set(vlans)
# result = sorted(result)
# print(result)



# Task5
# command1 = "switchport trunk allowed vlan 1,2,3,5,8"
# command2 = "switchport trunk allowed vlan 1,3,8,9"
# vlan1 = command1.split()
# vlan1 = vlan1[-1].split(',')
# vlans1 = set(vlan1)
# vlan2 = command2.split()
# vlan2 = vlan2[-1].split(',')
# vlans2 = set(vlan2)
# result = vlans1 & vlans2
# result = sorted(result)
# print(result)


# Task6
# ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
# word = ospf_route.split()
# print("{0:<20} {1:<20}".format('Prefix', word[0]))
# print("{0:<20} {1:<20}".format('AD/Metric', word[1].strip("[]")))
# print("{0:<20} {1:<20}".format('Next-Hop', word[3].strip(",")))
# print("{0:<20} {1:<20}".format('Last update', word[4].strip(",")))
# print("{0:<20} {1:<20}".format('Outbound Interface', word[5]))


# Task7
# mac = "AAAA:BBBB:CCCC"
# temp = mac.split(":")
# str = temp[0]+temp[1]+temp[2]
# result = bin(int(str,16)).strip("0b")
# print(result)


# Task8
ip = "192.168.3.1"
temp = ip.split(".")
print(f'''
{temp[0]:<8}  {temp[1]:<8}  {temp[2]:<8}  {temp[3]:<8}
{int(temp[0]):08b}  {int(temp[1]):08b}  {int(temp[2]):08b}  {int(temp[3]):08b}''')