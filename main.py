n = int(input("Enter the number of Guests: "))
guests = []

for i in range(0, n):
  name = str(input("Enter the name of Guests: "))
  guests.append(name)
print("Guests are: ", guests)
if(n%2==0):
  for k in range( int((n)/2) , n-1):
    print("\nFashionable late persons are: ", guests[k])
elif(n%2 != 0):
  for k in range( int((n-1)/2) , n-1):
    print("\nFashionable late persons are: ", guests[k])



