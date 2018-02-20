#Count tags in stackoverflow of popular tags in descending order

import requests
from lxml import html

def main():

  print ("======================================================================")
  print ("Show all the tags and their count in StackOverflow in descending order")
  print ("======================================================================")
  print ()
  #Show only 5 pages of popluar tags.
  #Change val if you want to increase or decrease pages.
  val = 5
  for co in range(1, val + 1):
    page = requests.get('https://stackoverflow.com/tags?page='+str(co)+'&tab=popular')
    tree = html.fromstring(page.content)
    
    tag_name = tree.xpath('//div/table/tr/td/a/text()')
    tag_count = tree.xpath('//div/table/tr/td/span/span/text()')
    

    if((len(tag_name)) == 0):
      return
    j = 1;
    for i in tag_name:
      print (i, end = '')
      sp = 40 - len(i)
      whsp = ' ' * sp
      print (whsp, end = '')
      print (tag_count[j-1]+tag_count[j])
      j += 2


if (__name__ == "__main__"):
  main()
