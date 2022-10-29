import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html',
    ]


    def parse(self,response):
        # with open("post.html","wb") as f:
        #     f.write(response.body)
        for block in response.css("article.product_pod"):
            yield{
                    # "title":response.xpath("//div[@class='p13n-sc-truncate p13n-sc-line-clamp-1']/text()").extract()
                    "title":block.xpath(".//h3/a/text()").get(),
                    "price":block.xpath(".//div/p[@class='price_color']/text()").get()[6:]
                }
        # next_page = response.xpath("//li[@class='a-last']/a@href").extract_first()