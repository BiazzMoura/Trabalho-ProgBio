#Script feito de acordo com as instruções do tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html

#Foi importado o modulo scrapy, que é um Framework open source para extração de informação em websites
import scrapy

#O spider é responsável pelo site que será realizado o rastreamento, pelo fluxo de navegação e pelo parse html para extração de informação.
class MundialSpider(scrapy.Spider):
 #name = nome do supermercado escolhido
    name = "mundial"
#URL da pagina do mercado que se deseja extrair os dados(produtos e preços)
    start_urls = [
        'https://www.supermercadosmundial.com.br/ofertas?format=json&page=1',
    ]
#Criando uma função parse que vai pegar os dados de respostas da pagina e permitirá a extração de dados desejados usando seletores da linguagem CSS

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
