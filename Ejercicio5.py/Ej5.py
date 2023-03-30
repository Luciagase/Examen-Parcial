class Encriptador:#inicializa dos tablas hash: encriptacion y desencriptacion
    def __init__(self):
        self.encriptacion = {}
        self.desencriptacion = {}
        self.inicializar_tablas()
        
    def inicializar_tablas(self):
        caracteres_legibles = list(range(32, 126))
        caracteres_encriptados = []
        for i in range(len(caracteres_legibles)):
            caracter_encriptado = str(caracteres_legibles[i]).zfill(8)
            caracteres_encriptados.append(caracter_encriptado)
            self.encriptacion[caracteres_legibles[i]] = caracter_encriptado
            self.desencriptacion[caracter_encriptado] = caracteres_legibles[i]
        
    def encriptar(self, texto):#recibe un texto como argumento y recorre cada caracter del texto, encriptándolo si está dentro del rango de caracteres legibles (del 32 al 125) y dejando el caracter original si no lo está.
        texto_encriptado = ""
        for caracter in texto:
            if ord(caracter) in self.encriptacion:
                texto_encriptado += self.encriptacion[ord(caracter)]
            else:
                texto_encriptado += caracter
        return texto_encriptado
        
    def desencriptar(self, texto_encriptado):#recibe un texto encriptado como argumento y recorre cada grupo de 8 caracteres en busca de una versión encriptada. Si encuentra una versión encriptada, la busca en la tabla de desencriptación para obtener el caracter original correspondiente, y lo agrega al texto desencriptado. Si no encuentra una versión encriptada, agrega el grupo de caracteres original al texto desencriptado.
        texto_desencriptado = ""
        i = 0
        while i < len(texto_encriptado):
            if texto_encriptado[i:i+8] in self.desencriptacion:
                texto_desencriptado += chr(self.desencriptacion[texto_encriptado[i:i+8]])
                i += 8
            else:
                texto_desencriptado += texto_encriptado[i]
                i += 1
        return texto_desencriptado
    
# Ejemplo de uso
e = Encriptador()
texto_original = "Hola, ¿cómo estás?"
texto_encriptado = e.encriptar(texto_original)
texto_desencriptado = e.desencriptar(texto_encriptado)

print("Texto original: ", texto_original)
print("Texto encriptado: ", texto_encriptado)
print("Texto desencriptado: ", texto_desencriptado)

