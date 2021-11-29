from typing import Text
import requests
import time

tele_auth_token = '2145819990:AAFGS4UUd-c3kXZJqOOf6DI280VVo7UiNhw'
tele_group_id = 'nachotest_bot1'

img = 'https://images.unsplash.com/photo-1593642633279-1796119d5482?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxlZGl0b3JpYWwtZmVlZHwxfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60'
image = 'https://media.istockphoto.com/photos/bitcoin-with-circuit-board3d-render-picture-id1313200433?b=1&k=20&m=1313200433&s=170667a&w=0&h=iI8PXT8TmAJgU1uRDhhCyZSGSW6KyZ9ljB2QteRMMWM='
msg = f'Message received on Group sent by bot \nMessage Admin\n@Nacho61'


def send_msg(message):
	while (True):
		
		tele_api = f'http://api.telegram.org/bot{tele_auth_token}/sendPhoto?chat_id=@{tele_group_id}&photo={image}&caption={message}'
		tele_resp = requests.get(tele_api)
		if tele_resp.status_code == 200:
			print('Sent')
		else:
			print('Error')
		time.sleep(10)

send_msg(msg)
