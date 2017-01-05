from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.load_extension('criteo')


fg.title('Your Website')
fg.link(href='http://www.yoursite.com/us/', rel='alternate')
fg.description('Your Website')


fe = fg.add_entry()

fe.id('myproductid')
fe.title('Working Boots Size 7.5')
fe.description('Excellent for daily use')
fe.criteo.google_product_category('Womens Shoes Working Boots')


print(fg.rss_str(pretty=True))
