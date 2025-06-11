from scapy.all import *
from func import scan_port
import argparse
import concurrent.futures

open_ports = []  # jetzt Liste statt Zähler

# ich will das alles nicht
parse = argparse.ArgumentParser()
parse.add_argument("host", help="Target IP or Domain")
parse.add_argument("-p", "--ports", help="Port range (e.g., 1-100)", default="1-1024")
args = parse.parse_args()
target = args.host
start_port, end_port = map(int, args.ports.split('-'))  # poa keine ahnung was dat macht–

print(f"Scanning {target} from port {start_port} to {end_port}")  # printet halt irgendwas mit ports

# ich habe massive schmerzen
def scan_and_collect(port):
    status = scan_port(target, port)
    if status == "Open":  # jup das macht bestimmt die wäsche XD LOL ICH LIEBE MEIN LEBEN "nicht"
        print(f"[+] Port {port}: {status}")
        open_ports.append(port)

# multithreading baby
with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_and_collect, range(start_port, end_port + 1))

# Ergebnisse
print(f"\nOpen ports found: {len(open_ports)}")
print(f"Ports: {open_ports}")
