#讀取檔案
#寫入跟讀取檔案都要用同一種編碼
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品, 價格' in line:
			continue
			#跳到下一個迴圈
			#continue 跟 break 一樣只能放在迴圈裏面
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)
		#一個line是一行，就是一個字串
		#split(',')代表當他遇到逗號(,)就要進行切割
		#split切割完的東西會變成清單

#讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':#quit
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	p = []
	p.append(name)
	p.append(price)
	#上面三行相當於 p = [name, price]
	products.append(p)
	#上面四行相當於 products.append([name, price])
print(products)

products[0][0]#把大清單(products)中的第一個小清單(p)的東西拿出來
# 二維清單

#印出所有購買紀錄
for p in products:
	print(p)
	print(p[0], '的價格是' , p[1])
	#只印出每一個小清單中的第幾個名字

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	#csv 是通融性最高
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		#str = string