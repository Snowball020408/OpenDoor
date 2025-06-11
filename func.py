from scapy.all import *

def scan_port(target,port):
    # sends 1 syn package to destination ip and port and waits for response
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    response = sr1(pkt, timeout=1.5, verbose=0)
    if response is None:
        return "Filtered or no response"
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12: # SYN-ACK
            # Send RST to close connection
            rst_pkt = IP(dst=target)/TCP(dport=port, flags="R") # warum tue ich mir das überhaupt an 
            send(rst_pkt, verbose=0) # sendet halt nen reset package and den port damit er byebye sagen kann
            return "Open" # jup ist offen also hack den lachs
        elif response.getlayer(TCP).flags == 0x14:
            return "Closed" # ja ist halt dicht lol
    return "Unkown" # ich weis ehrlich gesagt nicht einmal selber wann das returnt weil ein port immer closed oder open ist aber das muss so sonst error
