import scrapy


class ImgData(scrapy.Item):
    # other fields...
    images = scrapy.Field()
    image_urls = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "douban"

    start_urls = [
        'https://www.douban.com/group/topic/241830939/?_i=8668274pgoGGzC',
    ]

    image_urls = []

    def parse(self, response):
        print(response.text)
        # for page in pages:
        #     page = page.replace("http://", "https://")
        #     yield scrapy.Request(page, callback=self.item_parse, meta={'page': page})

    def item_parse(self, response):

        images1 = response.selector.xpath(
            '//*[@id="Content"]/p/img/@src').getall()

        images2 = response.selector.xpath(
            '//*[@id="Content"]/p/a/img/@src').getall()

        image_urls = images1+images2

        yield ImgData(image_urls=image_urls)

        next_page_url = response.selector.xpath(
            '//*[@id="after_this_page"]/@href').get()

        print(next_page_url)
        # item_parse
