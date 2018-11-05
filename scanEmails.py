from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import re

options = webdriver.ChromeOptions()
chrome_prefs = {}
options.experimental_options["prefs"] = chrome_prefs
# options.add_argument('--headless')
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}


def getemails(link):
    driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
    print(link)
    try:
        driver.get(link)
        visited = set()
        allemails = set()
        allLinks = set()
        html =driver.page_source.encode("utf-8")
        getdomain=driver.execute_script("return window.location.hostname")
        domain=re.findall(r'\.[\w]+\.',getdomain)
        v=re.findall(r'\w+',domain[0])
        email=re.findall(r'[\w\.-]+@[\w\.]+\.'+v[0]+'\.[\w]+|[\w]+@'+v[0]+'[a-zA-Z\.]+', html, flags=re.IGNORECASE)         
        
        if len(email) !=0:
            for x in email:
                if x not in allemails:
                    allemails.add(x)
                    yield(x)
        aal = driver.find_elements_by_tag_name("a")
        if len(aal) > 0:
            for link in aal:
                getlinkhome = link.get_attribute("href")

                allLinks.add(getlinkhome)
        else:
            print {"data": "no detail"}
    except Exception as ex:
        print(ex)
    while len(allLinks) != 0:
        print str(len(allLinks))
        try:
            link = allLinks.pop()
            if ".pdf" in link:
                continue
            if link not in visited:
                print link
                visited.add(link)
                driver.get(link)            
                html = driver.page_source.encode("utf-8")
                getdomain=driver.execute_script("return window.location.hostname")
                domain=re.findall(r'\.[\w]+\.',getdomain)
                v=re.findall(r'\w+',domain[0])
                email=re.findall(r'[\w\.-]+@[\w\.]+\.'+v[0]+'\.[\w]+|[\w]+@'+v[0]+'[a-zA-Z\.]+', html, flags=re.IGNORECASE)     
                if len(email) !=0:
                    for x in email:
                        if x not in allemails:
                            allemails.add(x)
                            yield(x)
        except Exception as ex:
            print("invalid link")

    print(allemails)

# if __name__ == '__main__':
#     for alll in getemails("https://www.pta.gov.pk/en/media-center/single-media/pta-extends-deadline-of-device-identification-registration-and-blocking-system-dirbs--181018"):
#         print alll
        # getemails("https://www.pta.gov.pk/en/media-center/single-media/pta-extends-deadline-of-device-identification-registration-and-blocking-system-dirbs--181018")    
