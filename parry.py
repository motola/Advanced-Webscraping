MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

for i in range(1, MAX_PAGE_NUM + 1):
  page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
  print(page_num)