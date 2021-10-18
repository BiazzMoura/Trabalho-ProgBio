#Script feito de acordo com as instruções do tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html

#Foi importado o modulo scrapy, que é um Framework open source para extração de informação em websites
import scrapy

#O spider é responsável pelo site que será realizado o rastreamento, pelo fluxo de navegação e pelo parse html para extração de informação.
class SuperMarketSpider(scrapy.Spider):
 #name = nome do supermercado escolhido
    name = "supermarket"
#URL da pagina do mercado que se deseja extrair os dados(produtos e preços)
    start_urls = [
        'https://smpravc.com.br/encartes/',
    ]
#Criando uma função parse que vai pegar os dados de respostas da pagina e permitirá a extração de dados desejados usando seletores da linguagem CSS
    def parse(self, response):
        for data in response.css('.produtos .item'):
            produto = {}
            produto['nome'] = data.css('p::text').get()
            produto['preco'] = data.css('.preco big::text').get() + data.css('.preco small::text').get()
            yield produto
