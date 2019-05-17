import sys
from selenium import webdriver 

if len(sys.argv) > 1:

    print("Opening Browser")
    
    br = webdriver.Firefox()

    emailid = sys.argv[1]       
    password = sys.argv[2]

    br.get("http://www.facebook.com/")

    email = br.find_element_by_xpath('//*[@id="email"]')
    email.send_keys(emailid)

    pwd = br.find_element_by_xpath('//*[@id="pass"]')
    pwd.send_keys(password)

    pwd.submit()
    
else:
    print("Please fill your email and pwd!")    

