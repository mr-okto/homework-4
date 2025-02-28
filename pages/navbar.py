from pages.base_component import Component


class NavBar(Component):
    MENU_BTN = '//div[@class="header-mobile__logo-wrapper"]'
    SEARCH_BTN = '//img[@class="header-mobile__search"]'
    MEETINGS_BTN = '//a[contains(@class, "navigation__choose-link") and @data-section="meetings"]'
    PEOPLE_BTN = '//a[contains(@class, "navigation__choose-link") and @data-section="people"]'
    SIGN_OUT = '//div[@id="signoutLink"]'

    def click_menu(self):
        self._wait_until_clickable(self.MENU_BTN).click()

    def click_search(self):
        self._wait_until_clickable(self.SEARCH_BTN).click()

    def click_meetings(self):
        self._wait_until_clickable(self.MEETINGS_BTN).click()

    def click_people(self):
        self._wait_until_clickable(self.PEOPLE_BTN).click()

    def click_sign_out(self):
        self._wait_until_clickable(self.SIGN_OUT).click()

