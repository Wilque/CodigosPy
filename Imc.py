print('===========')
print('Cálculo IMC')
print('===========')

altura = float(input('Digite sua altura em M: '))
peso = float(input('Digite seu peso em KG: '))

imc = peso/(altura*altura)

if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc < 24.9:
    print('peso ideal')
elif imc > 25 and imc < 29.9:
    print('Acima do peso')
elif imc > 30 and imc < 34.9:
    print('Obesidade I')
elif imc > 35 and imc < 39.9:
    print('Obesidade II')
else:
    print('Obesidade III')




