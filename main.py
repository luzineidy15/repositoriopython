import modulo
import json
print("======MAC: Média de Avaliação Continua====")
dados={
    "nome": "Luzia",
      "idade": 15,
      "curso": "python"
      }
while True:
    try:
        a= int(input("digite a primeira nota: " ))
        b= int(input("digite a segunda nota: "))
        c= int(input("digite a terceira nota: "))
        if 0<= a <=20  and 0<= b <=20  and 0<= c <=20:
            break
        else:
            print("as notas devem estar de 0 a 20")
    except ValueError:
        print("digite apenas numeros")
    
resultado= modulo.media(a,b,c)
dados["media"]= resultado 

if resultado>=0 and resultado<=20:
    if resultado>=18:
            classificacao= "excelente"
    elif resultado>=16:
            classificacao= "muito bom"
    elif resultado>=12:
            classificacao="suficiente"
    elif resultado>=7:
            classificacao= "mediocre"
    else:
            classificacao= "muito mal"
    print(classificacao)
    dados["classificação"]= classificacao
else:
        print("nota invalida")        
        dados["classificação"]= "nota invalida"
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

