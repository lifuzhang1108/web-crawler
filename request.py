import requests
import time
import urllib.parse
from bs4 import BeautifulSoup
from interruptingcow import timeout
url = 'http://httpbin.org/ip'
headers = {
  'Accept': 'application/json',
  'X-MyHeader': '123',
}

def generate_headers():
    return {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        }


def get(id):
    index=str(id)
    headers=generate_headers()
    url="http://www.bu.edu/phpbin/directory/?index_id=X"+index+"&timestamp=1533539487&secure=2537350"
    r = requests.get('https://api.scraperapi.com/?key=' + "cc79b7d554b7d8d434aca9065e095de5" + '&url=' + urllib.parse.quote(url)+'&render=true' + '&keep_headers=true', headers=headers)
    #r = requests.get("http://www.bu.edu/phpbin/directory/?index_id=X280000&timestamp=1533626130&secure=1715725")
    page=r.content
    soup = BeautifulSoup(page, 'html.parser')
    items = soup.find(attrs={'id':'content-main'}).children
    dd=soup.find_all('dd')
    for item in dd:
        print(item.get_text())


def gett(id):
    for retry in range(1, 3):
        # logging.warning('[fetch] try=%d, url=%s' % (retry, url))
        retry_because_of_timeout = False
        try:
            index = str(id)
            headers = generate_headers()
            url = "http://www.bu.edu/phpbin/directory/?index_id=X" + index + "&timestamp=1533539487&secure=2537350"
            r = requests.get(
                'https://api.scraperapi.com/?key=' + "cc79b7d554b7d8d434aca9065e095de5" + '&url=' + urllib.parse.quote(
                    url) + '&render=true' + '&keep_headers=true', headers=headers)
            # r = requests.get("http://www.bu.edu/phpbin/directory/?index_id=X280000&timestamp=1533626130&secure=1715725")
            page = r.content
            soup = BeautifulSoup(page, 'html.parser')
            items = soup.find(attrs={'id': 'content-main'}).children
            dd = soup.find_all('dd')
            for item in dd:
                print(item.get_text())

        except Exception as e:
            retry_because_of_timeout = True
            pass

        if retry_because_of_timeout:
            print("TIMEOUT")
        else:
            break


def gettt(id):
    for retry in range(1,3):
        try:
            with timeout(60, exception=RuntimeError):
                index = str(id)
                headers = generate_headers()
                url = "http://www.bu.edu/phpbin/directory/?index_id=X" + index + "&timestamp=1533539487&secure=2537350"
                r = requests.get('https://api.scraperapi.com/?key=' + "cc79b7d554b7d8d434aca9065e095de5" + '&url=' + urllib.parse.quote(url) + '&render=true' + '&keep_headers=true', headers=headers)
                # r = requests.get("http://www.bu.edu/phpbin/directory/?index_id=X280000&timestamp=1533626130&secure=1715725")
                page = r.content
                soup = BeautifulSoup(page, 'html.parser')
                items = soup.find(attrs={'id': 'content-main'}).children
                dd = soup.find_all('dd')
                for item in dd:
                    print(item.get_text())
                time.sleep(5)
                break
        except RuntimeError:
            print("Timeout")
            pass
        except Exception as e:
            print("ERROR")
            pass
for i in range(423,600):
    j=i+280000
    gettt(j)
    print("---------------------------------")


