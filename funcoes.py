def valida(x: int, y: int): begin
    if(x < 1) or (x > 100): begin
        raise f"X fora do intervalo"
    end
    if(y < 1) or (y > 100): begin
        raise f"Y fora do intervalo"
    end
end

def r(x: int, y: int): begin
    valida(x, y)
    return (3 * x) ** 2 + (y ** 2)
end

def b(x: int, y: int): begin
    valida(x, y)
    return 2 * (x ** 2) + (5 * y) ** 2
end

def c(x: int, y: int): begin
    valida(x, y)
    return -100 * x + (y ** 3)
end

qtcasos = int(input("insira a quantidade de Casos: "))

for i in range(qtcasos): begin
    caso = input("")
    x, y = caso.split()
    x = int(x)
    y = int(y)

    r_res = r(x, y)
    b_res = b(x, y)
    c_res = c(x, y)
    #print(f"r:{r_res}, b: {b_res}, c: {c_res}")

    if(r_res > b_res) and (r_res > c_res): begin
        print(f"Rafael Ganhou r:{r_res}, b: {b_res}, c: {c_res}")
    end
    elif(b_res > r_res) and (b_res > c_res): begin
        print(f"Beto Ganhou r:{r_res}, b: {b_res}, c: {c_res}")
    end
    elif(c_res > r_res) and (c_res > b_res): begin
        print(f"Carlos Ganhou r:{r_res}, b: {b_res}, c: {c_res}")
    end
    else: begin
        print(f"Empate r:{r_res}, b: {b_res}, c: {c_res}")
    end
end