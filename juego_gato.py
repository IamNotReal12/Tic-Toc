import random

print("=" * 40)
print("          🎮  TRIQUI (TIC-TAC-TOE)  🎮          ")
print("=" * 40)

print(" Las fichas se colocarán usando coordenadas.")
print("-" * 40)


matriz = [["-" for c in range(3)] for f in range(3)]
for fila in matriz:
    print(fila)


TurnoJugador = random.choice(["X", "O"])
TurnoNumero = 0


def VerificarGanador(matriz, jugador):
    for i in range(3):
        if (
            matriz[i][0] == jugador
            and matriz[i][1] == jugador
            and matriz[i][2] == jugador
        ):
            return True

        if (
            matriz[0][i] == jugador
            and matriz[1][i] == jugador
            and matriz[2][i] == jugador
        ):
            return True
        
    if matriz[0][0] == jugador and matriz[1][1] == jugador and matriz[2][2] == jugador:
        return True
    if matriz[0][2] == jugador and matriz[1][1] == jugador and matriz[2][0] == jugador:
        return True
    
    return False    


while TurnoNumero < 9:
    print("\n--- Sistema Turnos ⚔️ ---")
    print(f"Turno número {TurnoNumero + 1}")
    print(f"Le toca al jugador: {TurnoJugador}")

    Fila = int(input(f"Ingresa el numero de la fila jugador {TurnoJugador}: "))
    Columna = int(input(f"Ingresa el numero de la columna {TurnoJugador}: "))
    if not(1 <= Fila <= 3) or not(1<= Columna <= 3):
        print("Ingresa un numero menor o igual a 3")
        continue
    if matriz[Fila - 1][Columna - 1] == "-":
        matriz[Fila - 1][Columna - 1] = TurnoJugador

        for tablero in matriz:
            print(tablero)
        
        if VerificarGanador(matriz,TurnoJugador):
            print("Has ganado...🎉")
            break    

        if TurnoJugador == "X":
            TurnoJugador = "O"
        elif TurnoJugador == "O":
            TurnoJugador = "X"
        TurnoNumero += 1

    else:
        print("\n⚠️ ¡Esa casilla ya está ocupada! Elige otra.")

    if TurnoNumero == 9 and not VerificarGanador(matriz,"X") and not VerificarGanador(matriz,"O"):
        print("Empate...")
        break
    
