from Utilities import test_base
from datetime import datetime
from Utilities import setting as S

import logging_conf
import logging
LOGGER = logging.getLogger(S.LOG_NAME)

def validate_status_and_email_for_current_date(driver, mail_id):

	try:
		now = datetime.now()
		current_date = now.strftime("%d/%m/%Y")
		
		# rows = driver.find_elements_by_xpath("//table[@class='mat-table']//tbody//tr")
		row_len = test_base.find_elements(driver, "LP_rows")

		col_date = 1
		col_mail = 3

		for row in range(1, (row_len + 1)):
			row_ele = "//table[@class='mat-table']//tbody//tr[" + str(row) + "]//td[" + str(col_date) + "]"
			date_txt = driver.find_element_by_xpath(row_ele).text
			
			#Comparing if the date(1st column elements) is matching with current date
			if date_txt == current_date:
				LOGGER.info("The expected date '%s' is matching with current_date:", current_date)
				
				#if the date is matching then print the respective mail id which is in 3rd column
				req_mail= "//table[@class='mat-table']//tbody//tr[" + str(row) + "]//td[" + str(col_mail) + "]"
				mail_value = driver.find_element_by_xpath(req_mail).text
				
				if mail_id == mail_value :
					LOGGER.info("Mail id '%s' is matching with expected id '%s'", mail_id, mail_value)
				else:
					LOGGER.info("Mail id '%s' is not matching with expected id '%s'", mail_id, mail_value)


	except Exception as e:
		LOGGER.exception(str(" validate_status_and_email_for_current_date Exception: ") + str(e))
