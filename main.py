from scapy.all import *
from func import scan_port
import argparse

open_ports = 0

# ich will das alles nicht
parse = argparse.ArgumentParser()
parse.add_argument("host", help="Target IP or Domain")
parse.add_argument("-p", "--ports", help="Port range (e.g., 1-100)", default="1-1024")
args = parse.parse_args()
target = args.host
start_port, end_port = map(int, args.ports.split('-')) # poa keine ahnung was dat macht 
print(f"Scanning {target} from port {start_port} to {end_port}") # printet halt ihrgendwas mit ports
for port in range(start_port,end_port): # jup das macht bestimmt die wäsche XD LOL ICH LIEBE MEIN LEBEN "nicht"
    status = scan_port(target,port)
    if status == "Open":
        print(f"[+] Port {port}: {status}")
        open_ports + 1
# ich habe massive schmerzen
print(f"Open ports found: {open_ports}")
