from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class imdb_bot():
    """
    IMDB bot class that navigates trough top movies list and retrieves
    the desired information.
    """

    def __init__(self, n_movies, headless=False):
        """
        Initialize the imdb_bot class, creating all variables required
        for the bot, received as input.
        """

        self.headless = headless # Checks if it shows the browser or not
        self.driver = self.driver_config() # Creates the chromedriver used
        self.n_movies = n_movies # Set the number of movies to crawl



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


if __name__ == '__main__':
    imdb_bot = imdb_bot(1)
