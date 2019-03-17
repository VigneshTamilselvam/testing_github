import pytest
from POM import login_page
from POM import home_page


@pytest.mark.parametrize("username, password, emailid",[
	("vignesh", "password", "vignesh.t@stride.ai"), ("ajay", "password", "vinod.t@stride.ai")
])

def test_eod(request, driver, username, password, emailid):
	status = login_page.login_into_eod_tools(driver, username, password)

	# assert status == True
	# assert link_text == "Updates"
	# #assert title is True

	home_page.validate_status_and_email_for_current_date(driver,emailid)

	request.node._status = status

	
	
	























	




