#Script feito de acordo com as instruções do tutorial: https://docs.scrapy.org/en/latest/intro/tutorial.html

#Foi importado o modulo scrapy, que é um Framework open source para extração de informação em websites

import scrapy

#O spider é responsável pelo site que será realizado o rastreamento, pelo fluxo de navegação e pelo parse html para extração de informação.
class PrixSpider(scrapy.Spider):
    name = "prix"
 #URL da pagina do mercado que se deseja extrair os dados(produtos e preços)

    start_urls = [
        'https://www.tijuca.superprix.com.br/buscapagina?fq=H:153&O=OrderByBestDiscountDESC&PS=1500&cc=15&sm=0&PageNumber=1&sl=1daabf0d-5f18-47a2-8b3f-709dc17dc522',
    ]
#Criando uma função parse que vai pegar os dados de respostas da pagina e permitirá a extração de dados desejados usando seletores da linguagem CSS

    def parse(self, response):
        for data in response.css('.prateleira .data'):
            produto = {}
            produto['nome'] = data.css('h3 > a::text').get()
            produto['preco'] = data.css('.price .newPrice em::text').get()[3:]
            yield produto
