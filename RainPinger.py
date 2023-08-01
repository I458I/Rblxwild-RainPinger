from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Style, Fore
import win32gui
import win32con
import random
zaza = input("Enter your webhook: ")
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
options = webdriver.ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=options)
while True:
 kik = random.randint(25, 35)
 blck = random.randint(1, 10)
 time.sleep(blck)
 try:
  driver.get('https://rblxwild.com/cases')
  time.sleep(kik)
  guardian = driver.find_element(By.CSS_SELECTOR, "span[data-v-abe66f7a][class='amount']")
  tim = driver.find_element(By.CSS_SELECTOR, "span[data-v-abe66f7a][class='color-white']")
  times = tim.text
  timr = tim.text
  tilo = times.split(":")[0]
  milo = times.split(":")[1]
  timr = timr.replace(":", "")
  dropy = guardian.text
  dropy = dropy.replace(",", "")
  linky = "https://rblxwild.com/"
  print(f"{Style.BRIGHT}{Fore.RED}{timr}")
  print(f"{Style.BRIGHT}{Fore.BLUE}{tilo}{Fore.RESET}:{Fore.YELLOW}{milo}")
  print(f"{Style.BRIGHT}{Fore.GREEN}{dropy}")
  are = int(dropy)
  timr = int(timr)
  dropy = "{:,}".format(are)
  if are >= 25000 and timr <= 200:
   hook = DiscordWebhook(url=zaza, avatar_url="https://cdn.discordapp.com/attachments/1131282292258648194/1131282331160805396/icon_for_vespy.png", username="458's Rain!⭐", content="@everyone")
   embd = DiscordEmbed(title="🌟 IT'S RAINING! 🌟")
   embd.add_embed_field(name=f"**RAIN VALUE: {dropy}**", value=f"**Time left: {tilo}:{milo}**")
   embd.add_embed_field(name=f"**Join here!**", value=f"[**Link**]({linky})")
   hook.add_embed(embd)
   hook.execute()
 except Exception as g:
   print(g)
 time.sleep(blck)
