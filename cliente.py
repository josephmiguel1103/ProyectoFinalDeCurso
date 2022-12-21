from persona import Persona
from utils import limpiarPantalla,continuar

personas: Persona = []

           

def clienteDict():
    x : dict = [{"dni":"5699789","nombre":"carlos","apellido":"quintana","direccion":"av. las moras calle 15","telefono":"934847245" },\
    {"dni":"3576576","nombre":"william","apellido":"osorio","direccion":"av. los olivos calle 14","telefono":"943246834" },\
        {"dni":"4688676","nombre":"cinthia","apellido":"zuni","direccion":"linea 33 avenida","telefono":"911231243" }]
    a=0
    for i in x: 
        persona: Persona = Persona(x[a]["dni"],x[a]["nombre"], x[a]["apellido"],x[a]["direccion"],x[a]["telefono"])
        personas.append(persona)
        a=a+1
        

def persona():
    limpiarPantalla()
    print(" *** ingresar datos del cliente ***\n")
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)
    continuar()

def listar_personas():
    limpiarPantalla()
    print("    DNI     NOMBRES    APELLIDOS   DIRRECCION  TELEFONO\n")
    for persona in personas:
        Persona.convertir_a_string(persona)
    continuar()

limpiarPantalla()

def buscar_persona():
    
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            continuar()
            return persona 
    


def editar_persona():
    limpiarPantalla()
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)
    continuar()

def eliminar_persona():
    limpiarPantalla()
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)
            print("\nSe elimino correctamente el usuario")
    continuar()