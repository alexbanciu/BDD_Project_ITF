Feature: Test the search functionality in the homepage of ebay

  Background:
    Given Home page: I am on ebay homepage

  @T1 @regression @BDD
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage
    When Home page: I search for "<product_name>" from category "<category_name>"
    Then Home page: I have at least "<nr_of_results>" results returned

    @cell_phones
    Examples:
      | product_name | category_name             | nr_of_results |
      | iphone       | Cell Phones & Accessories | 1000          |
      | samsung      | Cell Phones & Accessories | 1000          |

    @electronics
    Examples:
      | product_name | category_name        | nr_of_results |
      | TV           | Consumer Electronics | 1000          |
      | LED          | Consumer Electronics | 1000          |

    @clothes
    Examples:
      | product_name | category_name                 | nr_of_results |
      | dress        | Clothing, Shoes & Accessories | 1000          |
      | sweater      | Clothing, Shoes & Accessories | 1000          |

  @T2 @functional @BDD
  Scenario Outline:  Check that the user can make an advanced search for a product
    When Home page: When I click on the advanced link
    When Advanced search page: I type "<keyword_item>" in the enter keyword textbox
    When Advanced search page: I select "<keyword_options>" from keyword options
    When Advanced search page: I select "<excluded_words>" to be excluded from search
    When Advanced search page: I choose "<category>" from the category list
    When Advanced search page: I click search button
    Then Home page: I have at least "<nr_of_results>" results returned

    Examples:
      | keyword_item | keyword_options          | excluded_words | category       | nr_of_results |
      | snowboard    | Exact words, exact order | ski            | Sporting Goods | 1000          |