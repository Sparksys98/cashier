def main():
	dic={}
	items=[]
	while True:
		name=str(input("Items: enter \"done\" when finished: "))
		if(name=="done"):
			break
		price=float(input("Price: "))
		quantity=int(input("Quantity:" ))

		dic["name"] = name
		dic["price"] = price
		dic["quantity"] = quantity
		price=dic["price"]*dic["quantity"]
		items.append(dic.copy())
		total2=0
		for num in items:
			total=num["quantity"]*num["price"]
			print(num["quantity"] , num["name"] ,total)
			total2=total2+total

		print("Total is: ", total2)

if __name__ == '__main__':
	main()
