from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SEARCH_TEXTBOX = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-btn')
    SEARCH_CATEGORIES = (By.ID, 'gh-cat')
    SEARCH_RESULTS = (By.XPATH, '//h1/span[@class="BOLD"][1]')
    ADVANCED_SEARCH_LINK = (By.ID, 'gh-as-td')
    # ADVANCED_SEARCH_LINK = (By.LINK_TEXT, 'Advanced')

    def navigate_to_homepage(self):
        self.chrom.get("https://www.ebay.com/")

    def insert_search_value(self, product_name):
        self.chrom.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

    def choose_category(self, category_name):
        category_dropdown = Select(self.chrom.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)

    def click_search_button(self):
        self.chrom.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self, nr_of_results):
        partial_result = self.chrom.find_element(*self.SEARCH_RESULTS).text
        result = partial_result.replace(",", "")
        assert int(result) >= int(
            nr_of_results), f'Error: Results are incorrect. Expected: {nr_of_results}, Actual: {result}'

    def click_advanced_link(self):
        self.chrom.find_element(*self.ADVANCED_SEARCH_LINK).click()