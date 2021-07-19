try:
  number = int(input("Enter a number:"))
except ValueError:
  print("Type Mismatch : Please enter a number")
except:
  print("Exception!")

print("Ending")