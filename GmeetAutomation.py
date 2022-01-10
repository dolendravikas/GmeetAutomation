from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
from os import system
import re
from webdriver_manager.chrome import ChromeDriverManager

def validate_text(regex,inp):
	if not re.match(regex,inp):
		return False
	return True

print("Enter Your Email : " , end="")
email = input()
while not(validate_text(r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",email)):
        system("cls")
        print("Invalid Email")
        print("Enter Email Again")
        email = input()
system('cls')
print("Enter Your Password : " , end="")
psswd = input()
system('cls')     
print("Enter Meeting Code Without Any Special-Character : " , end="")
code = input()
while not(validate_text(r"^[a-zA-Z0-9]*$",code)):
        system("cls")
        print("Invalid GMeet Code, Try Again")
        print("Without Special Character")
        code = input()
system('cls')


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
start_time = input()
while not(validate_text(r"\d\d:\d\d:\d\d",start_time)):
        system("cls")
        print("Enter In Correct Format [ HH:MM:SS ] ")
        print("Time To Join Class [ Format = HH:MM:SS ] eg. 01:59:20")
        start_time = input()
print("Time to End Class")
end_time = input()
while not(validate_text(r"\d\d:\d\d:\d\d",end_time)):
        system("cls")
        print("InCorrect Format, Try Again   [ HH:MM:SS ] ")
        print("Time to End Class")
        end_time = input()


while current_time != (start_time):
    system("cls")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time , " , Start at : " , start_time)
    sleep(1)

if current_time == (start_time):
    path = "chromedriver.exe"
    opt = Options()
    opt.add_argument("start-maximized") 
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 1 
    })

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
    driver.get("https://meet.google.com/new")
    search = driver.find_element_by_name("identifier")
    search.send_keys(email)
    search.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    search = driver.find_element_by_name("password")
    print(search)
    search.send_keys(psswd)
    search.send_keys(Keys.RETURN)

    sleep(3)
    driver.get("https://meet.google.com/lookup/" + code)
    sleep(3)

    
    try: 
      driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div").click()# Turn OFF Video By Default
      driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div").click()
      driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span").click()
      sleep(20)
    except:
        print("Can't Join, Try Again")
    

    while current_time != end_time:
            system("cls")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time =", current_time , " , End At : " , end_time)
            sleep(1)

    if current_time == end_time:
        driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[9]/div[2]/div[2]/div").click()
        system("cls")
        print("Left Meet")
        driver.close()
