import time
import requests
from requests import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from discord_webhook import DiscordWebhook, DiscordEmbed

#Login Details
email = 'emale here'
password = "password here"
itemUrl = 'Ulr'
itemSize = 'Size'


#Payment Details
card_Number = '5188690464584111'
card_Holder_name = 'sample sample'
card_Cvv= '123'
card_Bank_name = 'HSBC'
card_Month='01'
card_Year='2022'


 #WebDriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_extension("bfgblailifedppfilabonohepkofbkpm.crx")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
chrome_options.add_argument("user-agent="+user_agent)
driver = webdriver.Chrome(PATH,chrome_options=chrome_options)
driver.get("chrome-extension://bfgblailifedppfilabonohepkofbkpm/index.html")

#Bypass Queue-it
try:
	print('Bypassing Queue-it....')
	driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rule-groups/div/div[1]/ul[1]/li/button').click()
	driver.find_element_by_xpath('/html/body/app-root/div/nav/div/ul/li[4]/app-toggle/ng-toggle/span/span[3]').click()
	driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[1]/div/div[1]/div[1]/input[1]').send_keys('TitanBypass')
	driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/div/div[1]/div/div[3]/input').send_keys('https://titan22.queue-it.net')
	driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/div/div[2]/div/table/tbody/tr/td[1]/ng-select/div/div/div[2]').click()
	driver.find_element_by_xpath("//*[contains(text(), 'Redirect To')]").click()
	driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/div/div[2]/div/table/tbody/tr/td[2]/input').send_keys('https://www.titan22.com/checkout')
	driver.find_element_by_xpath('/html/body/app-root/div/nav/div/ul/li[3]/button').click()
	print('Bypassing Queue-it Sucessful')
except:
	print('Failed to Bypass')

# Time to enter credentials
#Login Account
try:
	print('Loggin in...')
	driver.get('https://www.titan22.com/customer/account/login/')
	emailAddress = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
	pword = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, "pass"))).send_keys(password)
	loginButton = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, "send2"))).click()
	driver.get(itemUrl)
	print('Login Sucessful')
except:
    print("Failed to Login")

#Selecting Size
try: 
	
	imageSrc = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="magnifier-item-0"]'))).get_attribute("src")
	SKU = driver.find_element_by_xpath('//*[@id="maincontent"]/div[3]/div/div[1]/div[1]/div[2]/div[6]').text
	price = driver.find_element_by_class_name("price").text
	itemName = driver.find_element_by_class_name("base").text
	quantity = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, 'qty'))).send_keys("1")
	SelectedSize = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, 'attribute139')))
	AvailSize = Select(SelectedSize)
	AvailSize.select_by_visible_text(itemSize)
	current_page_url = driver.current_url
	print("Carted " + itemName+  " Sucessful")
	print("Size", itemSize)
	AddtoCart = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, 'product-addtocart-button'))).click()
	proceedToCheckout = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.ID, 'ajaxcart_cancel'))).click() #continuea jaxcart_checkout
	driver.get('https://www.titan22.com/checkout/')
	print("Waiting for checkout page to load...")
except:
	print("Selecting size Failed")

#Checkout Page
try:
	
	checkout = WebDriverWait(driver, 1900).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]/div[5]/div[3]/div/div[4]/div/div/button'))).click()
	print("Waiting for Payment Page to load....")
except:
	print("Checkout Failed")

#2P2C PAYMENT PAGE
try:
	print("Submitting payment")
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_number"))).send_keys(card_Number)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_holder_name"))).send_keys(card_Holder_name)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_cvv"))).send_keys(card_Cvv)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_issuing_bank_name"))).send_keys(card_Bank_name)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_expiry_month")))
	drp = Select(element)
	drp.select_by_visible_text(card_Month)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "credit_card_expiry_year")))
	drp = Select(element)
	drp.select_by_visible_text(card_Year)
	element = WebDriverWait(driver, 100).until(
		EC.presence_of_element_located((By.ID, "btnCCSubmit"))).click()
	orderNumber =driver.find_element_by_xpath('//*[@id="payment-order"]').text
	print("Payment sucess check for OTP/Password")


	webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/690029142032646242/4mhafBRqtyIN9KfSwnapunRKllO64S76OC_tohHud0_Y-r7b9fPAIqCycEPzjSN1c87h', username='DAMBOTv0.4')

	# create embed object for webhook
	embed = DiscordEmbed(title='Checkout Success', description=itemName, color=242424)

	embed.add_embed_field(name='Product Link:', value=current_page_url, inline= False)
	embed.add_embed_field(name='Account', value=email, inline= False)
	embed.add_embed_field(name='Size', value=itemSize,inline= False)
	embed.add_embed_field(name="Order Number", value=orderNumber ,inline= False)
	embed.add_embed_field(name='Price', value=price,inline= False)
	embed.add_embed_field(name='SKU', value=SKU,inline= False)

	# set author
	embed.set_author(name='Titan22.com', url='https://www.titan22.com', icon_url='https://assets.queue-it.net/titan22/userdata/titan.png')

	# add embed object to webhook
	webhook.add_embed(embed)
	# set image
	#embed.set_image(url='https://assets.queue-it.net/titan22/userdata/titan.png', icon='https://assets.queue-it.net/titan22/userdata/titan.png')

	# set thumbnail
	embed.set_thumbnail(url=imageSrc)

	# set footer
	embed.set_footer(text='DAMBOTv0.4 developed by KyaAlod')

	# set timestamp (default is now)
	embed.set_timestamp()

	response = webhook.execute()
	
except:
    print("Encountered Error")














