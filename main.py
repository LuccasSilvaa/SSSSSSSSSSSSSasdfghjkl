
# missão 1

nome = input('Nome do aluno: ')
nota = float(input('Nota: '))

if nota >= 6:
    print('Aprovado')
else:
    print('Reprovado')

# missão 2

usuario = input('Qual seu nome ? ')
idade = int(input(f'Qual sua idade  {usuario}  ? '))

if idade > 16:
    print("Você está liberado para votar")
else:
    print("Infelizmente você não está liberado para votar")

# missão 3

nome_aluno = input('Qual seu nome ?: ')
nota_aluno = int(input('Qual sua nota ?:'))

if nota_aluno >= 90 and nota_aluno <= 100:
    print("Parabéns, você tirou A!")
elif nota_aluno >= 80 and nota_aluno <= 89:
    print("Muito bem, você tirou B.")
elif nota_aluno >= 70 and nota_aluno <= 79:
    print("Bom trabalho, você tirou C.")
elif nota_aluno >= 60 and nota_aluno <= 69:
    print("Fique atento, você tirou D.")
elif nota_aluno < 60:
    print("Estude um pouco mais, você tirou F.")
else:
    print("Nota invalida")

# missão 4

primeiro_numero = int(input("Escolha o primeiro numero: "))
segundo_numero = int(input("Escolha o segundo numero: "))

soma = primeiro_numero + segundo_numero

print(f"a soma dos dois numero é {soma}")

# missão 5

login_usuario = input("Digite o usuario: ")
login_senha = input("Digite a senha: ")

if login_senha == 'Python123':
    print("Sucesso!")
else:
    print("Senha incorreta!")

# missão 6

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

# missão 7

numeros = [8, 3, 10, 1, 5]

numeros.sort()

print(numeros)

# missão 8

registro_alunos = "Ana", "Bruno", "Carla", "Daniel", "Eduardo",

print(registro_alunos[0], registro_alunos[4])

# missão 9

numero = int(input("Digite o numero: "))


def dobro(num):
    dobro = num * 2
    return dobro


print(f"O dobro de {numero} é {dobro(numero)}")

# missão 10


def contar_letras():
    nome_pessoa = input("Digite seu nome: ")
    return print(f"O nome {nome_pessoa} tem {len(nome_pessoa)} letras")


contar_letras()
