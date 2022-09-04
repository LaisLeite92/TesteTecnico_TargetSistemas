seq_fibonacci = [0,1]
num_infor = int(input('Favor informe o valor que deseja encontrar: '))
cont1 = 0
cont2 = 1
vfinal = 0

while vfinal < num_infor:
  soma = seq_fibonacci[cont1] + seq_fibonacci[cont2]
  vfinal = soma
  seq_fibonacci.append(soma)
  cont1 = cont1 + 1
  cont2 = cont2 + 1
print('Resultado: ')
if vfinal == num_infor:
  print(f'O valor {num_infor} foi encontrado na sequência.')
else:
  print(f'O Valor {num_infor} não foi encontrado na sequência.')
