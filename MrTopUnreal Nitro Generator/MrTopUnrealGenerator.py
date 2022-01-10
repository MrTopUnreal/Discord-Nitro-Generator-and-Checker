import requests
import random
import string
import time

print(""" MrTopUnreal's Nitro Generator 
 """)


time.sleep(0.3)
print(" Discord: MrTopUnreal#7995\n Server: https://discord.gg/pYnH69uFy9\n Nulled.to Profile: https://www.nulled.to/user/5051021-mrtopreally")
time.sleep(0.2)

num = int(input('\n How many codes do you want to Generate and Check? '))

with open("NitroCodes.txt", "w", encoding='utf-8') as file:
    print("\n Your codes are being generated\n")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")



with open("NitroCodes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ")
            break
        else:
            #should be invalid
            print(f" Invalid | {nitro} ")



print("\nCodes successfully generated. Working codes are in Valid Codes.txt")