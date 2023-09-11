import requests, openpyxl 
import re
from bs4 import BeautifulSoup

try:
    license_name_tag =["0BSD","AAL","Abstyles","Adobe-2006","Adobe-Glyph","ADSL","AFL-1.1","AFL-1.2"]
    #name_list =[]
    

    url = "https://spdx.org/licenses/"
    url_1 = ".html"
    for lic_se in license_name_tag:
        #print ("lic name : " + lic_se)
        URL_S = url + lic_se + url_1
        #print(URL_S)
        response = requests.get(URL_S)
        #print(response.text)

        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify())
        #print (soup.find("div", class_="license-text").find_all("p"))
        #print(soup)
        license = soup.find_all('div', class_="page")
        for div in license:
        #[1].find_all("p"):
            h1 = div.find('h1')
            #p = div.find('p')
            print("*",h1.text)
            #ls_name = (h1.text)
            
            #name_list.append(ls_name)
            
            """lcc_l = soup.find_all('div', class_="license-text")
            for cont_ens in lcc_l:
            
                print(cont_ens)"""

            




            #print(name_list)            

            #print(license)
            """####lic_contens= soup.select('div.license-text p')
            #print(lic_contens)
            for cont_ens in lic_contens[3]:
                #leng_h = len(cont_ens)
                #print(leng_h)
                #p1 = cont_ens.find('p')
                print(cont_ens.text,"\n")
                #exit(1)"""

            """for licenses in license:
                licenses_name = licenses.find('var', class_="license-text")
                if licenses_name is None:
                    continue
                print(licenses_name)
            

            continue
            if True:
                #licenses_names = (licenses_name.text)
                print(licenses)
                for p_val in licenses.find_all("div"):
                    print(p_val)
                exit(1)
                #licenses_conten = licenses.find('p', class_="replaceable-license-text")
                #licenses_contens = (licenses_conten.text)
                print(licenses_names )
                #print(licenses_contens)
"""
        
except  Exception as e:
    print(e)

    
