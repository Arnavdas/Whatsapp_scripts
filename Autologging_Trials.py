#  TRial for without scanning QR code :

# Triall 1 : :FAILED : https://stackoverflow.com/a/54065166/5963608
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# options = Options()
# # Below commented not working for firefox_profile param in webdriver.Firefox
# options.add_argument("-profile")
# prof_pth = "/home/arnav/.mozilla/firefox/zav20pxf.default-release"
# options.add_argument(prof_pth)
# geck_pth = '/home/arnav/Gecko_folder/geckodriver'
# firefox_capabilities = DesiredCapabilities.FIREFOX
# firefox_capabilities['marionette'] = True
# driver = webdriver.Firefox(options=options.profile)#, capabilities=firefox_capabilities)
# driver.get('https://web.whatsapp.com/')
# time.sleep(30)

# Trial 2: FAILED : firefox_profile has been deprecated :https://stackoverflow.com/a/60539482/5963608
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2)
# profile.set_preference('browser.download.manager.showWhenStarting', False)
# profile.set_preference('browser.download.dir', os.getcwd())
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', ('application/vnd.ms-excel'))
# profile.set_preference('general.warnOnAboutConfig', False)
# profile.update_preferences()
# gecko_path = '/home/arnav/Gecko_folder/geckodriver'
# # path = "path_to_firefoxs\\Mozilla Firefox\\firefox.exe"
# # driver = webdriver.Firefox()
# driver = webdriver.Firefox(firefox_profile=profile,executable_path=gecko_path)
# driver.get('https://web.whatsapp.com/')


# TRial 3 :FAILED :https://stackoverflow.com/a/54065166/5963608
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# profile_path = '/home/arnav/.cache/mozilla/firefox/zav20pxf.default-release/'
# options=Options()
# options.set_preference('profile', profile_path)
# service = Service('/home/arnav/Gecko_folder/geckodriver')
# driver = webdriver.Firefox(service=service, options=options)
# driver.get('https://web.whatsapp.com/')
# time.sleep(30)

#  Trail 4: Failed :https://stackoverflow.com/a/61031427/5963608
# driver = webdriver.Firefox()
# fp = webdriver.FirefoxProfile('	/home/arnav/.cache/mozilla/firefox/zav20pxf.default-release')
# driver = webdriver.Firefox(firefox_profile=fp)
# driver.get('https://web.whatsapp.com/')

# TRial 5: Failed : OPening it in new tab : https://stackoverflow.com/questions/49831933/eliminate-entering-qr-whatsapp-web-automated-by-selenium-java
# driver.execute_script('''window.open("https://web.whatsapp.com/","_blank");''')
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[0])
# driver.get('https://web.whatsapp.com/')

# Trial 6 : FAILED : https://stackoverflow.com/a/69572816/5963608
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# gecko_file = r'/home/arnav/Gecko_folder/geckodriver'
# # profile_path = r'/home/arnav/.cache/mozilla/firefox/zav20pxf.default-release'
# profile_path = r'/home/arnav/.mozilla/firefox/zav20pxf.default-release'
# options=Options()
# options.set_preference('profile', profile_path)
# service = Service(gecko_file)
# driver = Firefox(service=service, options=options)
# driver.get("https://web.whatsapp.com/")
# # driver.quit()


# Trial 7 : FAILED : ABOVE + https://www.selenium.dev/documentation/webdriver/capabilities/firefox/
#  firefox_profile has been deprecated, please use an Options object
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from selenium.webdriver.firefox.options import Options

# profile_path = r'/home/arnav/.cache/mozilla/firefox/zav20pxf.default-release'
# options=Options()
# firefox_profile = FirefoxProfile(profile_path)
# # firefox_profile.set_preference("javascript.enabled", False)
# options.profile = firefox_profile
# driver = webdriver.Firefox(options=options)
# driver.get("https://web.whatsapp.com/")
