from lxml.html import fromstring
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import random
from itertools import cycle

def get_proxies():
    
    url = "https://hidemy.name/en/proxy-list/?country=ALDZADARAMAUATAZBDBYBOBABWBRBGKHCMCACLCNCOCRHRCYCZDKDOECEGFIFRGEDEGRHNHKHUINIDIRIQIEITJPKZKEKRKGLVLBLTMKMWMYMXMDMNMZNPNLNGNOPKPSPAPYPEPHPLPTPRRORUSARSSGSKSISOZAESSZCHTWTZTHTNTRUGUAAEGBUSUYVEVNVIZW&maxtime=1000&type=s&anon=34#list"	
    display = Display(visible=0, size=(800, 600))
    display.start()

    options =  webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('Chromdriver Location Here',options=options)
    #driver = webdriver.Chrome("chromedriver.exe", options=options)
    
    driver.get(url)
	
    timeout = 10
    try:
        element_present = EC.presence_of_element_located((By.ID, 'proxy__t'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")
	
    data = driver.page_source.encode('utf-8')
    #print data
	
    parser = fromstring(data)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:11]:
        proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
        proxies.add(proxy)
		
    driver.quit()
    display.stop()
	
    return proxies

def reacquire_web_page(proxy):
    url_base = "https://www.lottoland.com/en/keno247/"
    display = Display(visible = 0, size = (800, 600))
    display.start()
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/home/haseebawan/Desktop/src/chromedriver',options=options)
    #driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url_base)
    if "funds" in str(driver.page_source.encode("utf-8")):
        print("!!!")
    x_interval = randint(1,4)
    time.sleep(x_interval)
    driver.quit()
    display.stop()

def Robot_Core(exact_bets, no_draws, multiplier, start_from):
    data = ""
    url_base = "https://www.lottoland.com/en/keno247/"
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    for i in range(10):
        req_counter = 0
        req_retry_times_val = 4
        proxy = next(proxy_pool)
        while(req_counter <= req_retry_times_val):
            req_counter += 1
            try:
                r = request.get(url_base, proxies = {"http":proxy})
                data = r.content
                if len(data):
                    #print(proxy)
                    break
                else:
                    x_interval = random.uniform(3.0, 7.5)
                    time.sleep(x_interval)
            except:
                continue
        if len(data):
            working_proxy = proxy
            break

    display = Display(visible = 0, size = (800, 600))
    display.start()
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome('Chrome Driver Location Here',options=options)
    #driver = webdriver.Chrome("chromedriver.exe", options=options)
    driver.get(url_base)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "loginOverlay-loginForm-username-input")))
    login_key = driver.find_element_by_css_selector("#topNavigation > ul > li:nth-child(2) > span").click()
    time.sleep(1)
    username = driver.find_element_by_name("loginOverlay-loginForm-username-input").send_keys("EMAIL")
    time.sleep(1)
    password = driver.find_element_by_name("loginOverlay-loginForm-password-input").send_keys("PASSWORD")
    time.sleep(1)
    submit = driver.find_element_by_name("loginOverlay-loginForm-submit").click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "loginOverlay-loginForm-submit")))
    time.sleep(10)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "l-header-funds")))
    current_balance = driver.execute_script("""return $("#navItemPayinControl > a > div.l-header-funds > span.l-header-funds-amount").attr("title");""")
    if current_balance:
        current_balance = float(current_balance.replace("€",""))
        driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-content > div.l-tippengine-header > div.l-tippengine-panel-actions.l-tippengine-panel.l-tippengine-panel-inline > div > div").click();""")
        #array = [29, 41, 21, 72, 1, 55, 66, 8, 42]
        while True:
            page_status = driver.execute_script("return document.readyState;")
            if page_status != "complete":
                time.sleep(5)
            else:
                break
        for i in exact_bets:
            driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-content > div.l-tippengine-body > div:nth-child(1) > div > div > div > div.l-tippengine-line-body > div > div.l-tippengine-numbers > div:nth-child(""" + str(i) + """) > span").click();""")
            time.sleep(0.5)

        driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-content > div.l-tippengine-footer > div > div > div.l-tippengine-panel-duration.l-tippengine-panel > div.l-tippengine-panel-body > label:nth-child(""" + str(no_draws) + """) > input").click();""")
        time.sleep(1)
        driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-content > div.l-tippengine-footer > div > div > div.l-tippengine-panel-bet-multiplier.l-tippengine-panel > div.l-tippengine-panel-body > div.l-tippengine-stake-multiplier.l-tippengine-stake-multiplier-mobile.l-select-legacy.l-select-legacy-row > div > div > select > option:nth-child(""" + str(multiplier) + """)").attr("selected",true);""")
        time.sleep(1)
        #date_field = "02. Feb. 2020 19:44" 
        driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-content > div.l-tippengine-footer > div > div > div.l-tippengine-panel-first-draw.l-tippengine-panel > div.l-tippengine-panel-body > div.l-tippengine-first-draw.l-select-legacy.l-select-legacy-row > div > div > select > option").each(function() {  if ($(this).is(`:contains('"""+  start_from + """')`)){ $(this).attr("selected",true); console.log("YES") } });""")
        time.sleep(1)    
        driver.execute_script("""$("#tippenginev2-tippengine > div:nth-child(2) > div > div.l-tippengine-extra-footer > div > div > div.l-tippengine-stake-submit-container > div.l-tippengine-stake-submit > button").click();""")
        while True:
            page_status = driver.execute_script("return document.readyState;")
            if page_status != "complete":
                time.sleep(5)
            else:
                break
        time.sleep(5)
        total_amount = driver.execute_script("""return $("#shoppingCart > div:nth-child(3) > div > div > div > span").attr("title");""")
        total_amount = float(total_amount.replace("€",""))
        if total_amount > current_balance:
            print("Not enough funds. Loggin Out!")
            time.sleep(2)
            driver.execute_script("""$("#j_idt5986-controlLogout > span").click();""")
            time.sleep(10)
            print("Succesfully Logged Out!")
        else:
            time.sleep(1)
            driver.execute_script("""$("#paymentSubmitForm-paymentFinished").click();""")
            time.sleep(5)
            while True:
                page_status = driver.execute_script("return document.readyState;")
                if page_status != "complete":
                    time.sleep(5)
                else:
                    print("Bet slip submitted successfully!")
                    break
            driver.execute_script("""$("#j_idt5986-controlLogout > span").click();""")
            time.sleep(10)
            print("Succesfully Logged Out!")

            #ADDED THE CODE FOR SUBMITTING THE FORM WITH ENOUGH FUNDS
            
    else:
        pass
    #print(current_balance)
    driver.quit()
    display.stop()

    
#print(get_proxies())
#Robot_Core()
