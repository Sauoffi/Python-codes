ip_address = input("Enter IP address: ")


octets = ip_address.split(".")

octet1 = int(octets[0])
octet2 = int(octets[1])
octet3 = int(octets[2])
octet4 = int(octets[3])


if octet1 >= 1 and octet1 <= 127:
    print("Class A")
elif octet1 >= 128 and octet1 <= 191:
    print("Class B")
elif octet1 >= 192 and octet1 <= 223:
    print("Class C")
elif octet1 >= 224 and octet1 <= 239:
    print("Class D")
elif octet1 >= 240 and octet1 <= 255:
    print("Class E")
else:
    print("Invalid IP address")
