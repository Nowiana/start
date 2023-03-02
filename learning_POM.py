from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    loc_select_product_1 = "//button[@id='add-to-cart-sauce-labs-backpack']"
    loc_select_product_2 = "//button[@id='add-to-cart-sauce-labs-bike-light']"
    loc_select_product_3 =  "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    loc_cart = "//div[@id='shopping_cart_container']"
    loc_menu = "//button[@id='react-burger-menu-btn']"
    loc_menu_about = "//a[@id='about_sidebar_link']"


    # Getters
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_cart)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_menu)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.loc_menu_about)))

    # actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("click add cart product 1 ")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("click add cart product 2 ")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("click add cart product 3 ")

    def click_cart(self):
        self.get_cart().click()
        print("click cart")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("click menu_button")

    def click_about_button(self):
        self.get_about_button().click()
        print("click about_button")

    # methods
    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.assert_url("https://saucelabs.com/")




