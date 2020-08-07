# -*- coding: utf-8 -*-
import os
import scrapy
import requests
from scrapy.http import Request


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['fmovies.wtf']
    start_urls = ['http://fmovies.wtf/']
    target_url=''
    absolute_category_url =''

    def __init__(self):
        self.iterator = 0
    

    def parse(self, response):
        target_url = response.xpath('.//*[@class="links"]/li/a/@href').extract_first()
        absolute_category_url = response.urljoin(target_url)
        yield Request(absolute_category_url, callback=self.image_downloader)

    def image_downloader(self, response):
        images = response.xpath('.//*[@class="poster"]/img/@src').extract()
        try:
            target_url = response.xpath('//*[@class="widget"]/div[@class="widget-body"]/div/ul/li/a[@rel="next"]/@href').extract_first()
            for image in images:
                self.iterator += 1
                img_data = requests.get(image).content
                path = './images/File-'+str(self.iterator)+'.jpg'
                with open(path, 'wb') as handler:
                    handler.write(img_data)

            absolute_category_url = response.urljoin(target_url)
            yield Request(absolute_category_url, callback=self.image_downloader)       
        except:
            self.log('DOWNLOAD COMPLETE . NO MORE PAGES TO SCRAPE')
        
            
        
        
        