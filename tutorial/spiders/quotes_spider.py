import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.google.com/search?q=(renewables+OR+"renewable+energy"+OR+"Renewable+Power")+AND++(conference+OR+summit)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('000000000000000000000000')
        for href in response.css('div.Gx5Zad'):
            tags = href.css("div.AP7Wnd::text").getall()
            print('tags>>>>>>>',tags)
