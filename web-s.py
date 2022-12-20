from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome()

page_number = 1
while True:
    driver.get(f'https://www.jumia.co.ke/laptops/?page={page_number}#catalog-listing')

    
    #Find name and price
    product_names = driver.find_elements(By.CLASS_NAME, 'name')
    

    #Break if end of pagination
    if len(product_names) == 0:
        break
    
    prices = driver.find_elements(By.CLASS_NAME, 'prc')


    #Write to csv
    with open('products.csv', 'a', newline='') as products:
        writer = csv.writer(products)
        for i in range(len(product_names)):
            name = product_names[i].text[:70]
            price = prices[i].text
            if len(name) < 1 > len(price):
                continue
            else:
                writer.writerow((name, price))

    page_number = page_number + 1
    
driver.quit()