"""x = float(input("Qual o valor de x? "))
y = float(input("Qual o valor de y? "))

if x < y:
    print("x é maior que y")
elif x == y:
    print("x é igual a y")
else:
    print("x e menor que y")"""

while True:
    score = int(input("Score: "))

    if score >= 90 and score <=100:
        print("Grade: A")
    elif score >= 80 and score < 90:
        print("Grade B")
    elif score >= 70 and score < 80:
        print("Grade: C")
    elif score >=60 and score < 70:
        print("Grade: D")
    else:
        print("Grade: F")

    resposta = input("Deseja continuar? ").title()
    print(resposta)
    if (resposta == "Não") or (resposta == "Nao") :
        break
