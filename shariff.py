import subprocess
import os
from art import *

def display_logo():
    logo = text2art("Shariff", font='poison')
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

def perform_wordpress_vulnerability_check(api_token, website):
    clear_screen()
    display_logo()
    print("Performing WordPress website vulnerability check...")
    subprocess.call(['wpscan', '--url', website, '--api-token', api_token])
    input("Press Enter to continue...")

def perform_wordpress_password_bruteforce(username, password_list, website):
    clear_screen()
    display_logo()
    print("Performing WordPress password brute-forcing...")
    subprocess.call(['wpscan', '--url', website, '--passwords', password_list, '--user', username])
    input("Press Enter to continue...")

def perform_sql_injection_crawling(website):
    clear_screen()
    display_logo()
    print("Performing SQL injection database crawling...")
    subprocess.call(['sqlmap', '-u', website, '--crawl'])
    input("Press Enter to continue...")

def perform_sql_injection_rce(website):
    clear_screen()
    display_logo()
    print("Performing SQL injection RCE (Remote Code Execution)...")
    subprocess.call(['sqlmap', '-u', website, '--os-shell'])
    input("Press Enter to continue...")

repeat = True
while repeat:
    clear_screen()
    display_logo()

    website = input("Enter website URL: ")

    print("Choose a tool:")
    print("1: Nmap scan")
    print("2: Nikto scan")
    print("3: Exploit search")
    print("4: WordPress vulnerability check")
    print("5: WordPress password brute-forcing")
    print("6: SQL injection database crawling")
    print("7: SQL injection RCE (Remote Code Execution)")

    tool_choice = input("Enter the number of the tool you want to use, or 'skip' to go to the next tool: ")

    if tool_choice == '1':
        perform_nmap_scan(website)
    elif tool_choice == '2':
        perform_nikto_scan(website)
    elif tool_choice == '3':
        perform_exploit_search()
    elif tool_choice == '4':
        api_token = input("Enter your WPScan API token: ")
        perform_wordpress_vulnerability_check(api_token, website)
    elif tool_choice == '5':
        username = input("Enter the username to use for brute-forcing: ")
        password_list = input("Enter the location of the password list: ")
        perform_wordpress_password_bruteforce(username, password_list, website)
    elif tool_choice == '6':
        perform_sql_injection_crawling(website)
    elif tool_choice == '7':
        perform_sql_injection_rce(website)

    repeat_option = input("Do you want to scan again? [Y/n]: ")
    if repeat_option.lower() != 'y':
        repeat = False

print("Recon completed!")

