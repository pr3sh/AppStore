

from scrapy import Request

class AppStoreSpider(Spider):
    
    name = 'appstore_spider'
    start_urls = ['https://apps.apple.com/lr/genre/ios-entertainment/id6016']
    allowed_urls= ['https://apps.apple.com/lr/genre/ios/id36']
    
    def parse(self, response):
        
        urls = response.xpath('//div[@id="selectedcontent"]//li/a/@href').extract()

        for url in result_urls:
			yield Request(url=url, callback=self.parse_page)





        App =AppStoreSpider()

        Names = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract()  #List of all names in the app store
	    




	    Provider  = App.xpath('//dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()').extract() 
	    

	    Size = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    Category = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    Compatibility= App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    Languages = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    Age_Rating = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    Price = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 
	    App_Rating = App.xpath('//div[@id="selectedcontent"]//li/a/text()').extract() 



response.xpath('//dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()').extract() 