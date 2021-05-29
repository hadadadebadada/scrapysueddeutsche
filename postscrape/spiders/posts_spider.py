from __future__ import absolute_import

import scrapy
xclass PostSpider(scrapy.Spider):

    name = "posts"


    start_urls = [

        'https://www.sueddeutsche.de/',
        'https://www.sueddeutsche.de/politik',
        'https://www.sueddeutsche.de/wirtschaft',
        'https://www.sueddeutsche.de/meinung',
        'https://www.sueddeutsche.de/panorama',
        'https://www.sueddeutsche.de/sport',
        'https://www.sueddeutsche.de/kultur',
        'https://www.sueddeutsche.de/gesellschaft',
        'https://www.sueddeutsche.de/wissen',
        'https://www.sueddeutsche.de/reise',
        'https://www.sueddeutsche.de/auto'
    ]

    ##  """ reponse sind die data, welche gescrapt wurde """
    def parse(self, response):
      page = response.url.split('/')[-1]
      filename = 'posts-%s.html' % page
    ## file wird geöffnet undmit 'wb' für write binary gespeihert 
      with open(filename, 'wb') as f:
            f.write(response.body)
    def parse(self, response):
        for sel in response.xpath('//*[@id="wrapper"]/div[1]/div[5]/div'):
          item = PostItem()
          item['title'] = sel.xpath('//*[@id="wrapper"]/div[1]/div[5]/div/div[1]/a/div/div[2]/h3/text()').extract()  ## gibt jeweils die überschrift des ersten posts
          #title = response.css('h3::text').getall()
          item['author'] = response.css('p.sz-teaser__author::text' ).getall()
          yield item
          #print (title)

 

    ## related links 
    ##>>> response.css('div.related-links a::text').getall()
    ## überschriften
    ## >>> response.css('h3::text').getall() oder >>> response.css('div.teaserlist h3::text' ).getall()
    ## autor
    ##response.css('p.sz-teaser__author::text' ).getall()

