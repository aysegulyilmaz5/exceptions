list = ['Aysegul',0,3]

for x in list:
  try:
    print("Number:" +str(x))
    result = 1/int(x)
    print("Result:" +str(result))
  except ValueError:
    print(str(x)+"Invalid number")
  except:
    print(str(x) + " Not Calculated")
    print("System "+str(sys.exc_info()[0]))
  finally:
    print("Operations ending")