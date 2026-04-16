import scapy.all as scapy

def escanear_red(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    dispositivos_en_red = []
    for elemento in answered_list:
        dispositivo = {"ip": elemento[1].psrc, "mac": elemento[1].hwsrc}
        dispositivos_en_red.append(dispositivo)
    return dispositivos_en_red

def mostrar_resultados(resultados):
    print("IP\t\t\tMAC Address")
    print("-----------------------------------------")
    for dispositivo in resultados:
        print(dispositivo["ip"] + "\t\t" + dispositivo["mac"])

def main():
    target_ip = input("Ingrese la dirección IP/máscara de red a escanear (ejemplo: 192.168.1.1/24): ")
    resultados = escanear_red(target_ip)
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()