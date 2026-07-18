preco_final = 0
import os
money = 100.00
prod_comprados = []
prod = ["Tomate", "banana", "laranja"]
pric = [2.90, 3.50, 5.00]
conta = ""
conta_atual = ""
senha = ""
senha_atual = ""
desc = "O"
def final(price, total):
    money =- (price * total)
def desconto(price_old):
    if price_old > 100:
        price_new = price_old * 0.9
    else:
        price_new = price_old
    return price_new
def calcular_preco(price, total):
    return price * total
def cad_prod (nome, price):
    prod.append(nome)
    pric.append(price)
def mostrar_produtos():
    for product in range(0,len(prod)):
        print(product," - ",prod[product])
        print(pric[product])

if conta == "" :
    print("Faça Login para acessar a loja")
    conta = input("Coloque um nome para sua conta")
    senha = input("faça uma senha para acessar a loja")
os.system("cls")
while conta_atual == "":
    senha_atual = input("digite sua senha para acessar o site")
    if senha_atual == senha:
        print("Seja bem vindo devolta")
        conta_atual = conta
    else:
        print("senha incorreta tente novamente")

while money > 0
    print("Escolha um dos produtos do nosso catalogo")
    mostrar_produtos()
    prod_esc = len(prod) + 5
    while prod_esc > (len(prod)-1):
        prod_esc = int(input("Escolha um produto"))
        if prod_esc > (len(prod)-1):
            print("erro!! produto selecionado nao existe, tente novamente")
    print("o Produto :",prod[prod_esc]," foi escolhido")
    quant = int(input("quantos deseja levar?"))
    while desc != "S" and desc != "N":
        desc = input("deseja aplicar um desconto?[S/N]")
        if desc == "S":
            preco_final = desconto(calcular_preco(pric[prod_esc], quant))
        elif desc == "N":
            preco_final = calcular_preco(pric[prod_esc], quant)


print("o preço final é :",preco_final,"/ Seu dinheiro atual é",money)
conf = input("Deseja confirmar a compra?[S/N]")
if conf == "S":
    money =- preco_final
    for product in range(0,len(prod_comprados)):
        print(product," - ",prod_comprados[product])
elif conf == "N":
    pass
else:
    print("Como nenhuma mensagem compativel foi colocada irei assumir que nao quer comprar")