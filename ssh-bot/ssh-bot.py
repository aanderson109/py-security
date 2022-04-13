import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$']

def transmit(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)

def ssh_connect(user, host, password):
    ssh_newkey = 'are you sure you want to continue connecting'
    connect_string = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connect_string)
    ret = child.expect( [pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] error connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect( [pexpect.TIMEOUT, '[P|p]assword:'])
        if ret == 0:
            print('[-] error connecting')
            return
        child.sendline(password)
        child.expect(PROMPT)
        return child

def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'
    child = ssh_connect(user, host, password)
    transmit(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
    main()