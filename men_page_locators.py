from selenium.webdriver.common.by import By


class MenPageLocators:
    MEN_TOPS_GRID = (By.XPATH, "//div[2]/div[1]/strong[2]")


class MenCategoryPageLocators:
    @staticmethod
    def get_position_cart(position):
        return By.CSS_SELECTOR, f"li[class = 'item product product-item']:nth-child({position})"

    @staticmethod
    def get_position_button(position):
        return By.CSS_SELECTOR, f"li[class = 'item product product-item']:nth-child({position}) button"

    @staticmethod
    def get_product_image(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position})"

    @staticmethod
    def get_option_locator(option):
        return By.XPATH, f'(//option[@value="{option}"])[2]'




