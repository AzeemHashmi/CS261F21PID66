import scrapy


class HotelSpider(scrapy.Spider):
    name = 'hotel'
    start_urls = {
        'https://www.booking.com/searchresults.html?aid=397594;label=gog235jc-1DCAEoggI46AdIM1gDaLUBiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuAK9mJGMBsACAdICJDY4YWE4NmRjLTY0ZGUtNGEzOS1iZDg3LWQ5NDJmMjgwMzk2MdgCBOACAQ;sid=0f662c65adf2e0b50fbfe7657511e250;dest_id=-2762812;dest_type=city;sig=v1MxHhE72d&'
    }

    def parse(self, response, **kwargs):
        title = response.css('title::text').extract()
        yield {'titletext': title}
