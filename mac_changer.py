import argparse
import subprocess
import time

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--interface", dest='interface',
                    help="Type of interface [example: eth0, wlan0...]")
parser.add_argument("-m", "--mac", dest="mac",
                    help="The MAC address you want to change")
parser.add_argument("-t", "--time", dest="time_of_delay",
                    help="The time delay between MAC changes [in seconds]")

args = parser.parse_args()

if not args.interface:
    interface = input("Enter the interface > ")
else:
    interface = args.interface

first_digit = 0
second_digit = 0
third_digit = 0
fourth_digit = 0
fifth_digit = 0
last_digit = 0

if not args.mac:
    mac = f"{first_digit:02x}:{second_digit:02x}:{third_digit:02x}:{fourth_digit:02x}:{fifth_digit:02x}:{last_digit:02x}"
else:
    mac = args.mac

if not args.time_of_delay:
    time_of_delay = int(
        input("Enter the time delay between MAC changes (in seconds) > "))
else:
    time_of_delay = int(args.time_of_delay)

print(" ")
print("---------------------------------------------------------")
print("[+] Starting up")
print(
    f"[+] Changing the MAC address of {interface} every {time_of_delay} seconds")
print("---------------------------------------------------------")
print(" ")

while True:
    new_mac = f"{first_digit:02x}:{second_digit:02x}:{third_digit:02x}:{fourth_digit:02x}:{fifth_digit:02x}:{last_digit:02x}"
    cmd = ["ifconfig", interface, "hw", "ether", new_mac]
    subprocess.call(cmd)
    time.sleep(time_of_delay)

    last_digit = (last_digit + 1) % 256
    if last_digit == 0:
        fifth_digit = (fifth_digit + 1) % 256
        if fifth_digit == 0:
            fourth_digit = (fourth_digit + 1) % 256
            if fourth_digit == 0:
                third_digit = (third_digit + 1) % 256
                if third_digit == 0:
                    second_digit = (second_digit + 1) % 256
                    if second_digit == 0:
                        first_digit = (first_digit + 1) % 256
