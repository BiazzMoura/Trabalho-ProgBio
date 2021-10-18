#Foi importado do scrapy o CrawlProcess que tem o intuito de realizar o rastreamento na web dos itens desejados
from scrapy.crawler import CrawlerProcess
#Foram importados para esse script os spiders criados dos sites dos mercados
from trabalho_progbio.spiders.mundial_spider import MundialSpider
from trabalho_progbio.spiders.prix_spider import PrixSpider
from trabalho_progbio.spiders.supermarket_spider import SuperMarketSpider
from twisted.internet import defer, reactor

#Para esse script, foi feita uma utilização do Stackoverflow:
# https://stackoverflow.com/questions/62252561/scrapy-run-spiders-seqential-with-different-settings-for-each-spider

# Foi criada uma função para realizar um "Crawler" dos sites desejados e criar assim, um arquivo.csv.
def carregar_produtos():
    runner = CrawlerProcess(settings={
        "FEEDS": {
            "precos_%(name)s.csv": {"format": "csv"},
        },
    })
    runner.crawl(PrixSpider)
    runner.crawl(SuperMarketSpider)
    runner.start()
    runner.join()
