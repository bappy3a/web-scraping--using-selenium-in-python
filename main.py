from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('no-sandbox')

driver = webdriver.Chrome(executable_path=r'/home/bappy/www/python/pythonProject1/chromedriver', options=options)
driver.maximize_window()
driver.get("https://webscraper.io/test-sites/e-commerce/static")

driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a').click()
driver.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a').click()
rowDiv = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div')
productInfoList = driver.find_elements_by_class_name('thumbnail')

listoflinks = []
for el in productInfoList:
    productLink=el.find_element_by_class_name('title')
    listoflinks.append(productLink.get_property('href'))

listoflinks = []
alldatas = []
condition=True
while condition:
    productInfoList = driver.find_elements_by_class_name('thumbnail')
    for el in productInfoList:
        productLink = el.find_element_by_class_name('title')
        listoflinks.append(productLink.get_property('href'))

        nameOfProduct = el.find_element_by_class_name('title').text
        priceOfProduct = el.find_element_by_class_name('price').text
        tempJ = {
            'nameOfProduct': nameOfProduct,
            'priceOfProduct': priceOfProduct
        }
        alldatas.append(tempJ)
    try:
        driver.find_elements_by_class_name('/html/body/div[1]/div[3]/div/div[2]/ul/li[15]/a').click()
    except:
        condition=False


print(len(alldatas))