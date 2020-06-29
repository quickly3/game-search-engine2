import telnetlib
import sys
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def test_ip(ip,port):
    try:
        resp = telnetlib.Telnet(ip,port,timeout=2)
        print("代理ip有效！")
    except:
        print("代理ip无效！")


ip = sys.argv[1]
port = sys.argv[2]

ping(ip)
test_ip(ip,port)