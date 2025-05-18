from scapy.all import sniff, get_if_list

print("Available interfaces:", get_if_list())  # Show available interfaces

def packet_callback(packet):
    print(packet.summary())

print("Starting sniffing...")

try:
    sniff(prn=packet_callback, store=False)
except Exception as e:
    print(f"Error during sniffing: {e}")
