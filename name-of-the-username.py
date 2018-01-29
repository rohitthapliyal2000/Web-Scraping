
import requests
from lxml import html

#user input
handle = input("Enter handle : ")

#valid username url
url = 'https://www.codechef.com/users/' + handle

page = requests.get(url)

tree = html.fromstring(page.content)

#Storing the text of the first 'main' tag's child 'aside' tag's child tag 'div'
data = tree.xpath("//main[1]/aside/div/text()")

if len(data) == 0:
	print("Not a valid handle")

else:
	print("Name of the user:")
	for i in range(3, len(data[0])):
		print(data[0][i], end ="")
	print('\n')