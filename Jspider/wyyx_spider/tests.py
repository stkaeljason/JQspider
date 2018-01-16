from django.test import TestCase
import requests
# Create your tests here.

res = requests.post('https://m.you.163.com/xhr/item/detail.json',data={'id':'1452007'})
print(res.text)