import requests
from bs4 import BeautifulSoup
import smtplib

GMAIL = "YOUR GMAIL"
PASSWORD = "YOUR PASSWORD"
URL = "https://www.amazon.com/dp/B07VT23JDM/ref=syn_sd_onsite_desktop_13?psc=1&uh_it=b4e970d36e155cbb1a1431bdf08f86a8_CT&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMTRJNVI0QzNGWTVSJmVuY3J5cHRlZElkPUEwNTQyOTY4MUY0UVRYWkYwTlAwMSZlbmNyeXB0ZWRBZElkPUEwMTYzNzI1WkQ4TDZGMzBHRklNJndpZGdldE5hbWU9c2Rfb25zaXRlX2Rlc2t0b3AmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ta;q=0.7"
}

response = requests.get(url=URL, headers=HEADERS)

soup = BeautifulSoup(response.content, "lxml")
# print(soup)

price = soup.find(name="p", class_="twisterSwatchPrice").get_text()
price_as_float = float(price.split('$')[1])
print(price_as_float)

title_before_strip = soup.find(name="span", class_="a-size-large product-title-word-break").get_text()
product_title = title_before_strip.strip()

if price_as_float < 135:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs="shruthidakshinamurthy@gmail.com",
            msg=f"Subject:Amazon product price drop!\n\n{product_title} is now {price}. \n\n\n{URL}"
        )