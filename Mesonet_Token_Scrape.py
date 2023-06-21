from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from github import Github
from time import sleep
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://developers.synopticdata.com/mesonet/")
sleep(30)
html_source = browser.page_source
tks = html_source.find("&amp;token=")+11
tke = tks+32
tkn = html_source[tks:tke]
browser.close()
browser.quit()
with open("\\ESOH Data\\mesonet_api_token.txt", "r") as text_file:
    tko = text_file.read().rstrip()
if tkn != tko:
    with open("\\ESOH Data\\mesonet_api_token.txt", "w") as text_file:
        text_file.write(tkn)
    g = Github("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")
    r = g.get_user().get_repo("dbaver.github.io")
    f = r.get_contents("./mesonet_api_token.txt")
    r.update_file("./mesonet_api_token.txt","Mesonet API Token Update",tkn,f.sha)
    
