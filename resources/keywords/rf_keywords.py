#keywords for robot framework
from tests.helper_action import SiteHelper
from robot.api.deco import keyword


class RobotFrameworkKeywords:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self.e_commerce_html = "https://www.emag.ro"
        self.helper = SiteHelper()

    @keyword('Open e-commerce website')
    def open_site_html(self):
        self.helper.open_ecomerce_main_page(self.e_commerce_html)

    @keyword('Maximize web browser')
    def max_web_browser(self):
        self.helper.maximize_browser()

    @keyword('Close entire browser')
    def exit_browser(self):
        self.helper.close_browser()

    @keyword('user clicks category item')
    def click_cat_item(self, category_name):
        self.helper.click_category(category_name)
        
    @keyword('user click laptop subcategory name')
    def click_laptop_subcategory_name(self):
        self.helper.click_laptop_subcategory()
        
    @keyword('user clicks laptop link')
    def click_laptop_link(self):
        self.helper.click_laptop_link()
        
    @keyword('user clicks sort button')
    def sort_button_click(self):
        self.helper.click_sort_button()
    
    @keyword('user selects descending order')
    def click_descending_order(self):
        self.helper.click_descending_order()
    
    @keyword('user accept cookie preferences')
    def accept_cookies(self):
        self.helper.close_preference_by_accepting()
        
    @keyword('user closes login popup')
    def close_login_popup(self):
        self.helper.close_login_button()
        
    @keyword('user scrolls to the add to cart button for preferred item')
    def scroll_to_add_to_cart(self, found_index=1):
        self.helper.scroll_to_add_to_cart(found_index)
    
    @keyword('user clicks add to cart button for the chosen item')
    def click_add_to_cart_button_on_item(self, found_index=1):
        self.helper.click_add_button_to_cart(found_index)

    @keyword('user closes popup modal')
    def click_close_modal(self):
        self.helper.post_add_popup_close()

    @keyword('user verifies number of items in cart')
    def verify_number_of_items_in_cart(self, expected_count):
        self.helper.verify_number_of_items_in_cart(expected_count)
        
        