from colorama import Fore, Style
import requests
import time
zadx = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
website = input("Website domain: ")
while True:
 time.sleep(1)
 print(f"{Style.BRIGHT}{Fore.GREEN}Ping")
 check = requests.get(website, headers=zadx).status_code
 print(f"{Fore.BLUE}Pong: {check}")
