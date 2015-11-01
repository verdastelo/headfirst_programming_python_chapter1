text = "This costs <html>$10</html> and we are against it."

index = text.find(">$")

print(text[(index+1):(index+4)]) 
