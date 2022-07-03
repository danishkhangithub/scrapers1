from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import csv



#login_url = 'https://web.facebook.com/?stype=lo&jlou=Afe15k5Nm19xKSd_Kw31qahd6Go7Y0CA-8eEVdkIpM9sXrlHWpch4l4BnB7bzEwnaU6vwBJIqzTGYAkCMoXgNYF9GLXu8zUr5aNlT0iSPZThPw&smuh=5576&lh=Ac8eegEPR8H_XISu8-E'
base_url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.6.1e5b4c29rkCL99&id=623943202801"
chrome_driver_path = '/home/danish-khan/scrapers/researchgate/chromedriver'
names = []
chrome_options = Options()
#chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(
  executable_path=chrome_driver_path, options=chrome_options
)
'''
# default login credential and search query
username = 'danishkhansf@gmail.com'
password = 'danishkhan785'
search_query = "Islamia college Peshawar"
results = []
'''
with webdriver as driver:
    # Set timeout time 
    wait = WebDriverWait(driver, 10)

    # retrive url in headless browser
    driver.get(base_url)
    '''  
    # find search box
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_name("login").click()
    #driver.find_element_by_id("u_0_h_gr").click()
    '''
    time.sleep(2)
    driver.get(base_url)
    time.sleep(5)
    '''
    last_height = driver.execute_script('return document.body.scrollHeight')
    print('height:',last_height)
    time.sleep(5)
    total = []
    while True:
       # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
      time.sleep(2)
      
      #driver.execute_script("window.scrollTo(1, 5000);")
      new_height = driver.execute_script("return document.body.scrollHeight")
      print('new height:' +str(new_height))
      if new_height == last_height:
          break
      last_height = new_height 
    total.append(last_height)   
    '''

    name = driver.find_element_by_css_selector('.J_EbrandLogo font').text
    print(name)
    time.sleep(2)
    
    #//a[@class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8"]
    '''
    links  = driver.find_elements_by_xpath('//div[@class = "buofh1pr hv4rvrfc"]//a')
    for link in links:
        links = link.get_attribute('href')
        print('\nlinks:',links )
        count +=1   
        details = {
          'name' : links
        }
        names.append(details)
    print('count:',count) 
            
    time.sleep(5)
    
#    with open('schools_data.csv', 'w') as f:
#      
#        f.write(str(names),delimiter=',' )
#        f.write('\n')

#    with open('reaction rate list.csv','w') as output:
#     writer= csv.writer(output)
#     writer.writerow(names) 
#    
    
    with open('schools_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f,
                                fieldnames=['name'])
        writer.writeheader()
        writer.writerows(names)
    '''

    # must close the driver after task finished
    driver.close()
