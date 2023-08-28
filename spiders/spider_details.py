import scrapy
from scrapper_one.items import PropertyItem


class scrapper_Two_Spider(scrapy.Spider):
    name = 'spider_details'
    start_urls = ['https://www.nepalhomes.com/search?page=1']

    def parse(self, response):
        prefix = 'https://www.nepalhomes.com'
        houses = response.css('.property__card-text')
        pagination = response.css('ul.pagination')
        for house in houses:
            link = prefix + house.css('.property__card-contact.search_propertycard-contact a::attr(href)').get()
            yield response.follow(link, callback=self.get_details)
        try:
            next_page = 'https://www.nepalhomes.com/search?page=' + str(
                int(pagination.css('li.page-item.active a::text').get()) + 1)
            yield response.follow(next_page, callback=self.parse)
        except TypeError:
            pass

    def get_details(self, response):
        property_item = PropertyItem()
        price_unit = response.css('span.perData::text').get()
        if price_unit == ' ':
            price_unit = 'NA'

        property_item['ID'] = response.css('span.hash-id::text')[1].get()
        property_item['Title'] = response.css('h1.title::text').get()
        property_item['Address'] = response.css('p.location::text').get().split(',')[0]
        property_item['District'] = response.css('p.location::text').get().split(',')[1]
        property_item['Price'] = response.css('p.price::text').get()
        property_item['Price_Unit'] = price_unit
        property_item['Property_Type'] = response.css('span.span.tag.tag-gray-light.text-uppercase::text').get()
        property_item['Ad_Post_Date'] = response.css('span.posted.on::text')[1].get()
        property_item['Ad_Views'] = response.css('span.view-count::text').get()
        property_item['Agency'] = response.css('ul.list-nearby-places li h3::text').get()
        property_item['Seller'] = response.xpath('//ul[@class=\'list-nearby-places\']/li/p/text()')[1].get()
        property_item['Seller_Contact'] = response.css('a.btn.btn-email::attr(href)')[0].get()
        property_item['Seller_Email'] = response.css('a.btn.btn-email::attr(href)')[1].get()
        property_item['Link'] = response.url

        yield property_item
