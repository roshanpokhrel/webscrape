from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

# opening up a connection, grabbing the page
uClient = uReq(my_url)
# offloads contents into variable
page_html = uClient.read()
# close the connection
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)
# print(page_soup.p)
# print(page_soup.body)

# Find all div that have the class item-container
containers = page_soup.findAll("div", {"class":"item-container"})
#print(len(container))
#print(container[0])

# Open a csv file to write to
filename = "products_name.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)
for container in containers:
	brand = container.div.div.a.img["title"]		#Who makes this graphics card
	
	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class": "price-ship"})
	shipping = shipping_container[0].text.strip()		#strip to cut all whitespaces and other characters

	f.write(brand + ',' + product_name.replace(",", "|") + ',' + shipping + '\n')
#	print("My brand is:" + brand)
#	print("My Product is:" + product_name)
#	print("My shipping detail is:" + shipping)

f.close()