from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" # Browser executable If u aint using Brave or Chrome cry

option = webdriver.ChromeOptions()
option.binary_location = browser_path
driverService = Service("chromedriver.exe") # Download this!!!!!!!!!!

browser = webdriver.Chrome(service=driverService, options=option)

browser.get("https://www.drfrostmaths.com/timestables-game.php") # Opens to Dr Frost

go = input("Log in twat. \nEnter y to continue ") # Waits until logged in. If not logged in, HTML element will not be found. (Line 21)
while go.lower() != "y":
    go = input("Log in twat. \nEnter y to continue ")

MaxNum = int(input("Enter max right answers "))
START = browser.find_element(by=By.CLASS_NAME, value="very-large-button-variant") # Start Button
START.click() 

for i in range(MaxNum):
    sleep(0.01)
    question = browser.find_element(by=By.ID, value="question") # The question as a string
    ans = browser.find_element(by=By.ID, value="calculator-display") # The entry field
 
    if "×" in question.text:
        ans.send_keys(int(eval(question.text.replace("×", "*")))) # Finds answer
    else:
        ans.send_keys(int(eval(question.text.replace("÷", "/")))) # Finds answer

