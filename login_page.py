
from Utilities import test_base
from Utilities import setting as S

import logging_conf
import logging
LOGGER = logging.getLogger(S.LOG_NAME)

def login_into_eod_tools(driver, username, password):
	"""
	This functionality is to login into the EOD Tools
	"""
	try:
		test_base.open_url(driver)
		test_base.maximize_window(driver)
		test_base.imp_wait(driver,10)

		driver.get_screenshot_as_file("1.png")

		test_base.sending_keys(driver, "LP_txtbx_username", username)
		test_base.sending_keys(driver, "LP_txtbx_password", password)
		test_base.click(driver, "LP_submit")
		test_base.time_sleep(10)

		link_text = test_base.get_text(driver,"LP_linktext")
		driver.get_screenshot_as_file("2.png")
		assert link_text == "Updates"

		assert test_base.is_enabled(driver,"LP_bell_icon") is True

		return link_text

	except Exception as e:
		LOGGER.exception(str(" login_into_eod_tools Exception: ") + str(e))

