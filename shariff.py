import subprocess
import os
from art import *

def display_logo():
    logo = text2art("Shariff", font='starwars')
    print(logo)
    print("_______________________________")
    print("|                             |")
    print("|     Follow me on Instagram  |")
    print("|  https://www.instagram.com/s.a.m.i.r_012/ |")
    print("|                             |")
    print("|      Check out my GitHub    |")
    print("|   https://github.com/Royalboy2000/  |")
    print("|_____________________________|")
    print()

def clear_screen():
    os.system('clear')

def perform_nmap_scan(website):
    clear_screen()
    display_logo()
    print("Performing Nmap port scanning...")
    subprocess.call(['nmap', website])
    input("Press Enter to continue...")

def perform_nikto_scan(website):
    clear_screen()
    display_logo()
    print("Performing Nikto vulnerability scanning...")
    subprocess.call(['nikto', '-h', website])
    input("Press Enter to continue...")

def perform_exploit_search():
    clear_screen()
    display_logo()
    search_option = input("Enter the option to search (e.g., apache, nginx): ")
    print(f"Performing version detection and exploit search for '{search_option}'...")
    subprocess.call(['searchsploit', search_option])
    input("Press Enter to continue...")

repeat = True
while repeat:
    clear_screen()
    display_logo()

    website = input("Enter website URL: ")

    tool_choice = input("Which tool do you want to use? (nmap/nikto/exploit) or 'skip' to go to the next tool: ")
    if tool_choice.lower() == 'nmap':
        perform_nmap_scan(website)
    elif tool_choice.lower() == 'nikto':
        perform_nikto_scan(website)
    elif tool_choice.lower() == 'exploit':
        perform_exploit_search()

    repeat_option = input("Do you want to scan again? [Y/n]: ")
    if repeat_option.lower() != 'y':
        repeat = False

print("Recon completed!")

