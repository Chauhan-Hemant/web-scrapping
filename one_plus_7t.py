from selenium import webdriver
import numpy as np
import pandas as pd

reviews = pd.DataFrame(columns=['customer_id', 'customer_name', 'review_head', 'review_body', 'review_date', 'ratings'])

driver = webdriver.Chrome('/home/hemant/Downloads/chromedriver_linux64/chromedriver')
driver.get('https://www.amazon.in/Test-Exclusive-748/dp/B07DJLVJ5M/ref=sr_1_1?crid=22IEGEL0LZDYN&keywords=oneplus+7t&qid=1575991606&sprefix=one+%2Caps%2C331&sr=8-1')
driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a').click()

for i in range(0, 500):
    driver.get('https://www.amazon.in/OnePlus-Glacier-Display-Storage-3800mAH/product-reviews/B07DJLVJ5M/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='+str(i))

    ids = driver.find_elements_by_xpath("//*[contains(@id,'customer_review-')]")

    customer_id = []

    for x in ids:
        id = customer_id.append(x.get_attribute('id'))

    for x in customer_id:
        user_name = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[1]/a/div[2]/span')[0]
        review_head = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[2]/a[2]/span')[0]
        review_body = driver.find_elements_by_xpath('//*[@id="' + x + '"]/div[4]/span/span')[0]
        review_date = driver.find_elements_by_xpath('//*[@id="' + x + '"]/span')[0]
        ratings = driver.find_elements_by_xpath('//*[@id="'+x+'"]/div[2]/a[1]')[0]
        stars = ratings.get_attribute('title')

        print(x)
        print(user_name.text)
        print(review_head.text)
        print(review_body.text)
        print(review_date.text)
        print(stars)

        reviews.loc[len(reviews)] = [x, user_name.text, review_head.text, review_body.text, review_date.text, stars]

reviews.to_csv('one_plus_7t.csv')
driver.close()