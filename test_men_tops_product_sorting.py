from men_tops_page import MenTops

TOPS_MEN_PAGE = 'https://magento.softwaretestingboard.com/men/tops-men.html'

class TestMenTopsPage:

    # TC_008.006.001 | Tops Page > items amount on the Page and common items amount 
    # > Checking the quantity of items in the grid view

    def test_quantity_of_items_in_grid_view(self,driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert len(page.get_product_names()) == 12, "Quantity of items less than 12 in grid view"

    # TC_008.006.002 | Tops Page > items amount on the Page and common items amount 
    # > Checking the quantity of items in the list view

    def test_quantity_of_items_in_list_view(self,driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_list_mode()
        assert len(page.get_product_names()) == 10, "Quantity of items less than 10 in list view"

    
    # TC_008.007.001 | Tops Page > sort Items by: Position, Product Name and Price 
    # > Checking sorting items by Product Name ASC(A-Z)

    def test_sorting_items_by_Product_Name_ASC(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.select_sorter('Product Name')
        actual = [el.text for el in page.get_product_names()]
        expected = sorted(actual)
        
        assert actual == expected, "Product Names are not sorted A-Z"


    # TC_008.007.002 | Tops Page > sort Items by: Position, Product Name and Price 
    # > Checking sorting items by Product Name DESC(Z-A)

    def test_sorting_items_by_Product_Name_DESC(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.select_sorter('Product Name')
        page.click_arrow()
        actual = [el.text for el in page.get_product_names()]
        expected = sorted(actual, reverse=True)
        
        assert actual == expected, "Product Names are not sorted Z-A"

    # TC_008.007.003 | Tops Page > sort Items by: Position, Product Name and Price 
    # > Checking sorting items by Price ASC(0-9)

    def test_sorting_items_by_Price_ASC(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.select_sorter('Price')
        actual = [float(el.text[1:]) for el in page.get_price()]
        expected = sorted(actual)
        
        assert actual == expected, "Price are not sorted 0-9"

    # TC_008.007.004 | Tops Page > sort Items by: Position, Product Name and Price 
    # > Checking sorting items by Price DESC(9-0)
    
    def test_sorting_items_by_Price_DESC(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.select_sorter('Price')
        page.click_arrow()
        actual = [float(el.text[1:]) for el in page.get_price()]
        expected = sorted(actual, reverse=True)
        
        assert actual == expected, "Price are not sorted 9-0"
