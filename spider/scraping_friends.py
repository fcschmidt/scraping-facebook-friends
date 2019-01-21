import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://m.facebook.com/'


def get_session(url, cookies):
    session = requests.Session()
    response = session.get(url, cookies=cookies)
    return response


class FacebookScraper:

    def __init__(self, cookies, uid):
        self.cookies = cookies
        self.uid = uid
        self.amount_friends = None

    def get_friends_page(self):
        # url = BASE_URL  + uid + '?v=friends&startindex=' + str(startidx)
        url = BASE_URL + self.uid + '/friends'
        resp = get_session(url, self.cookies)

        new_friends = self.extract_friends(resp.text)
        friends = new_friends
        return friends

    @staticmethod
    def extract_friends(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        content = soup.find('div', {"id": "root"})

        links = content.find_all("a", class_='ce')
        friends_list = [f.text for f in links]
        return friends_list
    """
    def get_amount_friends(self, uid):
        profile_url = BASE_URL + '/' + uid
        resp = get_session(profile_url, self.cookies)
        soup = BeautifulSoup(resp.content, 'html.parser')

        profile_name = soup.title.text
        # amount_friends = soup.find_all('span', class_='_52jd')
    """

