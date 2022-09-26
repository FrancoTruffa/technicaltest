def thousands_with_commas(i):
  result = format(i, ",d")
  return str(result)

if __name__=='__main__':
 assert(thousands_with_commas(1234)=='1,234')
 assert(thousands_with_commas(123456789)=='123,456,789')
 assert(thousands_with_commas(12)=='12')