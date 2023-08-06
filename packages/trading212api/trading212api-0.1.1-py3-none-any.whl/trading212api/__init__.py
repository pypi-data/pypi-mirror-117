#!/usr/bin/python3

# trading212api
# Original GitHub project:
# https://github.com/auino/trading212api

import copy
import seleniumprocessor
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

# declaration of classes of exceptions

class ModeNotConfiguredException(Exception): pass
class MarketClosedException(Exception): pass
class LowerPriceException(Exception): pass
class HigherPriceException(Exception): pass

# internal static variables declaration

HOMELOAD_TO = 5
PAGELOAD_TO = 2
PAGEJS_TO = 1

FACTOR_TO = 3
TIMEOUTS_EDITED = False

FILTER_REAL = 'live'
FILTER_PRACTICE = 'demo'

URL_LOGIN = 'https://www.trading212.com/login'
URL_HOME_BASE = 'https://{}.trading212.com'
URL_HOME = URL_HOME_BASE

# declaration of processes

process_login = [
	{'name':'email', 'action':'click', 'sleep':PAGEJS_TO},
	{'name':'email', 'action':'send_keys', 'action_parameters':'{USERNAME}', 'sleep':PAGEJS_TO},
	{'name':'password', 'action':'click', 'sleep':PAGEJS_TO},
	{'name':'password', 'action':'send_keys', 'action_parameters':'{PASSWORD}', 'sleep':PAGEJS_TO},
	{'class_name':'submit-button', 'action':'click', 'sleep':PAGELOAD_TO}
]

process_portfolio = [
	{'class_name':'home-icon', 'action':'click', 'sleep':PAGELOAD_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'positions-table-item', 'action':'foreach', 'filter':FILTER_PRACTICE, 'action_parameters':[
		{'class_name':'instrument-name', 'action':'store_text', 'action_parameters':'name'},
		{'class_name':'quantity', 'action':'store_text', 'action_parameters':'shares'},
		{'class_name':'instrument-name', 'action':'click', 'sleep':PAGELOAD_TO},
		{'class_name':'quantity-and-price', 'action':'store_text', 'action_parameters':'quantity_and_price_full', 'context':'whole_page'},
		{'class_name':'formatted-price', 'action':'store_text', 'action_parameters':'value'},
		{'class_name':'position-result', 'action':'store_text', 'action_parameters':'return_value', 'context':'whole_page'},
	]},
	{'class_name':'portfolio-icon', 'action':'click', 'sleep':PAGELOAD_TO, 'filter':FILTER_REAL},
	{'class_name':'investment-item', 'action':'foreach', 'filter':FILTER_REAL, 'action_parameters':[
		{'class_name':'instrument-name', 'action':'store_text', 'action_parameters':'name'},
		{'class_name':'instrument-name', 'action':'click', 'sleep':PAGEJS_TO},
		{'class_name':'ticker', 'action':'store_text', 'action_parameters':'ticker', 'context':'whole_page'},
		{'class_name':'total-value', 'action':'store_text', 'action_parameters':'value'},
		{'class_name':'quantity', 'action':'store_text', 'action_parameters':'shares'},
		{'class_name':'return', 'action':'store_text', 'action_parameters':'return'}
	]}
]

process_getstocks_begin = [
	{'class_name':'search-icon', 'action':'click', 'sleep':PAGELOAD_TO},
	{'class_name':'search-folder-header', 'action':'navigate', 'action_parameters':'{NAVIGATION_PATH}', 'sleep':PAGEJS_TO}
]

process_getstocks_storeandscroll = [
	{'class_name':'item-wrapper', 'action':'foreach', 'action_parameters':[
		{'class_name':'name', 'action':'store_text', 'action_parameters':'name'},
		{'class_name':'secondary-name', 'action':'store_text', 'action_parameters':'ticker'}
	]},
	{'class_name':'item-wrapper', 'index':-1, 'action':'scroll_to', 'sleep':PAGELOAD_TO}
]

process_stockinfo = [
	{'class_name':'search-icon', 'action':'click', 'sleep':PAGELOAD_TO},
	{'class_name':'search-input', 'action':'click', 'sleep':PAGEJS_TO},
	{'class_name':'search-input', 'index':1, 'action':'send_keys', 'action_parameters':'{TICKER}', 'sleep':PAGELOAD_TO},
	{'class_name':'item-wrapper', 'action':'click', 'sleep':PAGELOAD_TO},
	{'class_name':'trading-chart-layout-button', 'action':'click', 'sleep':PAGELOAD_TO},
	{'class_name':'sidebar-header-option', 'index':0, 'action':'click', 'sleep':PAGEJS_TO},
	{'class_name':'instrument-name', 'action':'store_text', 'action_parameters':'name'},
	{'class_name':'ticker', 'action':'store_text', 'action_parameters':'ticker'},
	{'class_name':'market-status', 'action':'store_text', 'action_parameters':'market_status_full'},
	{'class_name':'priceBuy', 'action':'store_text', 'action_parameters':'full_price_buy'},
	{'class_name':'priceSell', 'action':'store_text', 'action_parameters':'full_price_sell'}
]

process_buy = [
	{'class_name':'trading-button', 'index':1, 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_REAL},
	{'class_name':'new-order-icon', 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'instrument-price', 'index':3, 'action':'click', 'sleep':PAGEJS_TO},
	{'class_name':'input', 'index':1, 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'input', 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_REAL},
	{'class_name':'input', 'index':1, 'action':'empty_value', 'sleep':PAGEJS_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'input', 'index':1, 'action':'send_keys', 'action_parameters':Keys.BACKSPACE, 'filter':FILTER_PRACTICE},
	{'class_name':'input', 'index':1, 'action':'send_keys', 'action_parameters':"{AMOUNT}", 'sleep':PAGEJS_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'input', 'action':'send_keys', 'action_parameters':"{AMOUNT}", 'sleep':PAGEJS_TO, 'filter':FILTER_REAL},
	{'class_name':'accent-button', 'index':2, 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_PRACTICE},
	{'class_name':'accent-button', 'action':'click', 'sleep':PAGEJS_TO, 'filter':FILTER_REAL}
]

process_sell = copy.deepcopy(process_buy)
for i in range(0, len(process_sell)):
	if process_sell[i].get('class_name') == 'trading-button': process_sell[i]['index'] -= 1
	if process_sell[i].get('class_name') == 'instrument-price': process_sell[i]['index'] -= 1

# internal functions declaration

# returns the content of the URL_HOME variable, by raising an exception if not properly configured (mode is not configured)
def get_urlhome():
	global URL_HOME
	if not FILTER_REAL in URL_HOME and not FILTER_PRACTICE in URL_HOME: raise ModeNotConfiguredException()
	return URL_HOME

# function used to tell if a filter f passes or not
def checkfilterpassed(f):
	return f in get_urlhome()

# external functions declaration

# multiplies all sleeps in the process p by the factor FACTOR_TO
def update_process_sleep(p, increase):
	for i in range(0, len(p)):
		if not p[i].get('sleep') is None:
			if increase: p[i]['sleep'] *= FACTOR_TO
			else: p[i]['sleep'] /= FACTOR_TO
		if p[i].get('action_parameters') is None: continue
		if type(p[i].get('action_parameters')) == list: p[i]['action_parameters'] = update_process_sleep(p[i].get('action_parameters'), increase)
	return p

# function to update timeouts and processes
def update_timeouts(increase):
	# updating global timeouts
	global PAGELOAD_TO, PAGEJS_TO
	if increase:
		PAGELOAD_TO *= FACTOR_TO
		PAGEJS_TO *= FACTOR_TO
	else:
		PAGELOAD_TO /= FACTOR_TO
		PAGEJS_TO /= FACTOR_TO
	# updating process timeouts
	global process_login, process_portfolio, process_stockinfo, process_getstocks_begin, process_getstocks_storeandscroll, process_buy, process_sell
	process_login = update_process_sleep(process_login, increase)
	process_portfolio = update_process_sleep(process_portfolio, increase)
	process_getstocks_begin = update_process_sleep(process_getstocks_begin, increase)
	process_getstocks_storeandscroll = update_process_sleep(process_getstocks_storeandscroll, increase)
	process_stockinfo = update_process_sleep(process_stockinfo, increase)
	process_buy = update_process_sleep(process_buy, increase)
	process_sell = update_process_sleep(process_sell, increase)

# function to enable real/live mode
def enable_real_mode():
	global URL_HOME
	URL_HOME = URL_HOME_BASE.format(FILTER_REAL)
	if TIMEOUTS_EDITED: update_timeouts(False)

# function to enable practice/demo mode
def enable_practice_mode():
	global URL_HOME
	URL_HOME = URL_HOME_BASE.format(FILTER_PRACTICE)
	# updating timeouts
	update_timeouts(True)
	# setting timeouts as edited
	global TIMEOUTS_EDITED
	TIMEOUTS_EDITED = True

# initiates a connection to URL_HOME
def initiate_connection(webdriverfile, loginusername=None, loginpassword=None, headless=False):
	global HOMELOAD_TO
	brw = seleniumprocessor.initiate_connection(webdriverfile, get_urlhome(), HOMELOAD_TO, loginusername is None, headless)
	if not loginusername is None:
		tmp_process_login = copy.deepcopy(process_login)
		for i in range(0, len(tmp_process_login)):
			if tmp_process_login[i].get('action_parameters') is None: continue
			if '{USERNAME}' in tmp_process_login[i].get('action_parameters'): tmp_process_login[i]['action_parameters'] = str(loginusername)
			if '{PASSWORD}' in tmp_process_login[i].get('action_parameters'): tmp_process_login[i]['action_parameters'] = str(loginpassword)
		seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, tmp_process_login, backtohome_begin=False)
	return brw

# returns the list of stocks
def get_stocks_list(brw, navigationpath=None):
	tmp_process_getstocks_begin = copy.deepcopy(process_getstocks_begin)
	for i in range(0, len(tmp_process_getstocks_begin)):
		if tmp_process_getstocks_begin[i].get('action_parameters') is None: continue
		if '{NAVIGATION_PATH}' in tmp_process_getstocks_begin[i].get('action_parameters'):
			if navigationpath is None: del tmp_process_getstocks_begin[i]
			else: tmp_process_getstocks_begin[i]['action_parameters'] = navigationpath
	seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, tmp_process_getstocks_begin, backtohome_end=False, checkfilterpassed_callback=checkfilterpassed)
	r = []
	max_height = brw.find_elements_by_class_name('scrollable-area')[1].find_element_by_tag_name('div').size['height']
	while True:
		l = seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, process_getstocks_storeandscroll, backtohome_begin=False, backtohome_end=False, checkfilterpassed_callback=checkfilterpassed)
		l = l.get('list')
		for e in l:
			if not e in r: r.append(e.get('ticker').replace(')', '(').replace('(', ''))
		# checking if last element
		attrs = brw.find_elements_by_class_name('item-wrapper')[-1].get_attribute("style").replace('; ', ';').split(';')
		el_height = 0
		for a in attrs:
			if 'top' in a or 'heigth' in a: el_height += int(a.replace(': ', ':').split(':')[1].replace('px', ''))
		if el_height >= max_height: break
	return r

# retrieves information from a stock with a given ticker, optionally, returning home at the begin/end of the method
def get_stock_info(brw, ticker, backtohome_begin=True, backtohome_end=True):
	tmp_process_stockinfo = copy.deepcopy(process_stockinfo)
	for i in range(0, len(tmp_process_stockinfo)):
		if tmp_process_stockinfo[i].get('action_parameters') is None: continue
		if '{TICKER}' in tmp_process_stockinfo[i].get('action_parameters'): tmp_process_stockinfo[i]['action_parameters'] = str(ticker)
	info = seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, tmp_process_stockinfo, backtohome_begin, backtohome_end, checkfilterpassed_callback=checkfilterpassed)
	# processing output for better presentation
	if '\n' in info.get('full_price_buy'): info['full_price_buy'] = info.get('full_price_buy').split('\n')[1]
	if '\n' in info.get('full_price_sell'): info['full_price_sell'] = info.get('full_price_sell').split('\n')[1]
	info['valuta'] = info.get('full_price_buy')[0]
	info['price_buy'] = float(info.get('full_price_buy')[1:].replace(',', ''))
	info['price_sell'] = float(info.get('full_price_sell')[1:].replace(',', ''))
	info['market_open'] = 'open' in info.get('market_status_full').lower()
	del info['full_price_buy']
	del info['full_price_sell']
	del info['market_status_full']
	return info

# retrieves information on the current portfolio
def get_portfolio(brw):
	portfolio = seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, process_portfolio, checkfilterpassed_callback=checkfilterpassed)
	# processing output for better presentation
	portfolio = portfolio.get('list')
	for i in range(0, len(portfolio)):
		if portfolio[i].get('quantity_and_price_full') is None:
			portfolio[i]['valuta'] = portfolio[i].get('value')[0]
			portfolio[i]['value'] = portfolio[i].get('value')[1:]
		else:
			portfolio[i]['valuta'] = portfolio[i].get('quantity_and_price_full').split(' ')[2][0]
			portfolio[i]['value'] = portfolio[i].get('quantity_and_price_full').split(' ')[2][1:]
			del portfolio[i]['quantity_and_price_full']
		portfolio[i]['value'] = float(portfolio[i].get('value').replace(',', ''))
		if ' ' in portfolio[i].get('shares'): portfolio[i]['shares'] = float(portfolio[i].get('shares').split(' ')[0].replace(',', ''))
		if not portfolio[i].get('return_value') is None:
			portfolio[i]['return'] = '{} ({}%)'.format(portfolio[i].get('return_value'), float(float(portfolio[i].get('return_value')[1:]) / float(portfolio[i].get('value')) * 100))
			del portfolio[i]['return_value']
		if not portfolio[i].get('return') is None:
			portfolio[i]['return_percentage'] = float(portfolio[i].get('return').split('(')[1].split('%')[0])
		portfolio[i]['return'] = float(portfolio[i].get('return').split(' ')[0][1:])
		return portfolio

# buys a stock identified by its own ticket, specifying the amount to spent (in current valuta) and an optional maximum price
def buy(brw, ticker, amount, max_price=None):
	info = get_stock_info(brw, ticker, backtohome_begin=True, backtohome_end=False)
	if not info.get('market_open'): raise MarketClosedException()
	if max_price != None and info.get('price_buy') > float(max_price): raise HigherPriceException()
	# fixing the amount to be filled in
	tmp_process_buy = copy.deepcopy(process_buy)
	for i in range(0, len(tmp_process_buy)):
		if tmp_process_buy[i].get('action_parameters') is None: continue
		if '{AMOUNT}' in tmp_process_buy[i].get('action_parameters'): tmp_process_buy[i]['action_parameters'] = str(amount)
	seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, tmp_process_buy, backtohome_begin=False, checkfilterpassed_callback=checkfilterpassed)
	return True

# sells a stock identified by its own ticket, specifying the amount in terms of number of stocks to sell and an optional minimum price
def sell(brw, ticker, amount=None, min_price=None):
	info = get_stock_info(brw, ticker, backtohome_begin=True, backtohome_end=False)
	if not info.get('market_open'): raise MarketClosedException()
	if min_price != None and info.get('price_sell') < float(min_price): raise LowerPriceException()
	# fixing the amount to be filled in
	tmp_process_sell = copy.deepcopy(process_sell)
	for i in range(0, len(tmp_process_sell)):
		if tmp_process_sell[i].get('action_parameters') is None: continue
		if '{AMOUNT}' in tmp_process_sell[i].get('action_parameters'):
			if amount is None: del tmp_process_sell[i]
			else: tmp_process_sell[i]['action_parameters'] = str(amount)
	seleniumprocessor.run_process(brw, get_urlhome(), HOMELOAD_TO, tmp_process_sell, backtohome_begin=False, checkfilterpassed_callback=checkfilterpassed)
	return True
