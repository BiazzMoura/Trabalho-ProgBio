import scrapy


class PrixSpider(scrapy.Spider):
    name = "prix"
    start_urls = [
        'https://www.tijuca.superprix.com.br/buscapagina?fq=H:153&O=OrderByBestDiscountDESC&PS=1500&cc=15&sm=0&PageNumber=1&sl=1daabf0d-5f18-47a2-8b3f-709dc17dc522',
    ]

    def parse(self, response):
        for data in response.css('.prateleira .data'):
            produto = {}
            produto['nome'] = data.css('h3 > a::text').get()
            produto['preco'] = data.css('.price .newPrice em::text').get()[3:]
            yield produto
