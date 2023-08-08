from time import sleep
import sys

tab = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = 0 

while a < len(tab):
    print(tab[a], end="", flush=True)
    sleep(1)
    a = a + 1