#contains locators for the main page and search result page


class MainPage:

    category_menu = 'megamenu-list-department__department-name'
    subcategory_menu = "//a[@href='/laptopuri-accesorii/sd?tree_ref=2&ref=dep_cat_tree_15']"
    laptops_link = "//a[@href='/laptopuri/c?tree_ref=2172&ref=cat_tree_91']"
    sort_button = "//div[@class='sort-control-btn-dropdown hidden-xs']"
    descending_order = "//a[@href='/laptopuri/sort-pricedesc/c']"
    add_to_cart_button = "//*[text()='Adauga in Cos']"
    accept_preferences_button = "//button[@class ='btn btn-primary js-accept gtm_h76e8zjgoo btn-block']"
    login_modal_close_button = "//button[@class='js-dismiss-login-notice-btn dismiss-btn btn btn-link pad-sep-none pad-hrz-none']"
    extra_info_modal = "//div[@class='modal-content']"
    extra_info_close_button = "//i[@class='em em-close gtm_6046yfqs']"
    extra_info_back_button = "//a[@class='btn btn-default btn-sm btn-block gtm_fewwqqtnc']"
    cart_item_count = "//span[@class='jewel jewel-danger']"

    def __init__(self):
        pass
