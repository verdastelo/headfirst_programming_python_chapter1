import urllib.request

page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
text = page.read().decode("utf8")

loc = text.find("$")
price = text[loc:loc+5]
print(price) 
