*** Settings ***
#Library  ../resources/helpers/helper_action.py
#Resource  ../resources/helpers/helper_action.py
#Test Setup  Open and maximize browser
#Test Teardown  Close entire browser
Library  helper_action.py
Resource  helper_action.py


*** Test Cases ***
Add two most expensive items from a certain category
    [Documentation]  Email received on May 16 2022
    user clicks category item   Laptops
    user click laptop subcategory name
    And user clicks laptop link
    And user clicks sort button
    And user selects descending order
    And user accept cookie preferences
    And user closes login popup
    And user scrolls to the add to cart button for preferred item  0
    And user clicks add to cart button for the chosen item  0
    And user closes popup modal
    And user clicks add to cart button for the chosen item  1
    And user closes popup modal
    Then user verifies number of items in cart  2

*** Keywords ***
Open and maximize browser
    Open e-commerce website
    Maximize web browser

Close browser
    Close entire browser