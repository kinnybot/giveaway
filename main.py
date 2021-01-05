import time
import random

import tweepy

CONSUMER_KEY = 'ENTER_CONSUMER_KEY_HERE'
CONSUMER_SECRET = 'ENTER_CONSUMER_SECRET_HERE'
ACCESS_KEY = 'ENTER_ACCESS_KEY_HERE'
ACCESS_SECRET = 'ENTER_ACCESS_SECRET_HERE'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

with open('./entries.txt') as f:
  entries = f.read().splitlines()
print(f'{len(entries)} Total Entries')

for i in range(10):
  winner = random.choice(entries)
  print(f'Winner Announced in: {10-i}', end=' \r')
  time.sleep(1)

status = f'Congrats {winner} You will be DM\'d Shortly'
print(status)
api.update_status(status=status)