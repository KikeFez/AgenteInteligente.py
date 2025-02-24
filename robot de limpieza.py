import random
import time

class AgenteInteligente:
    def __init__(self, entorno):
        self.entorno = entorno
        self.acciones_posibles = ["aspirar", "revisar_entorno", "navegar"]
        self.tabla_q = {}  # Tabla Q para el aprendizaje por refuerzo
        self.posicion_actual = (0, 0)  # Posición inicial del robot
        self.diametro_robot = 35  # Diámetro del robot en cm
        self.altura_robot = 9  # Altura del robot en cm
        self.bateria = 100  # Nivel de batería en porcentaje
        self.horas_transcurridas = 0

    def percibir_entorno(self):
        print("El robot está percibiendo el entorno.")
        for i in range(6):
            for j in range(6):
                estado = self.entorno[(i, j)]
                if estado:
                    print(f"Posición: ({i}, {j}) - Estado: {estado}")
        print("Posición actual del robot:", self.posicion_actual)
        time.sleep(0.5)

    def actuar(self):
        print("El robot está tomando decisiones y actuando en el entorno.")
        time.sleep(0.5)
        if self.horas_transcurridas >= 2:
            self.horas_transcurridas = 0
            self.ir_a_recargar_si_es_necesario()
        else:
            decision = self.tomar_decision()
            if decision == "aspirar":
                self.aspirar()
            elif decision == "revisar_entorno":
                self.revisar_entorno()
            elif decision == "navegar":
                self.navegar()

    def tomar_decision(self):
        if "O" in self.entorno.values() or "Y" in self.entorno.values():
            return "aspirar"
        else:
            return "revisar_entorno"

    def aspirar(self):
        print("El robot está aspirando.")
        time.sleep(0.5)
        self.bateria -= 1
        if self.entorno[self.posicion_actual] == "O":
            self.entorno[self.posicion_actual] = None
            print("El robot ha aspirado la suciedad 'O' en la posición:", self.posicion_actual)
        elif self.entorno[self.posicion_actual] == "Y":
            print("El robot no puede aspirar la suciedad 'Y' en la posición:", self.posicion_actual)

    def ir_a_recargar_si_es_necesario(self):
        print("Han transcurrido 2 horas. El robot está yendo a su estación de recarga.")
        time.sleep(0.5)
        if self.bateria <= 15:
            self.ir_a_recargar()

    def ir_a_recargar(self):
        print("El nivel de batería es bajo. El robot está recargando su batería.")
        time.sleep(0.5)
        self.bateria += 5
        if self.bateria >= 100:
            self.bateria = 100
            print("La batería está completamente cargada. El robot retoma sus funciones.")
        else:
            print("La batería se está cargando. Espere 20 minutos.")

    def navegar(self):
        print("El robot está navegando.")
        time.sleep(0.5)
        movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for movimiento in movimientos:
            nueva_posicion = (self.posicion_actual[0] + movimiento[0], self.posicion_actual[1] + movimiento[1])
            if self.validar_posicion(nueva_posicion):
                self.posicion_actual = nueva_posicion
                print("El robot se ha movido a la posición:", self.posicion_actual)
                return
        print("El robot está bloqueado y no puede moverse.")

    def validar_posicion(self, posicion):
        return 0 <= posicion[0] < 6 and 0 <= posicion[1] < 6 and not self.hay_obstaculo(posicion)

    def hay_obstaculo(self, posicion):
        return self.entorno.get(posicion) == "X" or self.entorno.get(posicion) == "mueble"

    def pasar_tiempo(self):
        if self.bateria < 100:
            self.bateria += random.randint(5, 10)
            if self.bateria > 100:
                self.bateria = 100
        self.horas_transcurridas += 1

# Función para obtener el entorno (habitación con suciedad en el suelo)
def obtener_entorno():
    entorno = {}
    for i in range(6):
        for j in range(6):
            entorno[(i, j)] = None

    for _ in range(2):
        mueble_pos = (random.randint(0, 5), random.randint(0, 5))
        while entorno[mueble_pos] is not None:
            mueble_pos = (random.randint(0, 5), random.randint(0, 5))
        entorno[mueble_pos] = "mueble"

    for _ in range(2):
        obstaculo_pos = (random.randint(0, 5), random.randint(0, 5))
        while entorno[obstaculo_pos] is not None:
            obstaculo_pos = (random.randint(0, 5), random.randint(0, 5))
        entorno[obstaculo_pos] = "X"

    for _ in range(2):
        suciedad_pos = (random.randint(0, 5), random.randint(0, 5))
        while entorno[suciedad_pos] is not None:
            suciedad_pos = (random.randint(0, 5), random.randint(0, 5))
        entorno[suciedad_pos] = "O"

    for _ in range(3):
        suciedad_pos = (random.randint(0, 5), random.randint(0, 5))
        while entorno[suciedad_pos] is not None:
            suciedad_pos = (random.randint(0, 5), random.randint(0, 5))
        entorno[suciedad_pos] = "Y"

    return entorno

# Uso del agente inteligente (robot de limpieza)
entorno = obtener_entorno()
robot_limpieza = AgenteInteligente(entorno)

# Simulación del paso del tiempo
for _ in range(24):  # Simulamos 24 horas
    robot_limpieza.percibir_entorno()
    robot_limpieza.actuar()
    robot_limpieza.pasar_tiempo()


