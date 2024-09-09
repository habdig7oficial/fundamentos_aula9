def valida(x: int, y: int): 
	if(x < 1) or (x > 100): 
		raise f"X fora do intervalo" 

	if(y < 1) or (y > 100): 
		raise f"Y fora do intervalo" 



def r(x: int, y: int): 
	valida(x, y) 
	return (3 * x) ** 2 + (y ** 2) 


def b(x: int, y: int): 
	valida(x, y) 
	return 2 * (x ** 2) + (5 * y) ** 2 


def c(x: int, y: int): 
	valida(x, y) 
	return -100 * x + (y ** 3) 


qtcasos = int(input("insira a quantidade de Casos: ")) 

for i in range(qtcasos): 
	caso = input("") 
	x, y = caso.split() 
	x = int(x) 
	y = int(y) 

	r_res = r(x, y) 
	b_res = b(x, y) 
	c_res = c(x, y) 
	#print(f"r:{r_res}, b: {b_res}, c: {c_res}") 

	if(r_res > b_res) and (r_res > c_res): 
		print(f"Rafael Ganhou r:{r_res}, b: {b_res}, c: {c_res}") 

	elif(b_res > r_res) and (b_res > c_res): 
		print(f"Beto Ganhou r:{r_res}, b: {b_res}, c: {c_res}") 

	elif(c_res > r_res) and (c_res > b_res): 
		print(f"Carlos Ganhou r:{r_res}, b: {b_res}, c: {c_res}") 

	else: 
		print(f"Empate r:{r_res}, b: {b_res}, c: {c_res}") 


