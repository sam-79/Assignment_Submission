
gift_presented_to=list(map(int,input("Enter gift_presented_to list(space-seperated): ").split()))
print("gift_presented_to list: ",gift_presented_to)

mydict={}

for i in range(len(gift_presented_to)):
	mydict[gift_presented_to[i]-1]=i+1

gift_received_from=[]

for i in range(len(gift_presented_to)):
	gift_received_from.append(mydict[i])

print("gift_received_from list: ",gift_received_from)
