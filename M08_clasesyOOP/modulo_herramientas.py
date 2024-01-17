class Tools:
    def __init__(self,lista_mumeros):
        self.lista = lista_mumeros

    def verifica_primo(self):
        for i in self.lista:
            if self.__verifica_primo(i):
                print(f'El valor {i} es primo')
            else:
                print(f'El valor {i} no es primo')
        

    def __verifica_primo(self,nro):
        es_primo = True  # Variable para almacenar el resultado de la verificación de número primo
        for i in range(2, nro):  # Iteración sobre los números desde 2 hasta nro-1
            if nro % i == 0:  # Verificación si nro es divisible por i (no es primo)
                es_primo = False  # Se marca la variable como False indicando que el número no es primo
                break  # Se rompe el bucle ya que no es necesario continuar la verificación
        return es_primo  # Se devuelve el resultado de la verificación de número primo



    def valor_modal(self):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(f'El valor {i} de {origen} a {destino} es {self.__conversion_grados(i, origen, destino)}')
    
    def __conversion_grados(self,valor, origen, destino):

        if origen == 'celsius':
            if destino == 'celsius':
                valor_destino = valor  # Si la unidad de origen y destino es la misma, no se realiza ninguna conversión
            elif destino == 'farenheit':
                valor_destino = (valor * 9 / 5) + 32  # Conversión de Celsius a Farenheit
            elif destino == 'kelvin':
                valor_destino = valor + 273.15  # Conversión de Celsius a Kelvin
            else:
                print('Parámetro de Destino incorrecto')  # Mensaje de error si el parámetro de destino no es válido
        elif origen == 'farenheit':
            if destino == 'celsius':
                valor_destino = (valor - 32) * 5 / 9  # Conversión de Farenheit a Celsius
            elif destino == 'farenheit':
                valor_destino = valor  # Si la unidad de origen y destino es la misma, no se realiza ninguna conversión
            elif destino == 'kelvin':
                valor_destino = ((valor - 32) * 5 / 9) + 273.15  # Conversión de Farenheit a Kelvin
            else:
                print('Parámetro de Destino incorrecto')  # Mensaje de error si el parámetro de destino no es válido
        elif origen == 'kelvin':
            if destino == 'celsius':
                valor_destino = valor - 273.15  # Conversión de Kelvin a Celsius
            elif destino == 'farenheit':
                valor_destino = ((valor - 273.15) * 9 / 5) + 32  # Conversión de Kelvin a Farenheit
            elif destino == 'kelvin':
                valor_destino = valor  # Si la unidad de origen y destino es la misma, no se realiza ninguna conversión
            else:
                print('Parámetro de Destino incorrecto')  # Mensaje de error si el parámetro de destino no es válido
        else:
            print('Parámetro de Origen incorrecto')  # Mensaje de error si el parámetro de origen no es válido
    
        return valor_destino

    def factorial(self):
        for i in self.lista:
            print(f'El factorial de {i} es {self.__factorial(i)}')
    
    def __factorial(self,numero):
            # Verifica si el número no es entero y devuelve un mensaje de error
        if type(numero) != int:
            return 'El número debe ser un entero'
    
        # Verifica si el número es negativo y devuelve un mensaje de error
        if numero < 0:
            return 'El número debe ser positivo'
    
            # Caso base: si el número es 0 o 1, el factorial es 1
        if numero <= 1:
            return 1
    
            # Recursión: calcula el factorial del número multiplicándolo por el factorial del número anterior
        numero = numero * self.__factorial(numero - 1)