# trading212api

An unofficial API library for Trading212 based on Selenium

### Description ###

This library allows you to interface with [Trading212](http://www.trading212.com) through [Selenium](https://www.selenium.dev).
Once you log in, the only operation requiring a human interation, you can buy and sell stocks, in both real and practice modes.

### Installation ###

```
pip install trading212api
```

Install a [Selenium](https://www.selenium.dev) web driver, e.g., the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/)

#### Available methods ####

* `enable_real_mode()`: this method is used to enable real/live mode
* `enable_practice_mode()`: this method is used to enable practice/demo mode
* `initiate_connection(webdriverfile, loginusername=None, loginpassword=None)`: initializes the connection to [Trading212](https://www.trading212.com) through [Selenium](https://www.selenium.dev), optionally asking for username and password to login; in such case, an automatic login will be performed; otherwise, user interaction will be required, for a manual login to occur
* `get_stocks_list(brw, navigationpath=None)`: returns all the list of stocks available, optionally selecting a specific `>` separated list identifying the navigation path, in terms of content, to follow
* `get_stock_info(brw, ticker, backtohome_begin=True, backtohome_end=True)`: starting from a `selenium.webdriver.chrome.webdriver.WebDriver` object `brw`, this method retrieves information from a stock identified by a given `ticker`, optionally, returning home at the begin/end of the method
* `get_portfolio(brw)`: starting from a `selenium.webdriver.chrome.webdriver.WebDriver` object `brw`, this method returns information on the current portfolio
* `buy(brw, ticker, amount, max_price=None)`: starting from a `selenium.webdriver.chrome.webdriver.WebDriver` object `brw`, this method buys a stock identified by its own `ticket`, specifying the `amount` in terms of money to invest in the current valuta, plus an optional maximum price `max_price`; returns a boolean value indicating the success of the operation
* `sell(brw, ticker, amount=None, min_price=None)`: starting from a `selenium.webdriver.chrome.webdriver.WebDriver` object `brw`, this method sells a stock identified by its own `ticket`, specifying the `amount` in terms of number of stocks to sell and an optional minimum price `min_price`; returns a boolean value indicating the success of the operation

### Sample usage ###

```
# import the library
import trading212api

# enable practice mode
trading212api.enable_practice_mode()

# initiate the connection
brw = trading212api.initiate_connection('./chromedriver')

# get and print portfolio information
portfolio = trading212api.get_portfolio(brw)
print(portfolio)

# get and print information on a given stock
stock_info = trading212api.get_stock_info(brw, 'AAPL')
print(stock_info)

# get all most popular stocks
popular_stocks = trading212api.get_stocks_list(brw, navigationpath='Stocks>Most Popular')

# get and print information on all most popular stocks
for s in popular_stocks:
	stock_info = trading212api.get_stock_info(brw, s.get('ticker'))
	print(stock_info)

# buy 10 USD of AAPL
trading212api.buy(brw, 'AAPL', 10)

# sell 1 stock of AAPL
trading212api.sell(brw, 'AAPL', 1)
```

### TODO ###

* Improve code readability

### Contacts ###

You can find me on [Twitter](https://twitter.com) as [@auino](https://twitter.com/auino).
