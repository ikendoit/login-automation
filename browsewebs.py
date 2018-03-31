from selenium import webdriver

# access the list of websites
def websites(weblist, wd):
    for i in weblist:
        wd.get(i)

# get list of websites from AutoData.txt
def getWebs(f):
    weblist = list()
    for line in f.readlines():
        if "link: " in line:
            weblist.append(line.split(" ")[1])
    return weblist

# iterate through list of websites
def browsewebss(f):
    while True:
        wd = webdriver.Chrome("chromedriver")
        wd.get("http://samsonhotel.com.vn")
        print(wd.find_element_by_css_selector(
            "#p1a-container > div.p1a-wrapper.clr > div.p1a-leftcol > div:nth-child(5) > ul > li.counter_day").text)
        websites(getWebs(f), wd)

        wd.close()
