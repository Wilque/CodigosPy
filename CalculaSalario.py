print('================')
print('Calcula Salários')
print('================')

func = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário atual de {}: '.format(func.title())))
dep = input('{}, possui dependentes?[S/N] '.format(func.title()))

if dep.upper() == 'N':
    salario = salario+salario*0.05
    print('{}, irá receber R${:.2f}'.format(func.title(), salario))

elif dep.upper() == 'S':
    qtd = int(input('Quantos são?'))
    
    if qtd == 1:
        salario = salario+salario*0.1
        print('{}, irá receber R${:.2f}'.format(func.title(), salario))

    elif qtd == 2:
        salario = salario+salario*0.15
        print('{}, irá receber R${:.2f}'.format(func.title(), salario))

    else:
        salario = salario+salario*0.18
        print('{}, irá receber R${:.2f}'.format(func.title(), salario))
