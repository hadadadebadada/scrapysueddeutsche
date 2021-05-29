import scrapy

class PostItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    #last_updated = scrapy.Field(serializer=str)
