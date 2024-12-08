#Toga's creation

#libs
import time
import pystyle
import os
import subprocess
import requests
import wget


#funcs
def check_hwid():
    command = 'wmic csproduct get UUID' #wmic csproduct get UUID --> a command to get unique UUID/HWID of Computer
    try:
        result = subprocess.run(command, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        output = result.stdout.strip().splitlines()
        return output[2].strip() #output[2].strip() --> will take 3 line of result in console. 
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    #vars
    Users = ["Name1", "Name2"] #any name can be
    Passwords = ["Password1", "Password2"] #any password can be
    HWIDS = ["136FE459-09EC-42E6-F0C3-K1659EA13D3B"] #just sample, to get real one, you need to open cmd and write there "wmic csproduct get UUID", and then paste it here
    checking_hwid = check_hwid()

    #code
    pystyle.Write.Print("<Your Name> Loader", pystyle.Colors.blue_to_cyan, interval=0.05)
    time.sleep(1)
    pystyle.Write.Print("\nHello! It is <Your Name> Loader!", pystyle.Colors.red_to_purple, interval=0.005)
    time.sleep(1)
    ask_login = pystyle.Write.Input("\nEnter your Login : ", pystyle.Colors.blue_to_red, interval = 0.05)
    ask_password = pystyle.Write.Input("Enter you Password : ", pystyle.Colors.blue_to_red, interval = 0.05)
    if ask_login in Users and ask_password in Passwords: #Checks if Login and Password are in variables "Users" and "Passwords"
        time.sleep(1)
        pystyle.Write.Print("You successfully entered your account!", pystyle.Colors.blue_to_cyan, interval=0.05)
        time.sleep(1)
        pystyle.Write.Print("\nChecking your HWID...", pystyle.Colors.green_to_cyan, interval=0.05)
        time.sleep(1)
        if checking_hwid in HWIDS : #Firstly it runs the function "checking_hwid()" and then checks in variable HWIDS
            url_download = requests.get("https://your.url") #I recommend you to use https://www.file.io/?ysclid=m27oxyzena757357435 you will load your file there, this code will be able to download the file, not html code, but this link can be used only once, next time you need to do new link, or make more links.
            wget.download(url_download)
            pystyle.Write.Print("\nYour HWID matches! Starting the app...", pystyle.Colors.red_to_purple, interval=0.05)
            time.sleep(1)
            bat_path = os.path.join("\\path\\to\\your\\file.exe")
            if os.path.exists(bat_path):
                os.startfile(bat_path)
            else :
                pystyle.Write.Print("Couldn't run the app!", pystyle.Colors.red_to_purple, interval=0.05)
        else :
            pystyle.Write.Print("Your HWID doesn't match!") 
            time.sleep(2.5)
    else :
        pystyle.Write.Print("Login or Password is incorrect!")
        time.sleep(2.5)


#start
if __name__ == "__main__":
    main()