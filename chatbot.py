from colorama import *; init(); print(Fore.GREEN, end="")
import random
import time

def slow_print(text):
    for char in text:
        print(char, end="")
        time.sleep(0.1)
    print()

hacker_slangs=("You're already inside the system. No point backing out now. ",
    "Your machine is a playground at this point. "
    "I see everything. Every keystroke. ",
    "Don't make me escalate this. ",
    "I've got root on your system. ",
    "Left a backdoor open. You didn't even notice. ",
    "Deploying payload… unless you cooperate. ",
    "Your system had too many exploits. Easy entry. ",
    "Nice shell you've got. Mine now. "
    "Your firewall? Decorative. ",
    "Been sniffing your packets for a while. ",
    "Could brute force this, but where's the fun? ",
    "You've got two options. Neither is comfortable. ",
    "Do the task. I disappear. Simple transaction. ",
    "Refuse, and things get… interesting. ",
    "Tick tock. I don't like waiting. ",
    "You're not in control here. You just haven't realized it yet. ",
    "Run the command. Now. ",
    "Type exactly what I say. No deviations. ",
    "Complete the task and we're done. ",
    "Fail, and I start digging deeper. ",
    "This isn't random. I chose your system. ",
    "Your defenses are predictable. ",
    "You're cooperating already. You just don't know it yet. ",
    "I prefer willing participants. Don't make me switch methods.")

def hacker_chat_bot(self):
        if self=="exit":
            slow_print("Hacker: Aww you think you can exit the terminal without my permission")
            slow_print("Hacker: Listen I am the boss here, so will exit whenever I want")
        else:
            slow_print("Hacker: "+random.choice(hacker_slangs))