import bs4
#from BeautifulSoup import BeautifulSoup 

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,'lxml')

elems = exampleSoup.select('#author')

print(type(elems))
print(elems[0])
print(elems[0].getText())
