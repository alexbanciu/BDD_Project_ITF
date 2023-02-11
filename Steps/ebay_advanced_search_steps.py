from behave import *


@when('Advanced search page: I type "{keyword_item}" in the enter keyword textbox')
def step_impl(context, keyword_item):
    context.advanced_search_object.enter_keywords_or_item_number(keyword_item)


@when('Advanced search page: I select "{keyword_options}" from keyword options')
def step_impl(context, keyword_options):
    context.advanced_search_object.select_keyword_options(keyword_options)


@when('Advanced search page: I select "{excluded_words}" to be excluded from search')
def step_impl(context, excluded_words):
    context.advanced_search_object.exclude_words_from_search(excluded_words)


@when('Advanced search page: I choose "{category}" from the category list')
def step_impl(context, category):
    context.advanced_search_object.select_search_category(category)


@when('Advanced search page: I click search button')
def step_impl(context):
    context.advanced_search_object.click_search_button()