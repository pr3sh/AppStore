

from scrapy import Request, Spider
from AppStore.items import AppStoreItem
import re

class AppStoreSpider(Spider):
    
    name = 'appstore_spider'

    #entertainment, finance, news, health-fitness,productivity,travel,medical,shopping,books,business
    #Food&Drink, lifestyle, magazine and newspaper,games, navigation, photo&video,reference,social networking
    # sports,weather, utilities


    start_urls = ['https://apps.apple.com/lr/genre/ios-entertainment/id6016','https://apps.apple.com/us/genre/ios-finance/id6015',
    'https://apps.apple.com/us/genre/ios-news/id6009','https://apps.apple.com/us/genre/ios-health-fitness/id6013',
    'https://apps.apple.com/us/genre/ios-productivity/id6007','https://apps.apple.com/us/genre/ios-travel/id6003',
    'https://apps.apple.com/us/genre/ios-medical/id6020','https://apps.apple.com/us/genre/ios-shopping/id6024',
    'https://apps.apple.com/us/genre/ios-books/id6018','https://apps.apple.com/us/genre/ios-business/id6000',
    'https://apps.apple.com/us/genre/ios-food-drink/id6023','https://apps.apple.com/us/genre/ios-lifestyle/id6012',
    'https://apps.apple.com/us/genre/ios-magazines-newspapers/id6021','https://apps.apple.com/us/genre/ios-games/id6014',
    'https://apps.apple.com/us/genre/ios-navigation/id6010','https://apps.apple.com/us/genre/ios-photo-video/id6008',
    'https://apps.apple.com/us/genre/ios-reference/id6006','https://apps.apple.com/us/genre/ios-social-networking/id6005',
    'https://apps.apple.com/us/genre/ios-sports/id6004','https://apps.apple.com/us/genre/ios-utilities/id6002',
    'https://apps.apple.com/us/genre/ios-weather/id6001']
    

    allowed_urls= ['https://apps.apple.com/lr/genre/ios/id36']
    
    def parse(self, response):
        
        urls = response.xpath('//div[@id="selectedcontent"]//li/a/@href').extract()

        for url in urls:
            yield Request(url=url, callback=self.parse_page)

    def parse_page(self,response):

        #List of all names in the app store
        name = response.xpath('//h1[@class="product-header__title app-header__title"]/text()').extract_first().strip()
        rows = response.xpath('//div[@class="information-list__item l-row"]')

        info_dict = {}

        for row in rows:
            try:
                key = row.xpath('./dt/text()').extract_first().strip()
            except:
                continue

            try:
                value = row.xpath('./dd/text()').extract_first().strip()
            except:
                continue
                
            info_dict[key] = value
        
        # provider  = App.xpath('//dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()').extract() 
        # size = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
        # category = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
        # compatibility= App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
        # languages = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
        # age_rating = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
        # price = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract()
        try:   
            app_rating = float(response.xpath('//span[@class="we-customer-ratings__averages__display"]/text()').extract_first())
        except:
            app_rating = None

        try:
            rating_count =  response.xpath('//p[@class="we-customer-ratings__count medium-hide"]/text()').extract_first()
        except:
            rating_count = ''

        try:
            rank = response.xpath('//li[@class ="inline-list__item"]/text()').extract_first().strip()
            rank = int(re.findall('\d+', rank)[0])
        except:
            rank = None

        
        size = rows[1].xpath('./dd/text()').extract_first()
        category = rows[2].xpath('./dd/a/text()').extract_first()
        compatibility = rows[3].xpath('./dd//p/text()').extract_first().strip()
        languages = rows[4].xpath('./dd//p/text()').extract_first()
        age_rating = rows[5].xpath('./dd/text()').extract_first()

        app = AppStoreItem()

        app['name'] = name
        # app['seller'] = info_dict['Seller'] 
        app['category'] = category
        app['languages'] = languages
        app['compatibility'] = compatibility
        app['app_rating'] = app_rating
        app['rating_count'] = rating_count
        app['rank'] = rank
        app['price'] = info_dict["Price"]
        app['age_rating'] = age_rating
        app['size'] = size

        yield app




