from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  # Use your preferred browser
url = "(https://books.toscrape.com/catalogue/category/books_1/index.html)"  # Replace with the actual URL
driver.get(url)

books = []
for book in WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="book"]'))):
    title = book.find_element(By.XPATH, './/h2[@class="title"]').text
    price = book.find_element(By.XPATH, './/span[@class="price"]').text
    stock_status = book.find_element(By.XPATH, './/span[@class="stock-status"]').text
    rating = book.find_element(By.XPATH, './/span[@class="rating"]').text
    description = book.find_element(By.XPATH, './/p[@class="description"]').text
    product_info = book.find_element(By.XPATH, './/ul[@class="product-info"]').text
    category = book.find_element(By.XPATH, './/span[@class="category"]').text
    
    book_data = {
        'title': title,
        'price': price,
        'stock_status': stock_status,
        'rating': rating,
        'description': description,
        'product_info': product_info,
        'category': category
    }
    
    books.append(book_data)

driver.quit()
print(books)