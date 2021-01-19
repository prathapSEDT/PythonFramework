from applicationobjects import HomePageOR
from frameworkutils import WebLibrary

def clickSignLink(driver):
    WebLibrary.clickElement(driver,HomePageOR.lnk_signin)