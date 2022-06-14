products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	#上面三行相當於 p = [name, price]
	products.append(p)
	#上面四行相當於 products.append([name, price])
print(products)

products[0][0]#把大清單(products)中的第一個小清單(p)的東西拿出來
# 二維清單

for p in products:
	print(p)
	print(p[0], '的價格是' , p[1])
	#只印出每一個小清單中的第幾個名字