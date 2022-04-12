'''
TCP Port Scanner using the full three way handshake

Goal: Build a TCP port scanner that completes the SYN/ACK handshake (e.g., sends response
        after port sends an ACK response)

aanderson109
'''
#imports
import pyfiglet
import argparse
import socket
from termcolor import colored

def target_connect(target_host, scan_port):
    """
    ARGUMENTS
    ------------
    target hostname (target_host)
    scan port (scan_port)
        ==> scan_port is an element in target_ports[] since it's being iterated
        ==> scan_port is the port currently being scanned pulled from the list of targets

    BEHAVIOR
    ------------
    1.) tries to connect to target host + port
        1.a) if successful => prints message that port is open
        1.b) if unsuccessful => prints message that port is closed
    """
    try:
        scanning_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        scanning_connection.connect( (target_host, scan_port) )
        print(colored('[+] %d/tcp open'% scan_port, "green"))
        scanning_connection.close()
    except:
        print(colored('[-] %d/tcp closed'% scan_port, "red"))

def port_scan(target_host, target_ports):
    """
    ARGUMENTS
    ------------
    target hostname (target_host)
    target ports (target_ports)
        ==> target_ports is the list of ports from the user

    BEHAVIOR
    ------------
    1.) attempts to identify IP address associated with hostname using socket.getfqdn() method
    2.) prints the hostname (if resolved)
        2.a) prints IP address (if hostname couldn't be resolved)
    3.) iterates through ports trying to establish a connection using the target_connect() method
    """
    try:
       target_name = socket.getfqdn(target_host)
    except:
        print("[-] cannot resolve '%s': unknown host"% target_host)
        return
    try:
        target_ip = socket.gethostbyaddr(target_ip)
        print('\n[+] scan results for: ' + target_ip[0])
    except:
        print('\n[+] scan results for: ' + target_name)
 
    for scan_port in target_ports:
        print(colored('scanning port ', "cyan") + scan_port)
        target_connect(target_host, int(scan_port))

def main():

    title_banner = pyfiglet.figlet_format("TCP Port Scanner", font="slant")
    print(colored(title_banner, "cyan"))
    print(colored("="*50, "cyan"))

    # instead of using optparse, we'll use argparse
    parser = argparse.ArgumentParser(prog="full-connect-scan.py",
                                    prefix_chars="-",
                                    usage="%(prog)s -host <target ip> -p, -ports <target ports>",
                                    description="TCP Port Scanner",
                                    epilog="Version 1.0 // Work In-Progress")

    # action flag for printing the version then exiting
    parser.add_argument('-version',
                        action='version',
                        version='%(prog)s [TCP Port Scanner] version 1.0')

    # argument for target hostname or IP address
    parser.add_argument('-host',
                        required=True,
                        help="host IP or DNS of target",
                        dest="target_host")

    # argument for ports you want to scan on the target
    parser.add_argument('-p',
                        '-ports',
                        default=list(range(10000+1)),
                        help="ports you want scanned on the target, separte with a comma (i.e., 22,23,24,25)",
                        dest="target_ports")

    # bring in the parser
    flags = parser.parse_args()
    target_host = flags.target_host
    target_ports = flags.target_ports.split(',')

    port_scan(target_host, target_ports)
    
    ending_banner = pyfiglet.figlet_format("GOODBYE!", font="big")
    print("\n" + colored('='*50, "cyan"))
    print(colored(ending_banner, "cyan"))

if __name__ == '__main__':
    main()
