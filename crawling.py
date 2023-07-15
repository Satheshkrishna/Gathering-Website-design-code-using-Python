import requests

def urlcode(url):
    try:
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError:
            pass
url = "google.com"
with open("sar.txt", "r") as list:
    for run in list:
        testing = run.strip()
        res = testing+"."+url
        response = urlcode(res)
        if response:
            print("discovering domain running : >>"+res) 
        
        
