import requests
from lxml import html

#user input
handle = input("Enter handle : ")

#valid username url
url = 'https://www.codechef.com/users/' + handle

page = requests.get(url)

tree = html.fromstring(page.content)

data = tree.xpath("//div/section/div/div/div/a/text()")

if len(data) == 0:
	print("Not a valid handle")

else:
	for i in range(0, len(data[0])-2):
		print(data[0][i], end="")
