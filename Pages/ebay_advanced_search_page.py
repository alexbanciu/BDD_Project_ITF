from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.XPATH, '//*[@id="_nkw"]')
    KEYWORD_OPTIONS = (By.XPATH, '//*[@id="s0-1-17-4[0]-7[1]-_in_kw"]')
    EXCLUDE_WORDS_FROM_SEARCH = (By.XPATH, '//*[@id="_ex_kw"]')
    SEARCH_CATEGORIES = (By.XPATH, '//*[@id="s0-1-17-4[0]-7[3]-_sacat"]')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[3]/div/main/form/fieldset[1]/div[5]/button')

    def enter_keywords_or_item_number(self, keyword_item):
        self.chrom.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys(keyword_item)

    def select_keyword_options(self, keyword_option):
        keyword_options_dropdown = Select(self.chrom.find_element(*self.KEYWORD_OPTIONS))
        keyword_options_dropdown.select_by_visible_text(keyword_option)

    def exclude_words_from_search(self, excluded_words):
        self.chrom.find_element(*self.EXCLUDE_WORDS_FROM_SEARCH).send_keys(excluded_words)

    def select_search_category(self, category):
        category_dropdown = Select(self.chrom.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category)

    def click_search_button(self):
        self.chrom.find_element(*self.SEARCH_BUTTON).click()