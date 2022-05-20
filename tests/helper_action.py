from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from robot.api import logger

from pages.main_page import MainPage


class SiteHelper:

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def close_browser(self):
        """
        Closes entire browser
        """
        self.driver.quit()

    def open_ecomerce_main_page(self, html):
        """
        Opens the web browser to the specific page and maximizes browser
        """
        self.driver.get(html)

    def maximize_browser(self):
        """
        Maximizes browser page
        """
        self.driver.maximize_window()

    def click_category(self, category_name):
        """
        :param category_name: nam of the product category that will be clicked
        """
        if category_name == 'Laptops':
            laptop_category = self.driver.find_elements_by_class_name(MainPage().category_menu)
            laptop_category[1].click()

    def click_laptop_subcategory(self):
        """
        Clicks the laptop subcategory
        """
        subcategory_button = self.driver.find_element_by_xpath(MainPage().subcategory_menu)
        subcategory_button.click()

    def click_laptop_link(self):
        """
        Clicks the laptop link
        """
        laptops_link = self.driver.find_element_by_xpath(MainPage().laptops_link)
        laptops_link.click()

    def click_sort_button(self):
        """
        Clicks the sort dropdown menu
        """
        sort_dropdown = self.driver.find_element_by_xpath(MainPage().sort_button)
        sort_dropdown.click()

    def click_descending_order(self):
        """
        Clicks the descending order menu element
        """
        desc_order_element = self.driver.find_element_by_xpath(MainPage().descending_order)
        desc_order_element.click()

    def get_add_buttons_to_cart(self):
            """
            The logic here is that only in stoc elements have "add item to cart" as a button name
            :return: a list of all the "add item to cart buttons"
            """
            return self.driver.find_elements_by_xpath(MainPage().add_to_cart_button)

    def click_add_button_to_cart(self, found_index=0):
        """
        Clicks one of the add to cart buttons depending on it's found index
        :param found_index: index of the element that's to be found
        """
        self.get_add_buttons_to_cart()[found_index].click()

    def close_preference_by_accepting(self):
        """
        Closes Accept cookie preferences modal
        """
        if self.driver.find_element_by_xpath(MainPage().accept_preferences_button).is_displayed():
            self.driver.find_element_by_xpath(MainPage().accept_preferences_button).click()

    def scroll_to_add_to_cart(self, found_index=0):
        """
        Scrolls moves to the add to cart element that will be clicked
        :param found_index: index of the add to cart element that will be added to cart
        """
        add_to_cart_button = self.get_add_buttons_to_cart()[found_index]
        self.actions.move_to_element(add_to_cart_button)
        self.actions.perform()

    def close_login_button(self):
        """
        closes login popup modal
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, MainPage().login_modal_close_button)))
        self.driver.find_element_by_xpath(MainPage().login_modal_close_button).click()

    def post_add_popup_close(self):
        """
        A modal pops up after an item was added to cart.
        This method closes that modal
        Two types of close options can appear: A close button or a back button
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, MainPage().extra_info_modal)))
        if self.driver.find_element_by_xpath(MainPage().extra_info_close_button).is_displayed():
            self.driver.find_element_by_xpath(MainPage().extra_info_close_button).click()
        else:
            self.driver.find_element_by_xpath(MainPage().extra_info_back_button).click()

    def verify_number_of_items_in_cart(self, expected_number_of_items: int):
        """
        Verifies the number of items in the cart
        :param expected_number_of_items: how many items are in the cart
        """
        number_of_items_in_cart = int(self.driver.find_element_by_xpath(MainPage().cart_item_count).text)
        if number_of_items_in_cart != expected_number_of_items:
            raise AssertionError(f'The number of items in the cart is expected to be {expected_number_of_items}\n'
                        f'The actual number of items in the cart is: {number_of_items_in_cart}!')
        else:
            logger.info('The expected number of items in the cart was found.')


if '__main__' == __name__:
    # I'm intentionally leaving this debug code here
    # I know the methods self.driver.find_element_by_xpath is being depracated. They would be changed down the line.
    sh = SiteHelper()
    sh.open_ecomerce_main_page('https://www.emag.ro')
    sh.click_category('Laptops')
    sh.click_laptop_subcategory()
    sh.click_laptop_link()
    sh.click_sort_button()
    sh.click_descending_order()
    sh.close_preference_by_accepting()
    sh.close_login_button()
    sh.scroll_to_add_to_cart(0)
    sh.click_add_button_to_cart(0)
    sh.post_add_popup_close()
    sh.scroll_to_add_to_cart(1)
    sh.click_add_button_to_cart(1)
    sh.post_add_popup_close()
    sh.verify_number_of_items_in_cart(2)
    sh.close_browser()

