import os

def recon (ip):
    os.system(f"nmap -A -p- PN {ip} -v")
    os.system(f"dirb {ip}")

recon (input("What IP address would yo like to scan and do simplest recon ever?"))