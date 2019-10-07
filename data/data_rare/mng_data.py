# -*- coding: utf-8 -*-
from faker import Faker


class Faker:
    faker = Faker()
    name_long = 'test_' + faker.word(ext_word_list=None)
    last_name_chaotic = faker.random_letters(length=5)
    mail_stupid = faker.word(ext_word_list=None) + '@mail.mail'


url = 'https://moroccangoldseries.com/'

seo_links_redirects_path ="C:\\Users\\Administrator\\Downloads\\MGS Meta Data.xlsx"
mng_urls = {
    'http://moroccangoldseries.com/press/',
    'http://moroccangoldseries.com/what-is-new/',
    'http://moroccangoldseries.com/shop.html/',

     'hmoroccangoldseries.com/all-products.html/',
     'http:/moroccangoldseries.com/shampoo.html/',
     'http:/moroccangoldseries.com/mask.html/',
     'http:/moroccangoldseries.com/treatment.html/',
     'http:/moroccangoldseries.com/styling-finishing.html/',
     'http:/moroccangoldseries.com/fine.html/',
     'http:/moroccangoldseries.com/dry-normal-to-thick.html/',
     'http:/moroccangoldseries.com/wavy-curly.html/',
    'http://moroccangoldseries.com/the-moroccan-way/'
}

items = ['Shampoo',
         'Trave',
         'Salt',
         'Leave-In Mask ',
         'Volumizing Moisture Mask ',
         'Curl Cream '
         ]

pwd = 'Test123#'

logged = [
    'rebeccanash@butler.com',
    'brooke42@hotmail.com',
    'uthomas@gmail.com',
     'wvaughn@hotmail.com'

]

migrate = [
        'catalog/category/view/s/root-category/id/12/',
        'shampoo.html',
        'whats-new.html',
        'quickshop/index/view/path/treatment-mask-50.html',
        'styling-finishing.html',

        'mask.html',
        'treatment.html',
        'catalog/category/view/id/26/?hair_type=9',
        'dry-normal-to-thick.html',
        'wavy-curly.html',
        'catalog/category/view/id/28/?hair_type=8',
        'fine.html',
        'quickshop/index/view/path/travel-kit-26.html',
        'travel-kit-26.html',
        'quickshop/index/view/path/argan-oil-34.html',
        'argan-oil-35.html',
        'quickshop/index/view/path/volumizing-moisture-mask-39.html',
        'quickshop/index/view/path/treatment-mask-34.html',
        'volumizing-moisture-mask-40.html',
        'treatment-mask-52.html',
        'treatment-mask-250ml.html',
        'quickshop/index/view/path/salt-free-shampoo-45.html',
        'salt-free-shampoo-46.html',
        'quickshop/index/view/path/moisturizing-style-cream-48.html',
        'moisturizing-style-cream-49.html',
        'quickshop/index/view/path/curl-cream-51.html',
        'curl-cream-52.html',
        'quickshop/index/view/path/curl-cream-149.html',
        'quickshop/index/view/path/leave-in-mask-56.html',
        'leave-in-mask-57.html',
        'leave-in-mask-125ml.html',
        'terms-and-conditions',
        'golden-tips/about-argan-oil.html',
        'the-moroccan-way',
        'rss/',
        'catalogsearch/term/popular/',
        'privacy-policy',
        'behind-the-brand',
        'customer/account/forgotpassword/',
        'sales/guest/form/',
        'catalogsearch/advanced/',
        'customer/account/login/',
        'customer/account/create',
        'customer/account/',
        'checkout/cart',
        'wishlist/',
        'blog/index/index/limit/4/?page=3',
        'golden-tips/why-should-you-use-argan-oil-in-your-hair.html',
        'golden-tips',
        'golden-tips/golden-hair-essentials.html',
        'golden-tips/is-salt-bad-for-your-hair.html',
        'blog/index/index/limit/4/?page=2',
        'golden-tips/the-best-argan-oil-products-for-your-hair.html',
        'golden-tips/the-ultimate-guide-to-using-moroccan-argan-oil-for-hair.html',
        'golden-tips/5-benefits-of-argan-oil-hair-products.html',
        'golden-tips/is-argan-oil-good-for-your-hair.html',
        'golden-tips/how-to-fix-damaged-hair-argan-oil-hair-products.html',

        'golden-tips/about-argan-oil.html',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS90aGUtbW9yb2NjYW4td2F5/',
        'quickshop/index/view/path/leave-in-mask.html',
        'quickshop/index/view/path/curl-cream.html',
        'quickshop/index/view/path/salt-free-shampoo.html',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS90cmVhdG1lbnQuaHRtbC8,/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS8,/',
        'contacts/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS9kcnktbm9ybWFsLXRvLXRoaWNrLmh0bWwvP2hhaXJfdHlwZT05JmFtcDttb2RlPWdyaWQ,/',
        'quickshop/index/view/path/volumizing-moisture-mask-131.html',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS9maW5lLmh0bWwv/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS9nb2xkZW4tdGlwcy9ob3ctdG8tZml4LWRhbWFnZWQtaGFpci1hcmdhbi1vaWwtaGFpci1wcm9kdWN0cy5odG1s/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS90cmVhdG1lbnQuaHRtbC8_aGFpcl90eXBlPTkmYW1wO21vZGU9bGlzdA,,/',
        'quickshop/index/view/path/treatment-mask-234.html',
        'quickshop/index/view/path/moisturizing-style-cream-139.html',
        'quickshop/index/view/path/salt-free-shampoo-136.html',
        'quickshop/index/view/path/travel-kit-161.html',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS90cmF2ZWwta2l0LTE5Ni5odG1s/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS9tYXNrLmh0bWwvP2hhaXJfdHlwZT04JmFtcDttb2RlPWxpc3Q,/',
        'catalog/product_compare/index/uenc/aHR0cHM6Ly93d3cubW9yb2NjYW5nb2xkc2VyaWVzLmNvbS93YXZ5LWN1cmx5Lmh0bWwvP2hhaXJfdHlwZT04JmFtcDttb2RlPWxpc3Q,/',
        'curl-cream-177.html',
        'treatment-mask-300.html',
        'argan-oil-163.html',
        'moisturizing-style-cream-174.html',
        'leave-in-mask-187.html',
        'travel-kit-196.html',
        'salt-free-shampoo-171.html'
        'sitemap.xml',
        'all-products.html',

]