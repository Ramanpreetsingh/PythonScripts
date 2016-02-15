import requests

print 'Hey there delilah'

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

playfile = open('web_download.txt','wb')
for chunk in res.iter_content(100000):
	playfile.write(chunk)

playfile.close()	


print(type(res))
print(len(res.text))

print(res.text[:250])