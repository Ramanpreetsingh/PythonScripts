import webbrowser
import sys

default = 'https://www.google.com/maps/place/'
address = []


#print len(sys.argv)
if(len(sys.argv)>1):
	i=1
	while i < len(sys.argv):
		address.append(sys.argv[i])
		i = i+1
	
	#print '+'.join(address)
	#print(address)

	url = default + '+'.join(address)
	print 'url requested is',url

	#for it in address:
	#	print it	
	# (sys.argv)
	webbrowser.open(url)

else:
	print 'Insufficient arguments,please provide location'	