import urllib.request

price = 99.99

while price < 4.99:
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
    text = page.read().decode("utf8") 

    where = text.find('>$') 

    start_of_price = where + 2
    end_of_price = start_of_price + 4

    price = float(text[start_of_price:end_of_price])

print("现在，你们买啊！") 

