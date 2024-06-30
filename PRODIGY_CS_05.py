print("🔒 Network Packet Analyzer 🔒")
from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source: {ip_layer.src}")
        print(f"Destination: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        print(f"Payload: {bytes(packet)}\n")

def start_sniffing(interface):
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff on: ")
    start_sniffing(interface)


