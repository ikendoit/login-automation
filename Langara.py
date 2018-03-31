from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#import redis
#TODO: store scraped infos in REDIS
import time
CHROME_PATH="./chromedriver"

# get user and pass for webs in AutoData.txt
def getInfo(initial,f):
    global user
    global password
    for line in f.readlines():
        if (initial in line):
            wrap = line.split(" ");
            user = wrap[1];
            password = wrap[2];

# d2l.langara
def d2l(f) :

    wd = webdriver.Chrome(CHROME_PATH)
    wd.get("http://d2l.langara.bc.ca")
    getInfo('d2l',f)
    wd.implicitly_wait(30)
    Ele1 = wd.find_element_by_xpath("//input[contains(@id,'user')] ").send_keys(user)
    wd.find_element_by_xpath(("//input[contains(@id,'pass')]")).send_keys(password)

    #click on notification
    wd.implicitly_wait(30)
    wd.find_element_by_xpath("//d2l-icon[contains(@icon,'notification-bell') and contains(@class,'x-scope d2l-icon-0')] ").click()

    #parse list notifications
    wd.implicitly_wait(30)
    notis = wd.find_elements_by_css_selector(".d2l-datalist-item-content")
    for noti in notis: 
        print(noti.get_attribute("title"))
    print("\n")

    time.sleep(60000)

#message.langara.bc.ca
def messagelang(f):

    wd = webdriver.Chrome(CHROME_PATH)
    wd.get("http://message.langara.bc.ca");
    getInfo('mylangara',f);
    wd.implicitly_wait(30)
    wd.find_element_by_id("username").send_keys(user)
    wd.find_element_by_id("password").send_keys(password)

    #get messages
    wd.implicitly_wait(30)
    wd.switch_to.frame(wd.find_element_by_xpath("//frame[@name='mailFrame']"))

    wd.implicitly_wait(30)
    messages= wd.find_elements_by_xpath("//tr[@bgcolor='white']");
    
    #parse each message element
    for message in messages[:5]: 
        title = message.find_element_by_xpath("td[contains(@width,'20%')]").text
        body = message.find_element_by_xpath("td[contains(@width,'50%')]").text
        print(title)
        print(body)
    print("\n")

    time.sleep(60000)

# mylangara.bc.ca
def mylangara(f):
    wd = webdriver.Chrome(CHROME_PATH)
    wd.implicitly_wait(30)
    wd.get("http://mylangara.bc.ca")
    getInfo("mylangara",f)
    wd.find_element_by_id("user").send_keys(user)

    wd.find_element_by_id(("pass")).send_keys(password)

    wd.implicitly_wait(20)

    #choose registration menu
    wd.find_element_by_link_text("Registration").click()

    #choose term
    wd.get("https://swing.langara.bc.ca/pls/prod/bwskflib.P_SelDefTerm")

    selected = Select(
        wd.find_element_by_xpath("/html/body/p/table/tbody/tr/td[2]/div[2]/form/table/tbody/tr/td[2]/select"))

    #set term
    selected.select_by_visible_text("Summer 2018")

    wd.find_element_by_css_selector(
        "body > p > table > tbody > tr > td:nth-child(2) > div.pagebodydiv > form > input[type='submit']:nth-child(3)").click()

    #sleep
    time.sleep(60000)

#C3 Langara Job Post Board
def C3(f):
    wd = webdriver.Chrome(CHROME_PATH)
    wd.implicitly_wait(30)
    wd.get("https://langara-csm.symplicity.com/students")
    getInfo("mylangara",f)
    wd.find_element_by_id("username").send_keys(user)
    wd.find_element_by_id("password").send_keys(password);

    #get to job posting
    wd.get("https://langara-csm.symplicity.com/students/index.php?s=jobs&ss=jobs&mode=list")
    wd.implicitly_wait(30)

    #choose COOP job in filter
    wd.find_element_by_xpath("//a[contains(@class,'ajax_advanced_search_button')]").click();
    wd.find_element_by_xpath("//select[contains(@id,'jobfilters_job_type')]/option[@value='3']").click();
    wd.find_element_by_xpath("//input[contains(@class,'ajax_filter_submit')]").send_keys("\n");

    #sleep
    time.sleep(300000)
