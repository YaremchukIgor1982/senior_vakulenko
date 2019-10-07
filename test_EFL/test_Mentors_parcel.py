from pprint import pprint

from parsel import Selector

from data.app_data import htaccess

dev = 'efl-dev.smashedmedia.guru/mentors'
def test_mentors(rest):
   page=  rest.get_data(htaccess + dev).text
   sel = Selector(text=page)
   item = sel.css(".portfolio-wrap").css(".work-item").getall()
   for i in item:
      sel2 = Selector(i)
      name = sel2.css(".work-info").css('h3::text').get()
      primary = sel2.css(".work-info").css("span.primary-category::text").get()
      port = sel2.css('a::attr(href)').get()

      pprint({'mentor_url':port,"name":name,"category":primary})
# def test_Mentors_pics(rest):
#    page = rest.get_data(htaccess + dev).text
#    sel = Selector(text=page)
#    item = sel.css(".portfolio-wrap").css(".work-item").getall()
#    for i in item:
#       sel2 = Selector(i)
#       name = sel2.css(".work-info").css('h3').get()