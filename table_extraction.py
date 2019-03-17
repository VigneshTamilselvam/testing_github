
from Utilities import setting as S
from selenium import webdriver

import logging_conf
import logging
LOGGER = logging.getLogger(S.LOG_NAME)

driver = webdriver.Chrome()

company_name = "IDFC L"

try:
	
	driver.get("http://demo.guru99.com/test/web-table-element.php")
	driver.maximize_window()
	driver.implicitly_wait(10)

	rows = driver.find_elements_by_xpath("//table[@class='dataTable']//tbody//tr")
	print(type(rows))
	print(len(rows))
	columns = driver.find_elements_by_xpath("//table[@class='dataTable']//thead//th")
	print(type(columns))
	print(len(columns))

	for col in range(1):
		for row in range(1, (len(rows)+1)):
			row_ele = "//table[@class='dataTable']//tbody//tr[" + str(row) + "]//td[" + str(1) + "]"
			row_value = driver.find_element_by_xpath(row_ele).text

			
			if row_value == company_name:
				current_price= "//table[@class='dataTable']//tbody//tr[" + str(row) + "]//td[" + str(4) + "]"
				req_value= driver.find_element_by_xpath(current_price).text
				print(req_value)
	
			
		print("No such company exists")

		print("****************************")
			


except Exception as e:
	LOGGER.exception(str("table extraction Exception: " + str(e)))

