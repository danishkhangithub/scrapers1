import requests
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36" ,
    'referer':'https://www.google.com/'
}

r = requests.get("http://webcache.googleusercontent.com/search?q=cache:www.naukri.com/jobs-in-andhra-pradesh")

print(r.text)