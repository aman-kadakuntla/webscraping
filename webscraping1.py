from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
url="https://www.flipkart.com/6bo/b5g/~cs-y81il7u9ez/pr?sid=6bo%2Cb5g&collection-tab-name=Best+Selling+Laptops&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkRlc2lnbiBDb250ZW50ICYgTGFwdG9wcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=17.productCard.PMU_V2_2"
page=None
try:   
    page=requests.get(url)
    print(page)
except:
    print("request cancelled")

content=bs(page.content,'html.parser')

laptops=content.findAll('div',class_="_4rR01T")

prices=content.findAll('div',class_="_30jeq3 _1_WHN1")

specifications=content.findAll('ul',class_="_1xgFaf")

laptops_list=[]
for i in laptops:
    laptops_list.append(i.get_text())

price_list=[]
for i in prices:
    price_list.append(i.get_text())

specifications_list=[]
for i in specifications:
    soup=bs(str(i),'html.parser')
    listofspecifics=[]
    for j in soup.find('ul').findChildren('li'):
        listofspecifics.append(j.get_text())
    specifications_list.append(listofspecifics)

processors_list=[]
ram_list=[]
os_list=[]
ssd_list=[]
display_list=[]
warranty_list=[]
others_list=[]

for i in specifications_list:
    for j in i:
        if 'Processor' in j:
            processors_list.append(j)
        elif 'RAM' in j:
            ram_list.append(j)
        elif 'Operating System' in j:
            os_list.append(j)
        elif 'SSD' in j:
            ssd_list.append(j)
        elif 'cm' in j:
            display_list.append(j)
        elif 'Year' in j:
            warranty_list.append(j)
        else:
            others_list.append(j)
    if(len(others_list))>len(processors_list):
        s=''
        for a in range((len(others_list)-len(processors_list))):
            s=s+others_list.pop()+" "
        others_list.append(others_list.pop()+" "+s)
    if(len(others_list)<len(processors_list)):
        for a in range(len(processors_list)-len(others_list)):
            others_list.append("NA")

df=pd.DataFrame()
df['Laptop']=laptops_list
df['Price']=price_list
df['Processor']=processors_list
df['RAM']=ram_list
df['SSD']=ssd_list
df['Operating System']=os_list
df['Display']=display_list
df['Other specification']=others_list
print(df.to_csv("D:\\Python Projects\\webscrapping\\laptops.csv"))
