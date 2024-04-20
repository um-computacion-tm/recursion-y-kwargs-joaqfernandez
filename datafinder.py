import unittest

def buscar_datos(*args, **kwargs):
    set_argumento = set(args)
    listado_personas = []
    
    for persona, datos in kwargs.items(): 
        set_datos = set(datos.values())

        if set_argumento.issubset(set_datos):  #Verifica si los valores de los argumentos
                                               #pasados son "subconjunto" de los datos en database.       
            listado_personas.append(persona)

    if listado_personas:
        return listado_personas                
    
    else:
        return "Los datos solicitados no se encuentran dentro de la base" 
database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Martin",
        "segundo_nombre": "Gustavo",
        "primer_apellido": "Rodriguez",
        "segundo_apellido": "Quiroga"
    },
    "persona3": {
        "primer_nombre": "Joaquin",
        "segundo_nombre": "Alberto",
        "primer_apellido": "Fernandez",
        "segundo_apellido": "Leuzzi"
    },
    "persona4": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Marcos",
        "primer_apellido": "Lucero",
        "segundo_apellido": "Gonzalez"
    },               
}
                                  


class TestInDatabase(unittest.TestCase):

    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, ["persona1"])
    
    def test_persona2(self):
        resultado = buscar_datos("Martin", "Gustavo", "Rodriguez", "Quiroga", **database)
        self.assertEqual(resultado, ["persona2"])
    
    def test_persona3(self):
        resultado = buscar_datos("Joaquin", "Alberto","Fernandez","Leuzzi", **database)
        self.assertEqual(resultado, ["persona3"])
    
    def test_persona4(self):
        resultado = buscar_datos("Elias", "Marcos", "Lucero", "Gonzalez", **database)
        self.assertEqual(resultado, ["persona4"])
    
    def test_personas_iguales(self):
        resultado = buscar_datos("Pablo", **database)
        self.assertEqual(resultado, ["persona2","persona3"])

    def  test_datos_mezclados(self):      
        resultado = buscar_datos("Alberto", "Marcos", "Rodriguez", "Ruiz", **database)
        self.assertEqual(resultado, ["persona1"])

    def  test_persona_no_existe(self):      
        resultado = buscar_datos("Gonzalo", "Pepe", "Stefano", "Tejada", **database)
        self.assertEqual(resultado, "En la base de datos no existen dichos datos")

if __name__ == "__main__":
    unittest.main()