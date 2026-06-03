Alimentação = {"Azul":["Azul"], "Verde":["Azul", "Amarela"],"Amarelo":["Amarela"],"Laranja":["Amarela", "Vermelha"],"Vermelho":["Vermelha"]}

def alimentar(passarinho):  
    sementes = Alimentação[passarinho]
    print(f"Passarinho {passarinho} come semente(s): {', '.join(sementes)}") 
    

passarinho=input("Qual passarinho você quer alimentar? ")

if passarinho =="azul":
    print("Come semente: azul")
elif passarinho=="verde":
    print("Come sementes: azul e amarela")
elif passarinho=="amarelo":
    print("Come semente: amarela")
elif passarinho=="laranja":
    print("Come sementes: amarela e vermelha")
elif passarinho=="vermelho":
    print("Come semente: vermelha")
else:
    print("Passarinho não reconhecido!")