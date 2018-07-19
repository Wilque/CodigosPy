nomes_magicos = ['howard thurston', 'david copperfield', 'lance burton',
                 'harry houdini', 'david blaine', 'dynamo', 'derren brown',
                 'criss angel']

def vermagicos (nomes):
    for i in nomes:
        print('Grande {}'.format(i))

vermagicos (nomes_magicos[:])
