from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
time.sleep(30)
# driver.maximize_window()# to enlarge the new window being opened


def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)
    
    
#  Finding a contact & clicking it ; 
contact, flag = 'Arnav Das', 0 # contact name should be very recent atleast withing 13 contacts ( a very peculiar thing but yes)
for i in range(1, 13):
    if i == 12:
        print('no such {} found in last 11 chats'.format(contact))
        break
    xpth = '/html/body/div[1]/div[1]/div[1]/div[3]/div/div[2]/div[1]/div/div/div[{}]/div/div/div[2]'.format(i)
    element_presence(By.XPATH, xpth, 40)
    clk = driver.find_element(By.XPATH, xpth)# class for clicking the contact name
    if contact in clk.text:
        clk.click()
        flag=1 # implies contact has been found 
        break
 

if flag == 1:# MSG TYPINGG  & SENDING
    # MSG TYPINGG :
    xpth = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    # finding msg box to type :
    msg = driver.find_element(By.XPATH, xpth)# xpath of space of typing msg
    msg.click()
    # Typing the msg in the found out space & sending
    typed_msg = 'hiiiii '
    msg.send_keys(typed_msg + Keys.ENTER)
    # Using Button class :# was successfull before
#     send = driver.find_element(by=By.CLASS_NAME, value='_4sWnG')
#     driver.execute_script("arguments[0].click();", send)
    print(clk.text)
    time.sleep(10)
#     driver.close()

if flag == 1: # MSG retrieving
    time.sleep(30)
#      below xpath is of the space 
    xpth = '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
    # finding msg box to type :
    spc = driver.find_element(By.XPATH, xpth)# xpath of space of typing msg
    spc.click()
    
    cls='copyable-text'# Successfull
    content = driver.find_elements(by=By.CLASS_NAME, value=cls)#.text
    for c in content:# Printing out the retrieved messages
        print(c.text)

driver.close()
