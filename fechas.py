
def encontra_medio_modulo(hora, minutos):
    if hora < 7:
        print("El nodo no funciona, llamar al encarcado de infraestructura, don louis")

    if hora == 7:
        if minutos <= 10:
            print("Es muy temprano che para retirar.")
        else:
            print("Se encuentran en el primer medio modulo")
            medio_modulo = 1

    elif hora == 8: 
        if minutos <= 24:
            print("Se encuentran en el primer medio modulo")
            medio_modulo = 1
        else:
            print("Se encuentran en el segundo medio modulo")
            medio_modulo = 2

    if hora == 9:
        if minutos <= 5:
            print("Se encuentran en el segundo medio modulo")
            medio_modulo = 2
        elif minutos > 5 and minutos < 55:
            print("Se encuentran en el tercero medio modulo")
            medio_modulo = 3 
        else:
            print("Se encuentran en el cuarto medio modulo")
            medio_modulo = 4

    elif hora == 10: 
        if minutos < 35:
            print("Se encuentran en el cuarto medio modulo")
            medio_modulo = 4
        else:
            print("Se encuentran en el quinto medio modulo")
            medio_modulo = 5 

    if hora == 11:
        if minutos <= 30:
            print("Se encuentran en el quinto medio modulo")
            medio_modulo = 5
        else:  # cuando minutos > 30
            print("Se encuentran en el sexto medio modulo")
            medio_modulo = 6

    elif hora == 12: 
        if minutos < 10:
            print("Se encuentran en el sexto medio modulo")
            medio_modulo = 6
        else:  # cuando minutos > 20
            print("Se encuentran en el septimo medio modulo")
            medio_modulo = 7

    elif hora == 13: 
        if minutos < 1:
            print("Se encuentran en el septimo medio modulo")
            medio_modulo = 7
        else:  # cuando minutos > 1 para cuando sean las 14
            print("Se encuentran en el octavo medio modulo")
            medio_modulo = 8

    elif hora == 14: 
        if minutos < 40:
            print("Se encuentran en el octavo medio modulo")
            medio_modulo = 8
        else:  # cuando minutos > 20
            print("Se encuentran en el noveno medio modulo")
            medio_modulo = 9

    elif hora == 15: 
        if minutos < 20:
            print("Se encuentran en el noveno medio modulo")
            medio_modulo = 9
        else:  # cuando minutos > 30
            print("Se encuentran en el decimo medio modulo")
            medio_modulo = 10

    elif hora == 16: 
        if minutos < 10:
            print("Se encuentran en el decimo medio modulo")
            medio_modulo = 10
        elif minutos <=50 and minutos > 10:   
            print("Se encuentran en el decimo primero medio modulo")
            medio_modulo = 11
        else: 
            print("Se encuentran en el decimo segundo medio modulo")
            medio_modulo = 12

    elif hora == 17: 
        if minutos < 40:
            print("Se encuentran en el decimo segundo medio modulo")
            medio_modulo = 12
        else:  # cuando minutos > 10 
            print("Se encuentran en el decimo tercero medio modulo")
            medio_modulo = 13

    elif hora == 18: 
        if minutos < 20:
            print("Se encuentran en el decimo tercer medio modulo")
            medio_modulo = 13
        else:  # cuando minutos > 10 
            print("Qué haces acá flaco, andate pa' ya bobo")
            medio_modulo = 0
    
    else:
        print("Qué haces acá flaco, andate pa' ya bobo")
        medio_modulo = 0

    
    return medio_modulo