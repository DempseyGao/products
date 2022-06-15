#function 的中心思想，是一個function只做一件事情
import os #operating system 作業系統=電腦的政府的意思
#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
					#跳到下一個迴圈
					#continue 跟 break 一樣只能放在迴圈裏面
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

	#寫入跟讀取檔案都要用同一種編碼(encoding='utf-8')
	#一個line是一行，就是一個字串
	#split(',')代表當他遇到逗號(,)就要進行切割
	#split切割完的東西會變成清單

#讓使用者輸入商品清單
def user_input(products):
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
	return products

		#把大清單(products)中的第一個小清單(p)的東西拿出來
		#二維清單

#印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是' , p[1])
		#只印出每一個小清單中的第幾個名字

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		#csv 是通融性最高
		f.write('商品, 價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')
			#str = string

def main():
	filename = 'products.csv'
	#檢查檔案在不在(只是個一行式的if，並不需要重複)
	if os.path.isfile(filename):
		print('找到檔案了!!!')
		products = read_file(filename)
	else:
		print('找不到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

#這叫做refactor重構