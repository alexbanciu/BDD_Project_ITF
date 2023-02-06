from browser import Browser
from Pages.ebay_homepage import HomePage


def before_all(context):
    # * before_all este o metoda recunoscuta de libraria behave si care se va executa inainte de toate testele
    # * context este o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere
    context.browser = Browser()
    context.home_page_object = HomePage()


def after_all(context):
    context.browser.close()