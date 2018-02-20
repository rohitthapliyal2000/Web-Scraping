import requests
from lxml import html

def main():
  handle = str(input("Enter handle: "))
  page = requests.get('https://www.codechef.com/users/'+handle)
  tree = html.fromstring(page.content)
  fully_solved = tree.xpath('//div/div/section/div/article[1]/p/strong/text()')
  partially_solved = tree.xpath('//div/div/section/div/article[2]/p/strong/text()')

  if(len(fully_solved) == 0):
    print ("Invalid Handle")
    return


  #Count of total questions solved
  full_q_c = len(tree.xpath('//div/div/section/div/article[1]/p/span/a/text()'))
  partial_q_c = len(tree.xpath('//div/div/section/div/article[2]/p/span/a/text()'))

  full_q = []
  co = 1
  while (1):
    questions = tree.xpath('//div/div/section/div/article[1]/p[' + str(co) + ']/span/a/text()')
    co += 1
    if(len(questions) == 0):
      break
    else:
      full_q.append(questions)
    
  partial_q = []
  co = 1
  while (1):
    questions = tree.xpath('//div/div/section/div/article[2]/p[' + str(co) + ']/span/a/text()')
    co += 1
    if(len(questions) == 0):
      break
    else:
      partial_q.append(questions)
  print ("Fully Solved (" + str(full_q_c) + ") : ", end = "\n\n")
  for i in range(len(full_q)):
    print (fully_solved[i], end = ' ')
    for k, j in enumerate(full_q[i]):
      print (j, end = '')
      if(k != len(full_q[i]) - 1):
        print (", ", end = '')
    print ()
  print()
  
  print ("Partially Solved (" + str(partial_q_c) + "): ", end = "\n\n")
  for i in range(len(partial_q)):
    print (partially_solved[i], end = ' ')
    for k, j in enumerate(partial_q[i]):
      print (j, end = '')
      if(k != len(partial_q[i]) - 1):
        print (", ", end = '')
    print ()


if (__name__ == "__main__"):
  main()
