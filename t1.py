import getpass
import telnetlib
HOST = "localhost"
user = input("Entrer nom d'utilisateur telnet: ")
password = getpass.getpass()

f = open('liste_IPs.txt')
H = open('hostname.txt')

for IP in f:
    IP=IP.strip()
    print("##### configuration de switch " + (IP) + " #####")
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"configure terminal\n")
    for n in range(20, 55):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name DEPAR" + str(n).encode('ascii') + b"\n")

    tn.write(b"exit\n")
    tn.write(b"banner motd c\n")
    tn.write(b"######  ####### #     #       # ####### #     # ######\n")
    tn.write(b"#     # #     # ##    #       # #     # #     # #     #\n")
    tn.write(b"#     # #     # # #   #       # #     # #     # #     #\n")
    tn.write(b"######  #     # #  #  #       # #     # #     # ######\n")
    tn.write(b"#     # #     # #   # # #     # #     # #     # #   #\n")
    tn.write(b"#     # #     # #    ## #     # #     # #     # #    #\n")
    tn.write(b"######  ####### #     #  #####  #######  #####  #     #\n")
    tn.write(b"c\n")

    tn.write(b"banner exec c\n")
    tn.write(b"####### ######    ###    #####    ###    #####\n")
    tn.write(b"   #    #     #    #    #     #  #   #  #     #\n")
    tn.write(b"   #    #     #    #          # # #   #       #\n")
    tn.write(b"   #    ######     #     #####  #  #  #  #####\n")
    tn.write(b"   #    #   #      #    #       #   # # #\n")
    tn.write(b"   #    #    #     #    #        #   #  #\n")
    tn.write(b"   #    #     #   ###   #######   ###   #######\n")
    tn.write(b"c\n")
    tn.write(b"username hatim password cisco\n")
    tn.write(b"line vty 0 15\n")
    tn.write(b"transport input all\n")
    tn.write(b"login local\n")
    tn.write(b"exit\n")
    tn.write(b"ip domain-name tri202.ma\n")
    tn.write(b"crypto key generate rsa modulus 1024\n")
    tn.write(b"ip ssh version 2\n")
    tn.write(b"service password-encryption\n")
    tn.write(b"end\n")
    tn.write(b"write\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))