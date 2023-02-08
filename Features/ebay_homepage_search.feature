Feature: Test the search functionality in the homepage of ebay
  Background:
    Given Home page: I am on ebay homepage

  @T1 @regression @BDD
  Scenario Outline: Check that the user can make a simple search in the Ebay homepage

    When Home page: I search for "<product_name>" from category Cell Phones & Accessories
    Then Home page: I have at least 1000 results returned
    Examples:
      | product_name | category_name                 | nr_of_results |
      | iphone       | Cell Phones & Accessories     | 1000          |
      | TV           | Consumer Electronics          | 1200000       |
      | sweater      | Clothing, Shoes & Accessories | 1800000       |

  @T2 @functional @BDD
  Scenario: Check that the user can make an advanced search for a product
      When Home page: When I click on the advanced link
      And Advanced search page: I type pampers in the keyword textbox
      * Advanced search page: I choose exact words, exact order from keyword options
      And Advanced search page: I click search button
      Then Home page: I have at least 1200 results returned