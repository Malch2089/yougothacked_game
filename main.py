from colorama import *; init(); print(Fore.GREEN, end="")
from chatbot import hacker_chat_bot
from tasks import task1
from tasks import task2
from tasks import task3
from tasks import finale
import time
import os
import random
from chatbot import slow_print

print("Windows PowerShell\nCopyright (C) Microsoft Corporation.\n")
print("PS C://Users//ADMIN>")

slow_print("...")
time.sleep(1)
slow_print("System Compromsied")
time.sleep(2)

slow_print("Hacker: Hey.")
slow_print("Hacker: Relax, if I want to damage you I would have done it")
slow_print("Hacker: I have deal for you")
slow_print("Hacker: I will give you a few puzzles if you would be able to solve them you will get your system back")
slow_print("Hacker: So will you do them or just I do my thing\n")

while True:
    terminal_effect = ("PS C://Users//ADMIN>")
    cmd = input(terminal_effect).lower()

    if cmd in ["yes", "y", "ok", "okay", "sure", "fine", "start","please stop", "okay okay", "fine don't hurt", "i'll do it", "just stop", "okay i agree","what is this", "idk but okay", "i guess", "whatever", "just tell me what to do","fine do it", "this is stupid but ok", "just start", "whatever man", "hurry up","do"]:
        if task1() and task2() and task3():
            finale()
        else:
            slow_print("\nHacker: You almost had it.")
        break

    elif cmd in ["ignore", "no"]:
        slow_print("Hacker: Ignoring me doesn't stop anything.")
        with open("warning.txt", "w") as f:
            f.write("still no ?")
        os.startfile("warning.txt")

    else:
        hacker_chat_bot(cmd)