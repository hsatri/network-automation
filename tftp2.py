#==============================================
#creatd by HATIM SATRI
#==============================================

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# entrez l'IP de votre serveur TFTP ici
SERV_TFTP = "43.15.24.2"

#la liste des adresses ip des péripheriques
IP_LIST = open('6_devices')
i = 0
# pour ajouter un périphérique, définissez ses détails de connexion ci-dessous, puis ajoutez son nom
for IP in IP_LIST:
    print ('\n  '+ IP.strip() + ' \n' )
    ROUTEURS = {
    'ip':   IP,
    'username': 'hatim',
    'password': 'cisco',
    'secret': 'cisco',
    'device_type': 'cisco_ios',
    }

    try:
        net_connect = ConnectHandler(**ROUTEURS)
    except NetMikoTimeoutException:
        print ('Device not reachable.')
        continue
    except AuthenticationException:
        print ('Authentication Failure.')
        continue
    except SSHException:
        print ('Make sure SSH is enabled in device.')
        continue
    i += 1
    name = f"R{str(i)}"
    net_connect.enable()
    copy_command = f"copy start tftp://{SERV_TFTP}/{name}.conf"
    output = net_connect.send_command_timing(copy_command)
    if "Address or name" in output:
        output += net_connect.send_command_timing("\n")
    if "Destination filename" in output:
        output += net_connect.send_command_timing("\n")
    print(output)
    net_connect.exit_enable_mode()