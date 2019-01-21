# import getpass
from spider.facebook_login import FacebookLogin
from spider.scraping_friends import FacebookScraper

USERNAME = ''
PASSWORD = ''


def login(username, password):
    conn = FacebookLogin()
    conn.start_crawler()
    conn.facebook_login(username, password)
    cookies = conn.driver.get_cookies()

    uid = input("Enter User id: ")

    conn.close_connection()

    formatted = {}
    for cook in cookies:
        formatted[cook['name']] = cook['value']

    scraper = FacebookScraper(formatted, uid=uid)
    friends_list = scraper.get_friends_page()

    print(friends_list)
    print(len(friends_list))


def main():
    # username = input("Enter your Facebook email: ")
    # password = getpass.getpass(prompt='Enter your facebook password: ')
    # login(username, password)
    login(USERNAME, PASSWORD)


if __name__ == '__main__':
    main()
