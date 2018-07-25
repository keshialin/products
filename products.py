products = []
while True:
	name = input('請輸入商品名稱 or [q]quit:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)

for p in products:
	print('{}的價格是{}'.format(p[0],p[1]))