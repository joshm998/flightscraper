#Importing packages
from selenium import webdriver
import time
import datetime
import json

class FlightResult:
    def __init__(self, flightName, departureDate, arrivalDate, price, fareType):
        self.flightName = flightName
        self.departureDate = departureDate
        self.arrivalDate = arrivalDate
        self.price = price
        self.fareType = fareType


class ScraperRun:
    def _init(self):
        self.FlightResults = []
        self.WebsiteCode = 'aaa'


driver = webdriver.Chrome('/Users/joshm998/Development/webdriver/chromedriver')
driver.get('https://booking.tigerair.com.au/TigerAirIBE/Booking/Search')
assert "tigerair IBE - Search A Flight" in driver.title
element = driver.find_element_by_xpath('//*[@id="oneWay"]')
driver.execute_script("arguments[0].click();", element)
driver.find_element_by_xpath('//*[@id="departurePortSelected"]').send_keys('adl')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="arrivalPortSelected"]').send_keys('mel')
time.sleep(2)
driver.execute_script("$('#departureDateField').val('01/12/2019').change();")
driver.find_element_by_xpath('//*[@id="searchFlightBtn"]').click()
flightElements = driver.find_elements_by_css_selector('td.js-fare-selection')

scraperResults = {}
scraperResults["FlightResults"] = []
scraperResults["DateRun"] = datetime.datetime.now().isoformat()
for item in flightElements:
    flightResult = {}
    flightResult["FlightName"] = "TT Sample"
    flightResult["DepartureDate"] = item.get_attribute('data-dep-date')
    flightResult["ArrivalDate"] = item.get_attribute('data-arr-date')
    flightResult["FlightCost"] = item.get_attribute('data-adt-fare')
    flightResult["FareType"] = item.get_attribute('data-fare-type')
    scraperResults["FlightResults"].append(flightResult)
json = json.dumps(scraperResults, ensure_ascii=False)
print(json)
