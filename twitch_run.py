
import datetime
import time
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import subprocess
import os
from pathlib import Path
import shutil

### Obsługa przeglądarki
PATH = "P:\\Projekty\\Python\\Twitch\\Main\\geckodriver.exe" # Zmiana na własny
driver = webdriver.Firefox()

UserName = os.getlogin()
time.sleep(10)

print(UserName)

path_download = f"C:\\Users\\{UserName}\\Downloads\\" #Zmiana na własny

file_name = ["Most watched games on Twitch - SullyGnome.csv", "Most streamed games on Twitch - SullyGnome.csv"]

for i in file_name:
    if os.path.exists(path_download + i):
        os.remove(path_download + i)
    else:
        print("file does not exist")

time.sleep(5)

### Ustalenie który miesiąc ma być pobrany
# Określenie czasu
time_now = datetime.datetime.now()

year_now = time_now.year
month_now = time_now.strftime("%B")

# Pętla miesiąc wstecz
if month_now == 'January':
    month_doc = 'December'
    year_now = year_now - 1
elif month_now == 'February':
    month_doc = 'January'
elif month_now == 'March':
    month_doc = 'February'
elif month_now == 'April':
    month_doc = 'March'
elif month_now == 'May':
    month_doc = 'April'
elif month_now == 'June':
    month_doc = 'May'
elif month_now == 'July':
    month_doc = 'June'
elif month_now == 'August':
    month_doc = 'July'
elif month_now == 'September':
    month_doc = 'August'
elif month_now == 'October':
    month_doc = 'September'
elif month_now == 'November':
    month_doc = 'October'
elif month_now == 'December':
    month_doc = 'November'


### Otwarcie odpowiedniej strony i kliknięcie
web_page = f"https://sullygnome.com/games/{year_now}{month_doc}/watched"
driver.get(web_page)
time.sleep(7)

select_100 = Select(driver.find_element(By.NAME, 'tblControl_length'))
select_100.select_by_value('100')
time.sleep(7)

link_csv = driver.find_element(By.XPATH, '//*[@id="tblControl_wrapper"]/div[1]/div[1]/button[1]').click()

web_page = f"https://sullygnome.com/games/{year_now}{month_doc}/streamed"
driver.get(web_page)
time.sleep(7)

link_csv = driver.find_element(By.XPATH, '//*[@id="tblControl_wrapper"]/div[1]/div[1]/button[1]').click()
time.sleep(7)

driver.close()


### Przeniesienie CSV z download do foldera na dysku P:
Path_P = "P:\\Projekty\\Python\\Twitch\\Main\\" #własny folder

for j in file_name:
    if os.path.exists(Path_P + j):
        os.remove(Path_P + j)
    else:
        print("file does not exist on drive P:")

for k in file_name:
    shutil.move(path_download + k, Path_P)

time.sleep(10)

