"""
Algorithm in Turkish(I wrote it for how i create this program)
'ARP' ve 'Ether' modülleri import edilir.
Hedef IP adresi belirlenir
'ARP' nesnesi oluşturulur ve hedef IP adresi atanır
'Ether' nesnesi oluşturulur ve hedef mac adresi atanır
Ether ve arp nesneleri birleştirilir
Oluşan paket, 3 saniye timeout ile ve verbose modu kapalı olarak gönderilir
Gelen paketler taranır ve her gelen paket için IP ve MAC adresleri bir listeye eklenir
Liste ekrana yazdırılır: print(clients)
"""
from scapy.all import ARP, Ether, srp

target_ip = "192.1.1.1/24"
arp_packet = ARP(pdst = target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp_packet
result = srp(packet, timeout = 3,verbose=0)[0]
clients = []
i = 0
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    print(clients[i])
    i += 1


