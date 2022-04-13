"""
script to look for servers w/ ftp on and anonymous login enabled
"""
import argparse
import ftplib
import pyfiglet
from termcolor import colored

def attempt_anon(target_host):
    """
    ARGUMENTS
    -----------
    target_host => ip address of server to attempt anon ftp login

    BEHAVIOR
    -----------
    takes the ip address of the target and attempts to login
    returns a boolean condition:
        ==> True indicates login was successful
        ==> False indicates login was unsuccessful
    """
    try:
        ftp = ftplib.FTP(target_host)
        ftp.login('anonymous','me@your.com')
        print('\n[*] ' + str(target_host) + colored(' ftp anon login success',"green"))
        ftp.quit()
        return True
    except:
        print('\n[-] ' + colored(str(target_host),"yellow") + colored(' ftp anon login failed',"red"))
        return False

def main():
    title_banner = pyfiglet.figlet_format("anonymous\n ftp finder", font="slant")
    print(colored(title_banner, "cyan"))
    print(colored("="*50, "cyan"))

    parser = argparse.ArgumentParser(prog="anon ftp finder",
                                    prefix_chars='-',
                                    usage="%(prog)s -host <target host>",
                                    description="script to find servers w/ anon ftp and attempt a log in")
    parser.add_argument('-version',
                        action="version",
                        version="%(prog)s version 1.0")

    parser.add_argument('-host',
                        required=True,
                        help="target host ip address",
                        dest="target_host")
    flags = parser.parse_args()
    target_host = flags.target_host
    attempt_anon(target_host)

    ending_banner = pyfiglet.figlet_format("goodbye!", font="big")
    print("\n" + colored('='*50, "cyan"))
    print(colored(ending_banner, "cyan"))

if __name__ == '__main__':
    main()