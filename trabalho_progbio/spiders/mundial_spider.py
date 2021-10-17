import scrapy


class MundialSpider(scrapy.Spider):
    name = "mundial"
    start_urls = [
        'https://www.supermercadosmundial.com.br/ofertas?format=json&page=1',
    ]

    def parse(self, response):
        self.next_page = 1
        for produto in self.parse_page(response):
            yield produto

    def parse_page(self, response):
        for data in response.css('.product'):
            produto = {}
            produto['nome'] = data.css('.name-product::text').get()
            produto['preco'] = data.css('.price-product strong::text').get() + data.css('.price-product strong > sup::text').get()
            yield produto
        next_url = response.css("button#bnt-carregar::attr(data-href)").get()
        if next_url and len(response.css('.product')):
            self.next_page += 1
            yield response.follow(next_url+"?page="+str(self.next_page), callback=self.parse_page)
