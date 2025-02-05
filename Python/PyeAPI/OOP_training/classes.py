class Coche:
    def __init__ (self, marca_id, modelo_id):
        self.marca = marca_id
        self.modelo = modelo_id
    
    def tipo_movimento(self):
        print ("Se mueve por la carretera en 4 ruedas ...")

    def get_caracteristicas(self):
        print (f"Soy un {self.marca} {self.modelo}")

class Avion(Coche):
    def __init__ (self, marca_id, modelo_id, faa_id):
        super().__init__(marca_id, modelo_id)
        self.faa = faa_id

    def tipo_movimento(self):
        print ("Vuela por el aire ...")

    def get_caracteristicas(self):
        print (f"Soy un {self.marca} {self.modelo} con FAA {self.faa:.2f}")

class Camion(Coche):
    def tipo_movimento(self):
        print ("Se mueve por la carretera en 8 o mas ruedas ...")

class GolfCarro(Coche):
    pass

class DoItRight(Exception):
    pass

mi_coche = Coche('Tesla', 'Modelo 1')
tu_coche = Coche('Audi', 'Modelo 5')
try:
    mi_avion = Avion("embraer", "Tucano", 345)
    raise DoItRight("lo has hecho muuuuy bien")
except Exception as error:
    print(error)
else:
    print("Lo has hecho bien")
finally:
    print('Todo OK')
mi_camion = Camion("Mercedes", "Sprinter4")
mi_golf = GolfCarro('Yamaha', 'GC203')

for x in (mi_coche, tu_coche, mi_avion, mi_camion, mi_golf):
    try:
        x.get_caracteristicas()
        x.tipo_movimento
    except Exception as error:
        print(error)
    else:
        print('No errors')

# mi_coche.get_caracteristicas()
# mi_coche.tipo_movimento()
# mi_avion.get_caracteristicas()
# mi_avion.tipo_movimento()
# mi_camion.get_caracteristicas()
# mi_camion.tipo_movimento()
# mi_golf.get_caracteristicas()
# mi_golf.tipo_movimento()


