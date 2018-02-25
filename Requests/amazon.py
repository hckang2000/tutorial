# import lxml
from lxml import html
import csv
import os
import requests
from exceptions import ValueError
from time import sleep
from random import randint
import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parse(url):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}
    
    try:
        # Retrying for failed requests
        for i in range(20):
            # Generating random delays
            sleep(randint(1,2))
            # Adding verify=False to avold ssl related issues
            response = requests.get(url, headers=headers, verify=False)

            if response.status_code == 200: 
                doc = html.fromstring(response.content)
                # print response.content

                XPATH_NAME = '//h1[@id="title"]//text()'
                XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]//text()'
                XPATH_ORIGINAL_PRICE = '//td[contains(text(),"List Price") or contains(text(),"M.R.P") or contains(text(),"Price")]/following-sibling::td/text()'
                XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
                XPATH_AVAILABILITY = '//div[@id="availability"]//text()'
                XPATH_AUTHOR = '//a[@class="a-link-normal contributorNameID"]//text()'
                XPATH_NUMBER_OF_REVIEWS = '//span[@id="acrCustomerReviewText"]//text()'
                XPATH_NUMBER_OF_STARS = '//*[@id="reviewSummary"]/div[2]/span/text()'
                XPATH_NUMBER_OF_5_STARS = '//a[@class="a-size-base a-link-normal 5star histogram-review-count"]//text()'
                XPATH_NUMBER_OF_4_STARS = '//a[@class="a-size-base a-link-normal 4star histogram-review-count"]//text()'
                XPATH_NUMBER_OF_3_STARS = '//a[@class="a-size-base a-link-normal 3star histogram-review-count"]//text()'
                XPATH_NUMBER_OF_2_STARS = '//a[@class="a-size-base a-link-normal 2star histogram-review-count"]//text()'
                XPATH_NUMBER_OF_1_STARS = '//a[@class="a-size-base a-link-normal 1star histogram-review-count"]//text()'

                for i in range(1,8):
                    XPATH_DATE = '//*[@class="content"]/ul/li[%s]/b/text()'%(i)
                    temp = doc.xpath(XPATH_DATE)
                    RAW_DATE = []
                    if "Publisher:" in temp:
                        var = '//*[@class="content"]/ul/li[%s]/text()'%(i)
                        RAW_DATE = doc.xpath(var)
                        break

                RAW_NAME = doc.xpath(XPATH_NAME)
                RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
                RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
                RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
                RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
                RAW_AUTHOR = doc.xpath(XPATH_AUTHOR)
                RAW_NUMBER_OF_REVIEWS = doc.xpath(XPATH_NUMBER_OF_REVIEWS)
                RAW_NUMBER_OF_STARS = doc.xpath(XPATH_NUMBER_OF_STARS)
                RAW_NUMBER_OF_5_STARS = doc.xpath(XPATH_NUMBER_OF_5_STARS)
                RAW_NUMBER_OF_4_STARS = doc.xpath(XPATH_NUMBER_OF_4_STARS)
                RAW_NUMBER_OF_3_STARS = doc.xpath(XPATH_NUMBER_OF_3_STARS)
                RAW_NUMBER_OF_2_STARS = doc.xpath(XPATH_NUMBER_OF_2_STARS)
                RAW_NUMBER_OF_1_STARS = doc.xpath(XPATH_NUMBER_OF_1_STARS)
                # RAW_DATE = doc.xpath(XPATH_DATE) 

                # print RAW_NUMBER_OF_5_STARS               

                NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
                SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).encode('utf-8').strip() if RAW_SALE_PRICE else None
                CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
                ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).encode('utf-8').strip() if RAW_ORIGINAL_PRICE else None
                AVAILABILITY = ''.join(RAw_AVAILABILITY).encode('utf-8').strip() if RAw_AVAILABILITY else None
                AUTHOR = ''.join(RAW_AUTHOR).encode('utf-8').strip() if RAW_AUTHOR else None
                NUMBER_OF_REVIEWS = ''.join(RAW_NUMBER_OF_REVIEWS).encode('utf-8').strip() if RAW_NUMBER_OF_REVIEWS else None
                NUMBER_OF_STARS = ''.join(RAW_NUMBER_OF_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_STARS else None
                NUMBER_OF_5_STARS = ''.join(RAW_NUMBER_OF_5_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_5_STARS else "0"
                NUMBER_OF_4_STARS = ''.join(RAW_NUMBER_OF_4_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_4_STARS else "0"
                NUMBER_OF_3_STARS = ''.join(RAW_NUMBER_OF_3_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_3_STARS else "0"
                NUMBER_OF_2_STARS = ''.join(RAW_NUMBER_OF_2_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_2_STARS else "0"
                NUMBER_OF_1_STARS = ''.join(RAW_NUMBER_OF_1_STARS).encode('utf-8').strip() if RAW_NUMBER_OF_1_STARS else "0"
                DATE = ''.join(RAW_DATE).strip() if RAW_DATE else None

                if not ORIGINAL_PRICE:
                    ORIGINAL_PRICE = SALE_PRICE
                # retrying in case of captcha
                if not NAME:
                    raise ValueError('captcha')

                data = {
                    'NAME': NAME,
                    'SALE_PRICE': SALE_PRICE,
                    'CATEGORY': CATEGORY,
                    'ORIGINAL_PRICE': ORIGINAL_PRICE,
                    'AVAILABILITY': AVAILABILITY,
                    'URL': url,
                    'AUTHOR': AUTHOR,
                    'NUMBER_OF_REVIEWS' : NUMBER_OF_REVIEWS,
                    'NUMBER_OF_STARS' : NUMBER_OF_STARS,
                    'NUMBER_OF_5_STARS' : NUMBER_OF_5_STARS,
                    'NUMBER_OF_4_STARS' : NUMBER_OF_4_STARS,
                    'NUMBER_OF_3_STARS' : NUMBER_OF_3_STARS,
                    'NUMBER_OF_2_STARS' : NUMBER_OF_2_STARS,
                    'NUMBER_OF_1_STARS' : NUMBER_OF_1_STARS,                      
                    'DATE' : DATE,
                }
                # print data
                return data
            
            elif response.status_code==404:
                break

    except Exception as e:
        print e

def ReadAsin():
    # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))

    AsinList = open("/home/vallabh/Project/public-amazon-crawler/test.csv" , "r+")            
    extracted_data = []

    for i in AsinList:
        i = i.strip(" ")
        url = "http://www.amazon.in/dp/" + i
        print "Processing: " + url
        # Calling the parser
        parsed_data = parse(url)
        if parsed_data:
            extracted_data.append(parsed_data)

    # Writing scraped data to csv file
    flag = 1
    while os.path.exists("/home/vallabh/Project/public-amazon-crawler/results/scraped_data_%s.csv" %flag):
        flag+=1

    with open('/home/vallabh/Project/public-amazon-crawler/results/scraped_data_%s.csv' %flag, 'w') as csvfile:
        fieldnames = ['NAME','SALE_PRICE','CATEGORY','ORIGINAL_PRICE','AVAILABILITY','URL','AUTHOR','NUMBER_OF_REVIEWS','NUMBER_OF_STARS','NUMBER_OF_5_STARS','NUMBER_OF_4_STARS','NUMBER_OF_3_STARS','NUMBER_OF_2_STARS','NUMBER_OF_1_STARS','DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()    
        for data in extracted_data:
            writer.writerow(data)

if __name__ == "__main__":
    ReadAsin()
