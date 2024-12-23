import pyautogui
import time
n = int(input("Enter the number of rows for the pyramid: "))
print("Switch to your target window in 3 seconds...")
time.sleep(3)
for i in range(1, n + 1):
    pyautogui.typewrite("#" * i) 
    pyautogui.press("enter")     
