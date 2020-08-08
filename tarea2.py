import time
visited = [False, False, False, False, False, False, False, False, False]

def definir_estado(estado):
    if(estado == 1):
        return ['A', 'DIRTY', 'DIRTY']
    elif(estado == 2):
        return ['A', 'DIRTY', 'CLEAN']
    elif(estado == 3):
        return ['A', 'CLEAN', 'DIRTY']
    elif(estado == 4):
        return ['A', 'CLEAN', 'CLEAN']
    elif(estado == 5):
        return ['B', 'DIRTY', 'DIRTY']
    elif(estado == 6):
        return ['B', 'DIRTY', 'CLEAN']
    elif(estado == 7):
        return ['B', 'CLEAN', 'DIRTY']
    elif(estado == 8):
        return ['B', 'CLEAN', 'CLEAN']

def reflex_agent(location, state):
    if state == "DIRTY":
        return 'CLEAN'
    elif location == 'A':
        return 'RIGHT'
    elif location == 'B':
        return 'LEFT'


def all_visited():
    if(visited[0] == True and visited[1] == True and visited[2] == True and visited[3] == True and visited[4] == True and visited[5] == True and visited[6] == True and visited[7] == True):
        return True
    else:
        return False


def imprimir_estado(estadoA, estadoB, posicion):
    if(estadoA == 'DIRTY' and estadoB == 'DIRTY' and posicion == 'A'):
        print("ESTADO 1")
        visited[0] = True
        return
    elif(estadoA == 'DIRTY' and estadoB == 'CLEAN' and posicion == 'A'):
        print("ESTADO 2")
        visited[1] = True
        return
    elif(estadoA == 'CLEAN' and estadoB == 'DIRTY' and posicion == 'A'):
        print("ESTADO 3")
        visited[2] = True
        return
    elif(estadoA == 'CLEAN' and estadoB == 'CLEAN' and posicion == 'A'):
        print("ESTADO 4")
        visited[3] = True
        return
    elif(estadoA == 'DIRTY' and estadoB == 'DIRTY' and posicion == 'B'):
        print("ESTADO 5")
        visited[4] = True
        return
    elif(estadoA == 'DIRTY' and estadoB == 'CLEAN' and posicion == 'B'):
        print("ESTADO 6")
        visited[5] = True
        return
    elif(estadoA == 'CLEAN' and estadoB == 'DIRTY' and posicion == 'B'):
        print("ESTADO 7")
        visited[6] = True
        return
    elif(estadoA == 'CLEAN' and estadoB == 'CLEAN' and posicion == 'B'):
        print("ESTADO 8")
        visited[7] = True
        return


def test(lado_inicial, states):
    bandera_limpio = 1
    contador = 0
    while bandera_limpio:
        location = states[0]

        state = (states[2], states[1])[states[0] == 'A']

        action = reflex_agent(location, state)
        imprimir_estado(states[1], states[2], states[0])
        if contador == 0 and states[2] == 'CLEAN'and states[1] == 'CLEAN':
            if(lado_inicial == 'A'):
                states[1] = 'DIRTY'
            else:
                states[2] = 'DIRTY'
            contador = contador + 1
        if contador == 1 and states[2] == 'CLEAN'and states[1] == 'CLEAN':
            states[1] = 'DIRTY'
            states[2] = 'DIRTY'
            contador = contador + 1
        if all_visited():
            bandera_limpio = 0

        print("---------")
        if action == "CLEAN":
            if location == 'A':
                states[1] = "CLEAN"
            elif location == 'B':
                states[2] = "CLEAN"
        elif action == "RIGHT":
            states[0] = 'B'
        elif action == "LEFT":
            states[0] = 'A'

        time.sleep(3)


def sucesores(n):
    if n == 1:
        return [3]
    elif n == 2:
        return [4]
    elif n == 3:
        return [1, 7]
    elif n == 4:
        return [2, 3, 8]
    elif n == 5:
        return [7]
    elif n == 6:
        return [2, 5]
    elif n == 7:
        return [8]
    elif n == 8:
        return [4, 6, 7]
    else:
        return None


def anchura(nodo_inicio, nodo_fin):
    lista = [nodo_inicio]
    while lista:
        nodo_actual = lista.pop(0)
        print(nodo_actual)
        if nodo_actual == nodo_fin:
            return print("SOLUCIÓN")
        temp = sucesores(nodo_actual)
        # temp.reverse()
        print(temp)
        if temp:
            lista.extend(temp)
            # print(lista)
    print("NO-SOLUCIÓN")


def profundidad(nodo_inicio, nodo_fin):
    lista = [nodo_inicio]
    while lista:
        nodo_actual = lista.pop(0)
        print(nodo_actual)
        if nodo_actual == nodo_fin:
            # print(len(lista))
            return print("SOLUCIÓN")
        temp = sucesores(nodo_actual)
        temp.reverse()
        print(temp)
        if temp:
            temp.extend(lista)
            lista = temp
           # print(lista)
    print("NO-SOLUCIÓN")

def recorrerTodo():
    print("Ingrese estado inicial del 1 al 8:")
    estado_inicial = int(input())
    arreglo_inicial = definir_estado(estado_inicial)
    lado_inicio = arreglo_inicial[0]
    test(lado_inicio, arreglo_inicial)

def busquedaPorAnchura():
    print("Ingrese estado inicial del 1 al 8:")
    estado_inicial = int(input())
    print("Ingrese estado final del 1 al 8:")
    estado_final = int(input())
    print("INICIO")
    anchura(estado_inicial,estado_final)
    print("FIN")
def busquedaPorProfundidad():
    print("Ingrese estado inicial del 1 al 8:")
    estado_inicial = int(input())
    print("Ingrese estado final del 1 al 8:")
    estado_final = int(input())
    print("INICIO")
    profundidad(estado_inicial,estado_final)
    print("FIN")

if __name__ == "__main__":
    bandera_salida= True
    while(bandera_salida):
        print("Ingrese una opcion:")
        print("1. Recorrer todo")
        print("2. Busqueda por anchura")
        print("3. Busqueda por profundida")
        print("4. Salir")
        seleccion = int(input())
        if(seleccion==1):
            recorrerTodo()
        elif(seleccion==2):
            busquedaPorAnchura()
        elif(seleccion==3):
            busquedaPorProfundidad()
        else:
            bandera_salida=False
