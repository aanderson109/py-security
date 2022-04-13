"""
script to pull information from the windows registry about wireless connections
"""
from winreg import *
from termcolor import colored
import pyfiglet
import argparse

def convert_bin2mac(address_as_bin):
    """
    OVERVIEW
    ---------
    winreg stores gateway mac addresses as binary;
    this method converts the binary to its mac address
    """
    address_as_mac = ""
    for ch in address_as_bin:
        address_as_mac += ("%02x "% ord(ch))
    address_as_mac = address_as_mac.strip(" ").replace(" ",":")[0:17]
    return address_as_mac

# method to extract the network name and mac address for every listed network profile from the keys in winreg
# use _winreg library for this
# after connecting to the registry, use OpenKey() and loop through network profiles
# for each profile we pull the profileguid, description, source, dnssuffix, firstnetwork, defaultgatewaymac
def reg_digger():
    net_path = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = OpenKey(HKEY_LOCAL_MACHINE, net_path)
    print(colored("\n[*] networks you have joined","magenta"))
    for i in range(100):
        try:
            guid = EnumKey(key, i)
            net_key = OpenKey(key, str(guid))
            (n, address_as_bin, t) = EnumValue(net_key, 5)
            (n, network_name, t) = EnumValue(net_key, 4)
            mac_address = convert_bin2mac(address_as_bin)
            str_network_name = str(network_name)
            print("[+] " + colored(str_network_name,"yellow") + " " + colored(mac_address,"green"))
            CloseKey(net_key)
        except:
            break
def main():
    title_banner = pyfiglet.figlet_format("WinReg\n digger", font="slant")
    print(colored(title_banner, "cyan"))
    print(colored("="*50, "cyan"))

    # instead of using optparse, we'll use argparse
    parser = argparse.ArgumentParser(prog="wap-register-digger.py",
                                    prefix_chars="-",
                                    usage="%(prog)s",
                                    description="WinReg Digger")

    # action flag for printing the version then exiting
    parser.add_argument('-version',
                        action='version',
                        version='%(prog)s version 1.0')
    
    reg_digger()

    ending_banner = pyfiglet.figlet_format("goodbye!", font="big")
    print("\n" + colored('='*50, "cyan"))
    print(colored(ending_banner, "cyan"))

if __name__ == '__main__':
    main()