from pprint import pprint

dev = 'https://endlessfrontierlabs.com/'
def test_FAQ(app):
    app.open(dev + '/faq/')
    tabs = [app.efl.click_to_open_and_get_FaqItem_Info_close(p, t) for t in app.efl.table_FAQ() for p in
            app.efl.sub_table_FAQ(t)]
    pprint(tabs)