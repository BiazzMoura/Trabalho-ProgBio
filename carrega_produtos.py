from scrapy.crawler import CrawlerProcess
from trabalho_progbio.spiders.mundial_spider import MundialSpider
from trabalho_progbio.spiders.prix_spider import PrixSpider
from trabalho_progbio.spiders.supermarket_spider import SuperMarketSpider
from twisted.internet import defer, reactor
# https://stackoverflow.com/questions/62252561/scrapy-run-spiders-seqential-with-different-settings-for-each-spider


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
