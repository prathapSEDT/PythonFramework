from frameworkutils import WebLibrary
from applicationobjects import AuthenticationOR

def validateAuthenticationHeader(driver):
    status=WebLibrary.elementExists(driver,AuthenticationOR.txt_Authentication)
    print(status)