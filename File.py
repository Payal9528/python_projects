with  open('Data.csv',"r+") as file:
  content = file.read()
  print(content)
  line5 = file.readlines() 
  print(line5)