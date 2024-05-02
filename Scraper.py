class Scraper:
    def __init__(self, headers,requests,BeautifulSoup):
        self.requests=requests
        self.BeautifulSoup=BeautifulSoup
        self.headers = headers
        

    def scrape(self,url):
        response = self.requests.get(url, headers=self.headers)
        return self.BeautifulSoup(response.content, 'lxml')