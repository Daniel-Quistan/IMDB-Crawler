from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class imdb_bot():
    """
    IMDB bot class that navigates trough top movies list and retrieves
    the desired information.
    """


    def __init__(self, n_movies=30, headless=False):
        """
        Initialize the imdb_bot class, creating all variables required
        for the bot, received as input.
        """

        self.headless = headless # Checks if it shows the browser or not.
        self.movies_url = 'https://www.imdb.com/chart/top/'
        self.driver = self.driver_config() # Creates the chromedriver used.
        self.driver.get(self.movies_url) # Go to IMDB top 250 page.
        self.n_movies = n_movies # Set the number of movies to crawl.
        self.list_of_movies = self.get_list_of_movies()
        self.get_movie_data()
        self.driver.quit()


    def driver_config(self):
        """
        Configures the Chromedriver that will use the browser to navigate
        the web, with the option between headless or not.
        """
        chrome_options = Options()
        chrome_options.add_argument('start-maximized')
        if self.headless: # Checks if it shows the browser or not
            chrome_options.add_argument('headless')
        driver =  webdriver.Chrome(options=chrome_options)
        return driver


    def get_list_of_movies(self):
        """
        Get's the page elements of the number of movies specified.
        """

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*/tbody[@class="lister-list"]/tr/td[1]')
                ))

        list_of_movies = self.driver.find_elements_by_xpath(
            '//*/tbody[@class="lister-list"]/tr/td[1]/a'
            )
        list_of_movies = list_of_movies[0:self.n_movies]
        return list_of_movies


    def get_movie_data(self):
        """
        Function that clicks each movie on list_of_movies and grabs
        data from it's page.
        """
        for movie in self.list_of_movies:
            movie.send_keys(Keys.CONTROL + Keys.RETURN)
            self.change_windows()
            self.get_data_from_movie()
            self.driver.close()
            self.change_windows()


    def change_windows(self):
        """
        Changes windows from window 0 to 1 and vice-versa.
        """
        windows = self.driver.window_handles
        if len(windows) != 1:
            self.driver.switch_to.window(windows[1])
        else:
            self.driver.switch_to.window(windows[0])



    def get_data_from_movie(self):
        """Functions that get's desired data from inside the movie URL"""
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'titleBar')
                ))
        title_1 = self.driver.find_element_by_xpath(
            '//*/div[@class="originalTitle"]'
            )
        title_2 = title_1.find_element_by_tag_name('span')
        title = title_1.text.replace(title_2.text, '')
        year = self.driver.find_element_by_id('titleYear').text
        year = year.replace('(', '').replace(')', '')
        rating = self.driver.find_element_by_class_name('ratingValue').text
        rating = rating.split('/')[0]
        director = self.driver.find_element_by_xpath(
            '//*/h4[@class = "inline" and contains(text(), "Director")]/following-sibling::a'
        ).text
        stars = self.driver.find_elements_by_xpath(
            '//*/h4[@class = "inline" and contains(text(), "Stars")]/following-sibling::a'
        )
        actors =[]
        for star in stars[0: len(stars)-1]:
            actors.append(star.text)
        cast = ', '.join(actors)

        recomendations = self.get_recomendations()


        print(title, year, rating, director, cast)

    def get_recomendations(self):
        """Inside a movie webpage get all movies recommended by IMDB."""
        self.driver.find_element_by_id(
            'titleRecs'
            ).location_once_scrolled_into_view
        time.sleep(5)



if __name__ == '__main__':
    imdb_bot = imdb_bot(5)
