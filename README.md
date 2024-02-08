Install :

pip install pytest-playwright
playwright install
pip install pytest-html  (to get html report)
   Command : pytest -m sanity --html=myreport.html // where -m to pass pytest marker i.e. tag
pip install pytest-retry  (to retry failed test cases)
   Command : pytest -m sanity1 --retries 2  --html=myreport.html


To Handle multiple window :     
   with page.expect_popup() as new_page_info:
        page.locator("css=#opentab").click()  # Opens a new tab
    new_page = new_page_info.value

Advantages of playwright:
Execution speed is fast
provides auto-wait for the locator
wide range of options to locate elemenet
provide code-gen to record and generate code (playwright codegen)

Fixture are used for the purpose of hooks i.e. set_up and tear down

