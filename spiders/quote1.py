# -*- coding: utf-8 -*-
import scrapy


class Quote1Spider(scrapy.Spider):
    name = 'quote1'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css('div.quote'):

            yield{
                'quote': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tag': quote.css('a.tag::text').extract_first()
              
            }
        next_page_url = response.css('li.next > a::attr(href)').extract_first()
        if next_page_url is not None:
            next_page_url= response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url,callback=self.parse)

#'quote': '//span[@class='text']/text()',
              #'author': '//small[@class='author']/text()',
              #'tag': '//a[@class='tag']/text()'
        