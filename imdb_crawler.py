from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        movie_names = []
        for movie in self.list_of_movies:
            movie_names.append(movie.text)
        print(movie_names)
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
        list_of_movies = self.driver.find_elements_by_xpath(
            '//*/tbody[@class="lister-list"]/tr'
            )
        list_of_movies = list_of_movies[0:self.n_movies]
        return list_of_movies


if __name__ == '__main__':
    imdb_bot = imdb_bot(1)
