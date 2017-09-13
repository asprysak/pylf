"""
A simple script producing some output in a loop
"""

from time import sleep
import sys

for i in range(10):
    print("TEST LOG!")
    print("-=> TEST LOG!")
    print("TEST ERRLOG!", file=sys.stderr)
    sleep(0.5)
