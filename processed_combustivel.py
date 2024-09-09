def calc_combustivel(delta_t: float, velocidade_media: float, gasto: int = 12): 
	delta_s = delta_t * velocidade_media 
	res = delta_s / gasto 
	return res 

tempo = float(input()) 
vm = float(input()) 
#res = calc_combustivel(22, 67) 
res = calc_combustivel(tempo, vm) 
print(f"{res: .3f}") 
