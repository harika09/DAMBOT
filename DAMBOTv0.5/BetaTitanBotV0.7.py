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
from config import chromePath, extensionPath, userAgentPath, extensionUrlPath, cardId, cardNameId, cvvId, bankNameId, cardMonthId, cardYearId, submitId, orderId, creditId, shippingId, placeOrderId, checkoutPage, sizeId, productToCart, continueShopping, sizeId, qtyId, quantity, price, productName, skuPath, imageId, imageSrc, waitingTime, loginUrl, emailId, passId, loginButton, email, password, itemUrl, itemSize, card_Number, card_Holder_name, card_Cvv, card_Bank_name, card_Month, card_Year, newRule, toggle, title, titanBypass, queueit, queueitBypass,redirectTo, clickRedirect, titanPage, titanPageCheckout, saveBypass

 #WebDriver
PATH = chromePath
options = Options()
options.add_extension(extensionPath)
user_agent = userAgentPath
options.add_argument("user-agent="+user_agent)
driver = webdriver.Chrome(PATH,options=options)
driver.get(extensionUrlPath)

#Bypass Queue-it
try:
	print('Bypassing Queue-it....')
	driver.find_element_by_xpath(newRule).click()
	driver.find_element_by_xpath(toggle).click()
	driver.find_element_by_xpath(title).clear()
	driver.find_element_by_xpath(title).send_keys(titanBypass)
	driver.find_element_by_xpath(queueit).send_keys(queueitBypass)
	driver.find_element_by_xpath(redirectTo).click()
	driver.find_element_by_xpath(clickRedirect).click()
	driver.find_element_by_xpath(titanPage).send_keys(titanPageCheckout)
	driver.find_element_by_xpath(saveBypass).click()
	print('Bypassing Queue-it Sucessful')
except:
	print('Failed to Bypass')

# Time to enter credentials
#Login Account
try:
	print('Loggin in...')
	driver.get(loginUrl)
	emailAddress = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, emailId))).send_keys(email)
	pword = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, passId))).send_keys(password)
	loginButton = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, loginButton))).click()
	driver.get(itemUrl)
	print('Login Sucessful')
except:
    print("Failed to Login")

#Selecting Size
try: 
	image_url = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.XPATH, imageId))).get_attribute(imageSrc)
	SKU = driver.find_element_by_xpath(skuPath).text
	price = driver.find_element_by_class_name(price).text
	itemName = driver.find_element_by_class_name(productName).text
	quantity = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, qtyId))).send_keys(quantity)
	SelectedSize = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, sizeId)))
	AvailSize = Select(SelectedSize)
	AvailSize.select_by_visible_text(itemSize)
	current_page_url = driver.current_url
	AddtoCart = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, productToCart))).click()
	proceedToCheckout = WebDriverWait(driver, waitingTime).until(EC.presence_of_element_located((By.ID, continueShopping))).click() #continuea jaxcart_checkout
	driver.get(checkoutPage)
	
	print("On going checkout")
except:
	print("Selecting size Failed")

#Checkout Page
try:
	driver.find_element_by_id(creditId).click()
	shipping = WebDriverWait(driver, 1900).until(EC.presence_of_element_located((By.ID, shippingId))).click()
	checkout = WebDriverWait(driver, 1900).until(EC.presence_of_element_located((By.XPATH, placeOrderId)))
	checkout.click()
	print("Placed Order")
except:
	print("Checkout Failed")		

#2P2C PAYMENT PAGE
try:
	print("Submitting payment")
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, cardId))).send_keys(card_Number)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, cardNameId))).send_keys(card_Holder_name)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, cvvId))).send_keys(card_Cvv)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, bankNameId))).send_keys(card_Bank_name)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, cardMonthId)))
	drp = Select(element)
	drp.select_by_visible_text(card_Month)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, cardYearId)))
	drp = Select(element)
	drp.select_by_visible_text(card_Year)
	element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, submitId))).click()
	orderNumber =driver.find_element_by_xpath(orderId).text
	print("Payment sucess check for OTP/Password")


	webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/690029142032646242/4mhafBRqtyIN9KfSwnapunRKllO64S76OC_tohHud0_Y-r7b9fPAIqCycEPzjSN1c87h', username='DAMBOTv0.6')

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
	embed.set_thumbnail(url=image_url)

	# set footer
	embed.set_footer(text='DAMBOTv0.6 developed by KyaAlod')

	# set timestamp (default is now)
	embed.set_timestamp()

	response = webhook.execute()
	
except:
    print("Encountered Error")
