# Web-Scraper

This is a webscraper written in python, the goal is to check a website once a minute and message the users phone using twilio if the website changes.

To run, you need a file named `variables.py`, it must contain this code:
```python
url = "https://humanfailure.github.io/Web-Scraper/"
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
twilio_phone_number = '+xxxxxxxxxxx'
my_phone_number = '+1-xxx-xxx-xxxx'
```
