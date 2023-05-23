import requests
import time
import json
import os

try:
    from rgbprint import rgbprint, gradient_print, Color
except:
    os.system("pip install rgbprint")

with open('config.json') as f:
    config_data = json.load(f)

cookie = config_data['accounts'][0]['cookie']

def get_username(cookie):
    headers = {
        "Cookie": f".ROBLOSECURITY={cookie}"
    }
    response = requests.get("https://users.roblox.com/v1/users/authenticated", headers=headers)
    data = response.json()
    name = data.get('name')
    return name

roblox_name = get_username(cookie)

title = (""" ▄████▄ ██▒   █▓ ███▄ ▄███▓     ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  
▒██▀ ▀█▓██░   █▒▓██▒▀█▀ ██▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄▓██  █▒░▓██    ▓██░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██ █░░▒██    ▒██      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░ ▒▀█░  ▒██▒   ░██▒   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░ ░ ▐░  ░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒    ░ ░░  ░  ░      ░   ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
░           ░░  ░      ░      ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
░ ░          ░         ░            ░           ░  ░              ░  ░   ░     
░           ░                                                                  


                             ░█▀▀█ █  █    ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ 
                             ░█▀▀▄ █▄▄█      █   █▄▄█ █   █  █ █   █▄▄█   █     █ 
                             ░█▄▄█ ▄▄▄█      ▀   ▀  ▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀  ▀   ▀     ▀         """)
start_time = time.monotonic()
def _print_stats(self) -> None:
    gradient_print(title, start_color="f58b00", end_color="0008f5")
    elapsed = time.monotonic() - start_time
    elapsed_str = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    gradient_print(f"                           • Script Version: {self.version}  ", start_color="f58b00", end_color="0008f5")
    print(f"                           ━━━━━━━━━━━━━━━━")
    gradient_print(f"                           • Current Task: {self.task} ", start_color="f58b00", end_color="0008f5")
    gradient_print(f"                           • Roblox Account: {roblox_name} ", start_color="f58b00", end_color="0008f5")
    gradient_print(f"                           • Proxies: {len(self.proxy_list)} ", start_color="f58b00", end_color="0008f5")  
    gradient_print(f"                           • Running Time: {elapsed_str}     ", start_color="f58b00", end_color="0008f5")
    print(f"                           ━━━━━━━━━━━━━━━━")
    gradient_print(f"                           •(Items loaded) Items To Cum: {len(self.items)}", start_color="f58b00", end_color="0008f5")

    item_list = list(self.items)

    item_display = item_list[:3] if len(item_list) > 3 else item_list
    short_list = ', '.join(item_display)
    if len(item_list) > 3:
        short_list += f"...({len(item_list) - 3}+)"

    gradient_print(f"                           • Ids: {short_list}  ", start_color="f58b00", end_color="0008f5") 
    gradient_print(f"                           • Price Checks: {self.checks}", start_color="f58b00", end_color="0008f5")
    gradient_print(f"                           • Speed: {self.last_time} ", start_color="f58b00", end_color="0008f5")
    gradient_print(f"                           • (Buyed) Items Cummed: {self.buys}    ", start_color="f58b00", end_color="0008f5")
    gradient_print(f"                           • Errors: {self.errors}  ", start_color="f58b00", end_color="0008f5")
    if self.rooms:
        unique_names = set(self.users)
        gradient_print(f"                           • Username: {self.username}", start_color="f58b00", end_color="0008f5")
        gradient_print(f"                           • Users: {len(unique_names)}  ", start_color="f58b00", end_color="0008f5")
        
        name_list = list(unique_names)
        
        name_display = name_list[:3] if len(name_list) > 3 else name_list
        users_list = ', '.join(name_display)
        if len(name_list) > 3:
            users_list += f"...({len(name_list) - 3}+)"

        gradient_print(f"                           • Usernames: {users_list}  ", start_color="f58b00", end_color="0008f5")
        gradient_print(f"                           • Room Code: {self.room_code}  ", start_color="f58b00", end_color="0008f5")
    print(f"                           ━━━━━━━━━━━━━━━━")