def ruffier_index(pulso_1: int, pulso_2: int, pulso_3: int) -> float:
     index = (4 * (pulso_1 + pulso_2 + pulso_3) - 200) / 10
     
     return index


def resultado_test_ruffier (name, pulse_1, pulse_2, pulse_3):
    
    index = ruffier_index(pulse_1, pulse_2, pulse_3)

    if index <= 5:
            evaluacion = "Excelente / Muy bueno."
            consejo = "Tu corazón tiene una capacidad de recuperación fantástica."
    elif index <= 10:
        evaluacion = "Bueno (Satisfactorio)."
        consejo = "Tu condición física y la eficiencia de tu corazón están en un buen nivel."
    elif index <= 15:
        evaluacion = "Promedio."
        consejo = "Eficiencia del corazón promedio. Tal vez valga la pena mantener una rutina de ejercicio constante."
    else:
        evaluacion = "Por debajo del promedio (Bajo)."
        consejo = "Tal vez valga la pena hacerse unas pruebas adicionales con el doctor."

        # Construimos el texto final con el mensaje dinámico
    texto_final = (
            f"{name}\n"
            f"Tu índice de Ruffier: {index}\n"
            f"Eficiencia del corazón: {evaluacion}\n"
            f"{consejo}"
        )
        
    return texto_final
    



def check_int(number:str) -> int:
     try:
          return int(number)
     except ValueError:
          return False