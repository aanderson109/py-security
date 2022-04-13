import nmap
import argparse
import pyfiglet
from termcolor import colored

def nmap_scan(target_host, scan_port):
    nmap_scanner = nmap.PortScanner()
    nmap_scanner.scan(target_host, scan_port)
    state = nmap_scanner[target_host]['tcp'][int(scan_port)]['state']
    print(colored(" [*] ","green") + colored(target_host, "yellow") + colored(" tcp/" + scan_port,"blue") + " " + state)

def main():
    title_banner = pyfiglet.figlet_format("nmap port scanner", font="slant")
    print(colored(title_banner, "cyan"))
    print(colored("="*50, "cyan"))

    parser = argparse.ArgumentParser(prog="nmap+python port scanner",
                                    prefix_chars="-",
                                    usage="%(prog)s -host <target host> -ports <target ports>",
                                    description="using nmap with python to scan ports")
    
    # the version action
    parser.add_argument('-version',
                        action='version',
                        version="%(prog)s version 1.0")
    
    # add host argument
    parser.add_argument('-host',
                        required=True,
                        help="IP or DNS of target",
                        dest="target_host")
    
    # add ports argument
    parser.add_argument('-ports',
                        help="list of ports on host to scan",
                        dest="target_ports")

    # pull user input from the command line
    flags = parser.parse_args()
    target_host = flags.target_host
    target_ports = flags.target_ports.split(',')

    for scan_port in target_ports:
        nmap_scan(target_host, scan_port)
    
    ending_banner = pyfiglet.figlet_format("goodbye!", font="big")
    print("\n" + colored('='*50, "cyan"))
    print(colored(ending_banner, "cyan"))

if __name__ == '__main__':
    main()

