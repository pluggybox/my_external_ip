# -*- coding: iso-8859-1 -*-

#import re
import requests


def extraire_ip(url):
    request = requests.get(url)
    return request.text
    
#==============================================================================    
#                               M A I N    
#==============================================================================    
if __name__ == "__main__" :
    external_ip = extraire_ip("http://myip.dnsdynamic.org")
    print 'external_ip: ', external_ip

