import requests

def shorten_url(token,url):
    try:
        header = {
        "Authorization": "Bearer "+token,
        "Content-Type": "application/json"
        }
        params = {
        "long_url": url
        }

        response = requests.post("https://api-ssl.bitly.com/v4/shorten", json=params, headers=header)
        data = response.json()
        if 'link' in data.keys(): short_link = data['link']
        else: short_link = None
        return short_link
    except exception as e:
        print(e)

token = "<your bitly token>"
url = "<url_to_be_shortened>"
print(shorten_url(token,url))
