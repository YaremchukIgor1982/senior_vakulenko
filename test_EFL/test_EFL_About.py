from pprint import pprint

from parsel import Selector



dev = 'https://endlessfrontierlabs.com/about/'
def test_mentors(rest):
   page=  rest.get_data(dev).text
   sel = Selector(text=page)
   item = sel.css(".flickity-slider").css(".cell").getall()
   for i in item:
      sel2 = Selector(i)
      name = sel2.css(".nectar-button").css('h2::text').get()
      primary = sel2.css(".nectar-button").css("p::text").get()
      port = sel2.css('a::attr(href)').get()

      pprint({'mentor_url':port,"name":name,"category":primary})