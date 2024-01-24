# %pip install playwright

from playwright.sync_api import sync_playwright

# playwright 시작하기
p = sync_playwright().start()
# 브라우저를 열고, 실행브라우저의 경로를 넣는다.
browser = p.chromium.launch(
    headless=False, executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

# context를 만들어 다양한 세션에 대응한다.
context = browser.new_context()
# context에서 페이지를 생성한다.
page = context.new_page()
# 페이지로 이동한다.
page.goto("https://bit.ly/방학특강")

page.query_selector("#i8 > div.vd3tt > div").click()
