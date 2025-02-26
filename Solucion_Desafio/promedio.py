def obtener_calificaciones():
    calificaciones = []
    for i in range(5):
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
                if 0 <= calificacion <= 100:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return calificaciones

def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    elif 40 <= promedio < 60:
        return "En recuperación"
    else:
        return "Reprobado"

def main():
    calificaciones = obtener_calificaciones()
    promedio = calcular_promedio(calificaciones)
    estado = determinar_estado(promedio)
    print(f"El promedio es: {promedio:.2f}")
    print(f"El estudiante está: {estado}")

if __name__ == "__main__":
    main()