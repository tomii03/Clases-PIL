
import random

monto = random.randint(1000,2000)

while True:
    print ('-'*20)
    print ('Bienvenido al cajero')
    print ('Opciones...')
    print ('1. Deposito: ')
    print ('2. Extraccion: ')
    print ('3. Tranferencia: ')
    print ('4. Salir: ')
    opc = int(input('Ingrese opciones: '))
    while opc > 4 or opc < 1:
        print ('Error, Ingrese opcion valida')
        opc = int(input('Ingrese opciones: '))
    
    print ('-'*20)
    print ('Monto actual:  $' + str(monto))
    print ('-'*20)

    if opc == 4:
        break

    elif opc == 1:
        dep = int(input('Ingrese dinero a depositar: '))
        print('Desea depositar: $' + str(dep) + ' ??')
        d_confirm = input('S o N: ')
        print (d_confirm)
        while d_confirm != 'S':
            if d_confirm == 'N':
                print('Cancelando...')
                break
            print ('Error, Ingrese opcion valida')
            d_confirm = input('Ingrese S o N: ')

        if d_confirm == 'S':
            monto += dep
            print ('El nuevo monto es de... $' + str(monto))
        
    elif opc == 2:
        ext = int(input('Ingrese dinero a extraer: '))
        print('Desea extraer: $' + str(ext) + ' ??')
        e_confirm = input('S o N: ')
        print (e_confirm)
        while e_confirm != 'S':
            if e_confirm == 'N':
                print('Cancelando...')
                break
            print ('Error, Ingrese opcion valida')
            e_confirm = input('Ingrese S o N: ')

        if e_confirm == 'S':
            monto -= ext
            print ('El nuevo monto es de... $' + str(monto))
        
    elif opc == 3:
        tranfe = int(input('Ingrese dinero a tranferir: '))
        print('Desea extraer: $' + str(tranfe) + ' ??')
        t_confirm = input('S o N: ')
        print (t_confirm)
        while t_confirm != 'S':
            if t_confirm == 'N':
                print('Cancelando...')
                break
            print ('Error, Ingrese opcion valida')
            t_confirm = input('Ingrese S o N: ')

        if t_confirm == 'S':
            monto -= tranfe
            print ('El nuevo monto es de... $' + str(monto))
        