from browser import Browser
from Pages.ebay_homepage import HomePage
from Pages.ebay_advanced_search_page import AdvancedSearchPage


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()
    context.advanced_search_object = AdvancedSearchPage()
    #  * beefore_all este o metoda recunoscuta de libraria behave si care se
    #  va executa inainte de toate testele
    #  * context este ca o cutiuta in care vom stoca toate atributele ce pot fi folosite in alte fisiere


def after_all(context):
    context.browser.close()
    # * after_all este o metoda recunoscuta de libraria behave si care se
    #     #  va executa dupa de toate testele