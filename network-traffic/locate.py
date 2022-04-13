"""
approximate location of ip
"""
import pygeoip
import pyfiglet
from termcolor import colored
import argparse

data = pygeoip.GeoIP('path/to/file')

def locate(target):
    target_profile = data.record_by_name(target)
    target_city = target_profile['city']
    target_region = target_profile['region_name']
    target_country = target_profile['country_name']
    target_longitude = target_profile['longitude']
    target_latitude = target_profile['latitude']
    print("[*] Target: " + target + "location data")
    print("==> " + str(target_city) + ", " + str(target_region) + ", " + str(target_country))
    print("==> latitude | longitude: " + str(target_latitude) + " | " + str(target_longitude))

def main():
    title_banner = pyfiglet.figlet_format("location\n finder", font="slant")
    print(colored(title_banner, "cyan"))
    print(colored("="*50, "cyan"))

    # instead of using optparse, we'll use argparse
    parser = argparse.ArgumentParser(prog="locate.py",
                                    prefix_chars="-",
                                    usage="%(prog)s -target <target ip>",
                                    description="location finder")

    # action flag for printing the version then exiting
    parser.add_argument('-version',
                        action='version',
                        version='%(prog)s version 1.0')

    # argument for target hostname or IP address
    parser.add_argument('-target',
                        required=True,
                        help="target ip address",
                        dest="target")
    flags = argparse.parse_args()
    target = flags.target

    locate(target)
    
    ending_banner = pyfiglet.figlet_format("see ya later!", font="big")
    print("\n" + colored('='*50, "cyan"))
    print(colored(ending_banner, "cyan"))

if __name__ == '__main__':
    main()