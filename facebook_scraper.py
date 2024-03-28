from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.chrome.options import Options
import requests
import time
import sys
import os
#==============開啟瀏覽器並導向清交二手拍===============
print("=========Initialize=========")
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")

# ------ 設定要前往的網址 ------
url = 'https://www.facebook.com'  
# ------ 登入的帳號與密碼 ------
username = 'your account'
password = 'your password'


# ------ 透過Browser Driver 開啟 Chrome ------
cService = webdriver.ChromeService(executable_path='your chromedriver path')
driver = webdriver.Chrome(service = cService, options=options)
driver.get(url)

time.sleep(1)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
elem = driver.find_element(By.ID,"email")
elem.send_keys(username)

elem = driver.find_element(By.ID,"pass")
elem.send_keys(password)        

elem.send_keys(Keys.RETURN)
time.sleep(5)


#檢查有沒有被擋下來
if len(driver.find_elements(By.XPATH,"//*[contains(text(), '你的帳號暫時被鎖住')]")) > 0:
    driver.find_elements(By.XPATH,"//*[contains(text(), '是')]")[1].click()

spec_url = 'specific facebook group url'
driver.get(spec_url)
print("=========Initialization complete=========")
#====================================================================

def change_mode():
    if(len(driver.find_elements(By.XPATH,"//*[contains(text(), '最相關')]")) > 0):  
        btn = driver.find_element(By.XPATH,"//*[contains(text(), '最相關')]")
        btn.click()
        time.sleep(2)
        btn = driver.find_element(By.XPATH,"//*[contains(text(), '新貼文')]")
        btn.click()
        time.sleep(2)
    elif(len(driver.find_elements(By.XPATH,"//*[contains(text(), '最新動態')]")) > 0):  
        btn = driver.find_element(By.XPATH,"//*[contains(text(), '最新動態')]")
        btn.click()
        time.sleep(2)
        btn = driver.find_element(By.XPATH,"//*[contains(text(), '新貼文')]")
        btn.click()
        time.sleep(2)


def boardcast(url):
    params = {"message": "\n有新的租屋貼文:\n" + url}
    headers = {"Authorization": "Bearer " + "your key",
           "Content-Type":"application/x-www-form-urlencoded"}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers = headers, params=params)
    print(r.status_code)

def main():
    keywords = []  #some keywords you would like to trace. for example ["租屋","租房","套房","雅房","室友","分租","台電","獨立電表","出租","租客"]
    notified_post = ""
    failed = 0
    try:
        while True:
            change_mode()
            if(failed > 3):
                print("重新啟動中...")
                driver.quit()
                p = sys.executable
                os.execl(p,p,*sys.argv)
            soup = Soup(driver.page_source,"html.parser")
            #content = soup.find('div',class_ ='x1iorvi4 x1pi30zi x1l90r2v x1swvt13')
            content = soup.find('div', class_=lambda c: c and c.startswith('x1iorvi4 x1pi30zi'))
            if(content == None):
                driver.refresh()
                print("fetching failed")
                failed = failed + 1
                time.sleep(20)
                continue
            failed = 0
            content = content.text
            current_time = time.strftime("%H:%M:%S")
            if notified_post != content:
                print(f"=============有新貼文 時間:{current_time}=============")
                notified_post = content
                print(notified_post)
                if ("" not in content) and ("" not in content) and ("" not in content): #add some condition if you don't want to trace. for example "限女"
                    for word in keywords:
                        if(word in content): 
                            boardcast(content)
                            break                   
            time.sleep(40)
            driver.refresh()
            time.sleep(15)
    except:
        print("重新啟動中...")
        driver.quit()
        p = sys.executable
        os.execl(p,p,*sys.argv)

if __name__ == "__main__":
    main()



