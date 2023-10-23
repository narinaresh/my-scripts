import optparse
import subprocess
import time

arguments = optparse.OptionParser()

arguments.add_option("-i", "--interface", dest='interface',
                     help="type of interface [example:eth0,wlan0..]")
arguments.add_option("-t", "--time", dest="time_of_delay",
                     help="the time delay between IP changes [in seconds] ")

option = arguments.parse_args()

interface = input("interface > ")

time_of_delay = int(
    input("Enter the time delay between IP changes (in seconds) > "))

print(" ")
print("---------------------------------------------------------")
print("[+] Starting up")
print("[+] Changing your ip address of", interface , " in every " + str(time_of_delay) + " sec" )
print("---------------------------------------------------------")
print(" ")
last_digit = 0
third_digit = 100

while True:

    ipaddr = f"192.168.{third_digit}.{last_digit}"
    cmd = (["ifconfig", interface, "inet", ipaddr])
    subprocess.call(cmd)

    time.sleep(time_of_delay)
    last_digit += 1
    third_digit += 1

    if third_digit > 255:
        third_digit = 100

    if last_digit > 255:
        last_digit = 0
