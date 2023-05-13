import os
import argparse
import time
import sys

# p = subprocess.Popen(
#         "start /wait cmd /k",
#         shell=1,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.STDOUT
#     )

# p.communicate()

parser = argparse.ArgumentParser(description="Activating BIOS with restart", prog="BIOS ACTIV")

parser.add_argument("-t","--time", help="Integer number of seconds to restart the computer and run BIOS", type=int, default=2 ,required=False)

args = parser.parse_args()
print("This script will restart the computer in {} seconds and open BIOS.".format(args.time))
decision = input("Are you sure?(Y/N)     ")

if decision == "Y" or decision.lower()=="y":
    os.system("cls")
    for x in range(args.time,0,-1):
        print(x,end="\n")
        time.sleep(1)
    os.system("shutdown /r /fw /f /t 0")
else:
    os.system("cls")


