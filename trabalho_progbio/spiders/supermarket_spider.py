# https://docs.scrapy.org/en/latest/intro/tutorial.html
import scrapy


class SuperMarketSpider(scrapy.Spider):
    name = "supermarket"
    start_urls = [
        'https://smpravc.com.br/encartes/',
    ]

    def parse(self, response):
        for data in response.css('.produtos .item'):
            produto = {}
            produto['nome'] = data.css('p::text').get()
            produto['preco'] = data.css('.preco big::text').get() + data.css('.preco small::text').get()
            yield produto
