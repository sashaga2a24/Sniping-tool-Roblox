from colorama import Fore, Back, Style
import os
try:
   from rgbprint import gradient_print, Color, rgbprint
except:
    os.system("pip install rgbprint")
# self.version = Shows Version
# title = Shows the title 
# self.items = Shows a list of every item
# self.buys = Shows every success buy
# self.errors = Shows every error occured
# self.last_time = Shows the last execution time
# self.checks = Shows total price checks
# self.task = Shows current task


title = ("""
                     █    ██   ▄████  ▄████▄       ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███           You cool :D
                     ██  ▓██▒ ██▒ ▀█▒▒██▀ ▀█     ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
                    ▓██  ▒██░▒██░▄▄▄░▒▓█    ▄    ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
                    ▓▓█  ░██░░▓█  ██▓▒▓▓▄ ▄██▒     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
                    ▒▒█████▓ ░▒▓███▀▒▒ ▓███▀ ░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
                    ░▒▓▒ ▒ ▒  ░▒   ▒ ░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
                    ░░▒░ ░ ░   ░   ░   ░  ▒      ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
            :)         ░░░ ░ ░ ░ ░   ░ ░           ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ 
                       ░           ░ ░ ░               ░           ░  ░              ░  ░   ░


                             ░█▀▀█ █  █    ▀▀█▀▀ █▀▀█ █▀▀ █▀▀█ █▀▀ █▀▀█ ▀▀█▀▀ ▀▀█▀▀ 
                             ░█▀▀▄ █▄▄█      █   █▄▄█ █   █  █ █   █▄▄█   █     █ 
                             ░█▄▄█ ▄▄▄█      ▀   ▀  ▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀  ▀   ▀     ▀        
                                                                                             
""")
def _print_stats(self) -> None:
    output_lines = []
    output_lines.append(Fore.RED + Style.BRIGHT + title)
    output_lines.append(Fore.RESET + Style.RESET_ALL)
    output_lines.append(Style.BRIGHT + f"                           [ Loaded items: {Fore.GREEN}{Style.BRIGHT}{len(self.items)}{Fore.WHITE}{Style.BRIGHT} ]")
    output_lines.append(Style.BRIGHT + f"                           [ Total buys: {Fore.GREEN}{Style.BRIGHT}{self.buys}{Fore.WHITE}{Style.BRIGHT} ]")
    output_lines.append(Style.BRIGHT + f"                           [ Total errors: {Fore.RED}{Style.BRIGHT}{self.errors}{Fore.WHITE}{Style.BRIGHT} ]")
    output_lines.append(Style.BRIGHT + f"                           [ Last Speed: {Fore.YELLOW}{Style.BRIGHT}{self.last_time}{Fore.WHITE}{Style.BRIGHT} ]")
    output_lines.append(Style.BRIGHT + f"                           [ Total price checks: {Fore.YELLOW}{Style.BRIGHT}{self.checks}{Fore.WHITE}{Style.BRIGHT} ]")
    output_lines.append("")
    output_lines.append(Style.BRIGHT + f"                           [ Version: {self.version}  ]")
    if self.rooms:
        output_lines.append(Style.BRIGHT + f"                           [ Room Users: {Fore.GREEN}{Style.BRIGHT}{len(self.users)}{Fore.WHITE}{Style.BRIGHT} ]")
        output_lines.append(Style.BRIGHT + f"                           [ Room Code: {Fore.GREEN}{Style.BRIGHT}{self.room_code}{Fore.WHITE}{Style.BRIGHT} ]")
        output_lines.append("")
    output_lines.append(Style.BRIGHT + f"                           [ Current Task: {Fore.GREEN}{Style.BRIGHT}{self.task}{Fore.WHITE}{Style.BRIGHT} ]")

    output = '\n'.join(output_lines)
    os.system(self.clear)
    print(output, flush=True)