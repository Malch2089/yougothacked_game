from colorama import *; init(); print(Fore.GREEN, end="")
import time
import random
import os
from chatbot import slow_print

def task1():
    slow_print("\n[PHASE 1: ACCESS CHECK]\n")

    code = str(random.randint(1000, 9999))
    attempts = 7

    slow_print("Hacker: Simple lock, 4 digits, 7 attempts(thalla for a reason)")
    slow_print("Hacker: But I'll help. I'm not evil. Just efficient.\n")

    while attempts > 0:
        guess = input("Enter code: ")

        if guess == code:
            slow_print("...nice.")
            return True
        else:
            attempts -= 1

            hint = []
            for i in range(min(len(guess), 4)):
                if guess[i] == code[i]:
                    hint.append("✓")
                elif guess[i] in code:
                    hint.append("?")
                else:
                    hint.append("x")

            print(" ".join(hint) + f"   ({attempts} left)")

    slow_print("Hacker: That was disappointing.")
    return False


def task2():
    slow_print("\n[PHASE 2: FILE TRACE]\n")

    binary = "01001000 01000101 01001100 01010000"
    with open("trace.log", "w") as f:
        f.write(binary)

    os.startfile("trace.log")

    slow_print("Hacker: File opened.")
    slow_print("Hacker: Don't overthink it just tell what it says\n")

    user_decode = input("Decode: ").lower()

    if user_decode == "help".lower():
        slow_print("Hacker: ironic.")
        return True
    else:
        slow_print("Hacker: Wrong. And that was basic.")
        return False


def task3():
    slow_print("\n[PHASE 3: SYSTEM LOGS]\n")

    logs = [
        "[21:02] root login success",
        "[21:03] anomaly detected",
        "[21:05] patch ignored",
        "[21:07] override pushed",
        "[21:08] key rotated: GATE-9",
        "[21:09] outbound ping",
    ]

    for i in logs:
        slow_print(i)
        time.sleep(0.4)

    slow_print("\nHacker: System accepts only one key now.")
    key = input("Enter key: ").strip().upper()

    if key == "GATE-9":
        slow_print("\nAccess granted.")
        return True
    else:
        slow_print("Denied.")
        return False


def finale():
    slow_print("\n[FINAL TRACE]\n")

    time.sleep(1)
    slow_print("Tracing origin...")
    time.sleep(2)

    slow_print("Target breached.")
    time.sleep(1)
    slow_print("Data extracted.")
    time.sleep(1)

    slow_print("\nOrigin: YOU\n")

    time.sleep(2)

    slow_print("Hacker: You really thought you were fixing your system?")
    slow_print("Hacker: I needed a clean path.")
    slow_print("Hacker: No flags. No suspicion.\n")

    slow_print("Hacker: So I used yours.")

    time.sleep(2)

    slow_print("\n>>> YOU EXECUTED THE ACCESS <<<")
    slow_print(">>> TRACE COMPLETE <<<\n")

    slow_print("Connection terminated.")