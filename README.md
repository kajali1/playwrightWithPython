Install :

pip install pytest-playwright
playwright install
pip install pytest-html  (to get html report)
   Command : pytest -m sanity --html=myreport.html // where -m to pass pytest marker i.e. tag
pip install pytest-retry  (to retry failed test cases)
   Command : pytest -m sanity1 --retries 2  --html=myreport.html
