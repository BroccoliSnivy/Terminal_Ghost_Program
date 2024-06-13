from os import system, name
from colorama import Fore
from time import sleep




class Ghost():
    def __init__(self) -> None:
        self.EyeArea = "████"
        self.mouthAreaL1 = "████"
        self.mouthAreaL2 = "████████"
        self.mouthAreaL3 = "████████"
        self.mouthAreaL41 = "██"
        self.mouthAreaL42 = "██"
        self.tongue1 = "████"
        self.tongue2 = "████████"

    def displayGhostTextBanner(self):
        print(Fore.RED+"""\n\n
                        ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓
                       ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
                      ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
                      ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
                      ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
                       ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
                        ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
                      ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      
                            ░  ░  ░  ░    ░ ░        ░           
                """+Fore.RESET)
        
    def displayBooBannerArt(self):
        print(Fore.CYAN+"""\n\n
                                 ▄▄▄▄    ▒█████   ▒█████  
                                ▓█████▄ ▒██▒  ██▒▒██▒  ██▒
                                ▒██▒ ▄██▒██░  ██▒▒██░  ██▒
                                ▒██░█▀  ▒██   ██░▒██   ██░
                                ░▓█  ▀█▓░ ████▓▒░░ ████▓▒░
                                ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ 
                                ▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ 
                                 ░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒  
                                 ░          ░ ░      ░ ░  
                                      ░                   
                """+Fore.RESET)
    def dispalyGhostBannerArt(self, eyeArea, mouth1, mouth2, mouth3, mouth41 ,mouth42, tongue1, tongue2):
        print(Fore.WHITE+f"""
                                      ████████████
                                  ████            ████
                              ████                    ████
                            ██                            ██
                          ██                                ██
                          ██    ████        ████            ██
                  ████  ██    ██{eyeArea}██    ██{eyeArea}██            ██  ████
                ██    ████    ██{eyeArea}██    ██{eyeArea}██            ████    ██
                ██    ██      ██{eyeArea}██    ██{eyeArea}██            ██      ██
                  ██  ██      ██{eyeArea}██    ██{eyeArea}██          ██      ██
                    ████        ████        ████                  ██
                      ██              ████                      ██
                      ██            ██{mouth1}██                    ██
                      ██          ██{mouth2}██                  ██
                      ██          ██{mouth3}██                  ██
                      ██          ██{mouth41}████{mouth42}██                  ██
                        ██        ████{tongue1}████                  ██    ██
                        ██        ██{tongue2}██                    ████  ██
                          ██        ████████                            ██
                          ██                                            ██
                            ██                                        ██
                              ████                                ████
                                  ████████████████████████████████
              """+Fore.RESET)
    
    def clearance(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

def main():
    instance1 = Ghost()
    instance1.clearance()
    # RED BLUE MAGENTA YELLOW
    while True:
        for i in range(1, 4):
            if i == 1:
                instance1.clearance()
                instance1.displayGhostTextBanner()
                instance1.dispalyGhostBannerArt(Fore.GREEN+instance1.EyeArea+Fore.RESET,Fore.GREEN+instance1.mouthAreaL1+Fore.RESET,Fore.GREEN+instance1.mouthAreaL2+Fore.RESET,Fore.GREEN+instance1.mouthAreaL3+Fore.RESET,Fore.GREEN+instance1.mouthAreaL41+Fore.RESET,Fore.GREEN+instance1.mouthAreaL42+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue1+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue2+Fore.RESET)
                instance1.displayBooBannerArt()
                sleep(4)
            if i == 2:
                instance1.clearance()
                instance1.displayGhostTextBanner()
                instance1.dispalyGhostBannerArt(Fore.BLUE+instance1.EyeArea+Fore.RESET, Fore.BLUE+instance1.mouthAreaL1+Fore.RESET, Fore.BLUE+instance1.mouthAreaL2+Fore.RESET, Fore.BLUE+instance1.mouthAreaL3+Fore.RESET, Fore.BLUE+instance1.mouthAreaL41+Fore.RESET,Fore.BLUE+instance1.mouthAreaL42+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue1+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue2+Fore.RESET)
                instance1.displayBooBannerArt()
                sleep(4)
            if i == 3:
                instance1.clearance()
                instance1.displayGhostTextBanner()
                instance1.dispalyGhostBannerArt(Fore.MAGENTA+instance1.EyeArea+Fore.RESET, Fore.MAGENTA+instance1.mouthAreaL1+Fore.RESET, Fore.MAGENTA+instance1.mouthAreaL2+Fore.RESET, Fore.MAGENTA+instance1.mouthAreaL3+Fore.RESET, Fore.MAGENTA+instance1.mouthAreaL41+Fore.RESET,Fore.MAGENTA+instance1.mouthAreaL42+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue1+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue2+Fore.RESET)
                instance1.displayBooBannerArt()
                sleep(4)
            if i == 4:
                instance1.clearance()
                instance1.displayGhostTextBanner()
                instance1.dispalyGhostBannerArt(Fore.YELLOW+instance1.EyeArea+Fore.RESET, Fore.YELLOW+instance1.mouthAreaL1+Fore.RESET, Fore.YELLOW+instance1.mouthAreaL2+Fore.RESET, Fore.YELLOW+instance1.mouthAreaL3+Fore.RESET, Fore.YELLOW+instance1.mouthAreaL41+Fore.RESET,Fore.YELLOW+instance1.mouthAreaL42+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue1+Fore.RESET,Fore.LIGHTRED_EX+instance1.tongue2+Fore.RESET)
                instance1.displayBooBannerArt()
                sleep(4)

main()