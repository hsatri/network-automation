import requests

Paramètres de l'API RESTCONF #OpenDayLight.
odl_url = 'http://10.5.5.1:8181/restconf/operational/network-topology:network-topology'
odl_username = 'admin'
odl_password = 'admin'

# Récupère les informations de l'API.
response = requests.get(odl_url, auth=(odl_username, odl_password))

# Trouver des informations sur les noeuds dans le fichier JSON récupéré.
for nodes in response.json()['network-topology']['topology']:

    # Parcourir toutes les informations de noeud.
    node_info = nodes['node']

    # Recherchez les adresses MAC et IP dans les informations de noeud.
    for node in node_info:
        try:
            ip_address = node['host-tracker-service:addresses'][0]['ip']
            mac_address = node['host-tracker-service:addresses'][0]['mac']
            print('Found host with MAC address %s and IP address %s' % (mac_address, ip_address))
        except:
            pass