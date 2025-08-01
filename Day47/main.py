from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("PRODUCT_URL")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
response = requests.get(URL, headers=headers)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
product_pricing= (soup.find(name="span", class_ = "a-price-whole").text).split(".")[0]
product_price = float(product_pricing.replace(",", ""))

product_title = soup.find(name="span", class_="a-size-large product-title-word-break").text.strip()
BUY= 15000
if product_price < BUY:
    message_promt = f"{product_title} is now for Rupees {product_price}"
    with smtplib.SMTP(os.getenv("MY_SERVER"),port=os.getenv("MY_PORT")) as connection:
        connection.starttls()
        result = connection.login(user=os.getenv("SENDER_EMAIL"),password=os.getenv("SENDER_PASSWORD"))
        connection.sendmail(from_addr=os.getenv("SENDER_EMAIL"), to_addrs=os.getenv("RECIEVER_EMAIL"), msg=f"Subject: Amazon {product_title} Price Alert!\n\n{message_promt}\nCheckout {URL}".encode("utf-8"))
