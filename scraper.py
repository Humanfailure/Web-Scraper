from twilio.rest import Client
import variables
import requests
from bs4 import BeautifulSoup
import twilio
import schedule
import time

headline = ""


def message(text_body):
    client = Client(variables.account_sid, variables.auth_token)

    message = client.messages.create(
        body=text_body,
        from_=variables.twilio_phone_number,
        to=variables.my_phone_number,
    )

    print(message.sid)


def no():
    url = variables.url1
    global page
    page = BeautifulSoup(requests.get(url).text, "html.parser")


def change():
    global headline
    old_headline = headline
    print("Checking.")
    no()
    for headlines in page.find_all("h1"):
        print(headlines.text.strip())
        headline = headlines.txt

    if headline != old_headline:
        message("Your GitHub page has changed.")
        old_headline = headline


no()
for headlines in page.find_all("h1"):
    print(headlines.text.strip())
    headline = headlines.txt

schedule.every(1).minutes.do(change)

while 1:
    schedule.run_pending()
    time.sleep(1)
