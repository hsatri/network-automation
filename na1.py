import getpass
import telnetlib
HOST = "localhost"
user = input("Entrer nom d'utilisateur telnet: ")
password = getpass.getpass()

f = open('liste_IPs.txt')

for IP in f:
    IP=IP.strip()
    print("configuration de switch " + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    if password:
        tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
 #   tn.write(b"cisco\n")
    tn.write(b"configure terminal\n")
    for n in range(2, 15):
        tn.write(b"vlan" + str(n).encode('ascii') + b"\n")
        tn.write(b"name python-vlan-" + str(n).encode('ascii') + b"\n")
    print(tn.read_all().decode('ascii'))
