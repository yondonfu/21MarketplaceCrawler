import datetime
import logging
import requests

APP_TITLE = 'Hello, World!'

class AppCrawler():
    def __init__(self, start_url, log_file):
        self.configure_logging(log_file)

        self.start_url = start_url

    def configure_logging(self, log_file):
        logging.basicConfig(level=logging.INFO,
                            filename=log_file,
                            filemode='a',
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M')

        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)

        logging.getLogger('crawler').addHandler(self.console)

        self.logger = logging.getLogger()

    def crawl_pages(self):
        curr_page = 1
        total_pages = self.get_total_pages()

        aggregated_endpoints = []

        self.logger.info('Crawler start timestamp: {}\n'.format(datetime.datetime.now()))
        self.logger.info('Total pages: {}'.format(total_pages))

        while curr_page < total_pages:
            self.logger.info('Parsing page: {}'.format(curr_page))
            aggregated_endpoints += self.parse_page(self.start_url + '?page=' + str(curr_page))
            curr_page += 1

        self.logger.info('Crawler end timestamp: {}\n'.format(datetime.datetime.now()))

        return aggregated_endpoints

    def get_total_pages(self):
        res = requests.get(self.start_url).json()

        return res['total_pages']

    def parse_page(self, url):
        res = requests.get(url).json()

        endpoints = []
        apps = res['results']

        for app in apps:
            if app['title'] == APP_TITLE:
                self.logger.info('Found app endpoint: {}'.format(app['app_url']))
                endpoints.append(app['app_url'])

        return endpoints


if __name__ == '__main__':
    # Start from page 1 of entire list of published apps
    start_url = 'https://api.21.co/market/apps/'

    crawler = AppCrawler(start_url, 'crawler.log')
    crawler.crawl_pages()
