import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_for_portal(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        elem = driver.find_element(By.ID, "store_nav_search_term")
        elem.click()
        elem.send_keys("portal")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertNotIn("0 results match your search.", driver.page_source)

    def test_search_for_nonexistentvalue(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        elem = driver.find_element(By.ID, "store_nav_search_term")
        elem.click()
        elem.send_keys("nonexistentvalue")
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        self.assertIn("0 results match your search.", driver.page_source)

    def test_home_tabs_trending(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")

        trending_tab = driver.find_element(By.ID, "tab_newreleases_content_trigger")
        trending_tab_classes = trending_tab.get_attribute("class")
        self.assertIn("active", trending_tab_classes.split())

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab_classes = top_tab.get_attribute("class")
        self.assertNotIn("active", top_tab_classes.split())

        popular_tab = driver.find_element(By.ID, "tab_upcoming_content_trigger")
        popular_tab_classes = popular_tab.get_attribute("class")
        self.assertNotIn("active", popular_tab_classes.split())

        specials_tab = driver.find_element(By.ID, "tab_specials_content_trigger")
        specials_tab_classes = specials_tab.get_attribute("class")
        self.assertNotIn("active", specials_tab_classes.split())

    def test_home_tabs_top(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab.click()
        top_tab_classes = top_tab.get_attribute("class")
        self.assertIn("active", top_tab_classes.split())

        trending_tab = driver.find_element(By.ID, "tab_newreleases_content_trigger")
        trending_tab_classes = trending_tab.get_attribute("class")
        self.assertNotIn("active", trending_tab_classes.split())

        popular_tab = driver.find_element(By.ID, "tab_upcoming_content_trigger")
        popular_tab_classes = popular_tab.get_attribute("class")
        self.assertNotIn("active", popular_tab_classes.split())

        specials_tab = driver.find_element(By.ID, "tab_specials_content_trigger")
        specials_tab_classes = specials_tab.get_attribute("class")
        self.assertNotIn("active", specials_tab_classes.split())

    def test_home_tabs_popular(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")

        popular_tab = driver.find_element(By.ID, "tab_upcoming_content_trigger")
        popular_tab.click()
        popular_tab_classes = popular_tab.get_attribute("class")
        self.assertIn("active", popular_tab_classes.split())

        trending_tab = driver.find_element(By.ID, "tab_newreleases_content_trigger")
        trending_tab_classes = trending_tab.get_attribute("class")
        self.assertNotIn("active", trending_tab_classes.split())

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab_classes = top_tab.get_attribute("class")
        self.assertNotIn("active", top_tab_classes.split())

        specials_tab = driver.find_element(By.ID, "tab_specials_content_trigger")
        specials_tab_classes = specials_tab.get_attribute("class")
        self.assertNotIn("active", specials_tab_classes.split())

    def test_home_tabs_specials(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")

        specials_tab = driver.find_element(By.ID, "tab_specials_content_trigger")
        specials_tab.click()
        specials_tab_classes = specials_tab.get_attribute("class")
        self.assertIn("active", specials_tab_classes.split())

        trending_tab = driver.find_element(By.ID, "tab_newreleases_content_trigger")
        trending_tab_classes = trending_tab.get_attribute("class")
        self.assertNotIn("active", trending_tab_classes.split())

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab_classes = top_tab.get_attribute("class")
        self.assertNotIn("active", top_tab_classes.split())

        popular_tab = driver.find_element(By.ID, "tab_upcoming_content_trigger")
        popular_tab_classes = popular_tab.get_attribute("class")
        self.assertNotIn("active", popular_tab_classes.split())

    def test_language_localization(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        language_dropdown = driver.find_element(By.ID, "language_pulldown")
        language_dropdown.click()
        german = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[1]/div/div[3]/div/div/div/a[9]")
        german.click()
        time.sleep(5)
        self.assertEqual(driver.title, "Willkommen bei Steam!")

    def test_footer_links(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        time.sleep(5)
        cookie_button = driver.find_element(By.ID, "rejectAllButton")
        cookie_button.click()
        footer_links = driver.find_elements(By.CSS_SELECTOR, ".valve_links a")
        link_text = ["About Us - Valve Corporation", "Valve Corporation", "Steamworks", "Steamworks Partner Program", "Steam Support", "Steam Gift Cards", "Steam", "X"]

        for i in range(len(footer_links)):
            if i != 4 and i != 5:
                footer_links[i].click()
                time.sleep(2)
                tabs = driver.window_handles
                driver.switch_to.window(tabs[1])
                # 6 asercji w pętli
                time.sleep(2)
                self.assertIn(link_text[i], driver.title)
                driver.close()
                driver.switch_to.window(tabs[0])

    def test_your_store_dropdown(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        for_you_button = driver.find_element(By.ID, "foryou_tab")
        hover = ActionChains(driver).move_to_element(for_you_button)
        hover.perform()
        dropdown_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/a")
        element_contents = ["Home", "Community Recommendations", "Recently Viewed", "Steam Curators"]
        for i in range(len(dropdown_elements)):
            # 4 asercje w pętli
            self.assertEqual(dropdown_elements[i].text, element_contents[i])

    def test_new_and_noteworthy_dropdown_first_column(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        for_you_button = driver.find_element(By.ID, "noteworthy_tab")
        hover = ActionChains(driver).move_to_element(for_you_button)
        hover.perform()
        dropdown_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[5]/div/div[1]/a")
        element_contents = ["Top Sellers", "Most Played", "New Releases", "Upcoming Releases", "Recently Updated"]
        for i in range(len(dropdown_elements)):
            # 5 asercji w pętli
            self.assertEqual(dropdown_elements[i].text, element_contents[i])

    def test_new_and_noteworthy_dropdown_second_column(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        for_you_button = driver.find_element(By.ID, "noteworthy_tab")
        hover = ActionChains(driver).move_to_element(for_you_button)
        hover.perform()
        dropdown_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/div[5]/div/div[2]/a")
        element_contents = ["Special Offers", "Sale Events", "Steam Year In Review", "Steam Next Fest", "The Steam Awards"]
        for i in range(len(dropdown_elements)):
            # 5 asercji w pętli
            self.assertEqual(dropdown_elements[i].text, element_contents[i])

    def test_sidebar_recommended(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        sidebar_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div[1]/div[4]/a")
        element_contents = ["By Friends", "By Curators", "Tags"]
        for i in range(len(sidebar_elements)):
            self.assertEqual(sidebar_elements[i].accessible_name, element_contents[i])

    def test_sidebar_categories(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        sidebar_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div[1]/div[6]/a")
        element_contents = ["Top Sellers", "New Releases", "Upcoming", "Specials", "VR Titles", "Controller-Friendly", "Great on Deck"]
        for i in range(len(sidebar_elements)):
            self.assertEqual(sidebar_elements[i].accessible_name, element_contents[i])

    def test_sidebar_genre(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        sidebar_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[1]/div/div[2]/a")
        element_contents = ["Free to Play", "Early Access", "Action", "Adventure", "Casual", "Indie", "Massively Multiplayer", "Racing", "RPG", "Simulation", "Sports", "Strategy"]
        for i in range(len(sidebar_elements)):
            self.assertEqual(sidebar_elements[i].accessible_name, element_contents[i])

    def test_supernav(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        supernav_elements = driver.find_elements(By.CSS_SELECTOR, ".supernav a")
        element_contents = ["STORE", "COMMUNITY", "ABOUT", "SUPPORT"]
        for i in range(len(supernav_elements)):
            # 4 asercje w pętli
            self.assertEqual(supernav_elements[i].text, element_contents[i])

    def test_supernav_store(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        store_button = driver.find_element(By.CSS_SELECTOR, "a.supernav:nth-child(1)")
        hover = ActionChains(driver).move_to_element(store_button)
        hover.perform()
        store_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[1]/div/div[2]/div[1]/div/a")
        element_contents = ["Home", "Discovery Queue", "Wishlist", "Points Shop", "News"]
        for i in range(len(store_elements)):
            # 5 asercji w pętli
            self.assertEqual(store_elements[i].text, element_contents[i])

    def test_supernav_community(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        community_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[1]/div/div[2]/a[2]")
        hover = ActionChains(driver).move_to_element(community_button)
        hover.perform()
        community_elements = driver.find_elements(By.XPATH, "/html/body/div[1]/div[7]/div[1]/div/div[2]/div[2]/div/a")
        element_contents = ["Home", "Discussions", "Workshop", "Market", "Broadcasts"]
        for i in range(len(community_elements)):
            # 5 asercji w pętli
            self.assertEqual(community_elements[i].text, element_contents[i])

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab.click()
        item = driver.find_element(By.CSS_SELECTOR, "div.tab_content_items:nth-child(3) > a:nth-child(1)")
        item.click()
        time.sleep(3)
        cookie_button = driver.find_element(By.ID, "rejectAllButton")
        cookie_button.click()
        time.sleep(1)
        add_to_cart_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[7]/div[6]/div[3]/div[2]/div[1]/div[5]/div[2]/div[2]/div[1]/div/div[2]/div/div[2]")
        add_to_cart_button.click()
        time.sleep(2)
        go_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button.DialogButton:nth-child(2)")
        go_to_cart_button.click()
        time.sleep(3)
        self.assertNotIn("Your cart is empty.", driver.page_source)

    def test_steam_login(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        time.sleep(3)
        cookie_button = driver.find_element(By.ID, "rejectAllButton")
        cookie_button.click()

        login_button = driver.find_element(By.CSS_SELECTOR, "a.global_action_link")
        login_button.click()
        time.sleep(10)

        username_field = driver.find_element(By.CSS_SELECTOR, "div._2KXGKToxF6BG65rXNZ-mJX:nth-child(1) > input:nth-child(3)")
        username_field.send_keys("testaccount00752")
        password_field = driver.find_element(By.CSS_SELECTOR, "div._2KXGKToxF6BG65rXNZ-mJX:nth-child(2) > input:nth-child(3)")
        password_field.send_keys("Test1029!")
        password_field.send_keys(Keys.RETURN)

        time.sleep(6)
        self.assertIn("dhs00752", driver.page_source)

    def test_add_to_wishlist(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/")
        time.sleep(3)
        cookie_button = driver.find_element(By.ID, "rejectAllButton")
        cookie_button.click()

        login_button = driver.find_element(By.CSS_SELECTOR, "a.global_action_link")
        login_button.click()
        time.sleep(3)

        username_field = driver.find_element(By.CSS_SELECTOR, "div._2KXGKToxF6BG65rXNZ-mJX:nth-child(1) > input:nth-child(3)")
        username_field.send_keys("testaccount00752")
        password_field = driver.find_element(By.CSS_SELECTOR, "div._2KXGKToxF6BG65rXNZ-mJX:nth-child(2) > input:nth-child(3)")
        password_field.send_keys("Test1029!")
        password_field.send_keys(Keys.RETURN)
        time.sleep(10)

        top_tab = driver.find_element(By.ID, "tab_topsellers_content_trigger")
        top_tab.click()
        item = driver.find_element(By.CSS_SELECTOR, "div.tab_content_items:nth-child(3) > a:nth-child(1)")
        item.click()
        time.sleep(3)

        wishlist_button = driver.find_element(By.ID, "add_to_wishlist_area")
        wishlist_button.click()
        time.sleep(3)

        wishlist_check = driver.find_element(By.CSS_SELECTOR, "#view_wishlist_btn > span")
        self.assertEqual(wishlist_check.text.strip(), "On Wishlist")
        wishlist_check.click()
        time.sleep(3)

        wishlist_check = driver.find_element(By.CSS_SELECTOR, "#add_to_wishlist_area > a > span")
        self.assertEqual(wishlist_check.text.strip(), "Add to your wishlist")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
