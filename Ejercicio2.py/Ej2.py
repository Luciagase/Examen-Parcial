class Lista:
    def __init__(self, lista):
        self.lista=lista

    def multiplo_de_10_y_menor_que_200(self):
        for num in self.lista:
            if num%10==0 and num<200:
                print(num)
            elif num>300:
                break
        
    def merge_sort(self):
        if len(self.lista) <= 1:
            return self.lista
        
        medio = len(self.lista) // 2
        lista_izquierda=self.lista[:medio]
        lista_derecha=self.lista[medio:]

        lista_izq_ordenada=Lista(lista_izquierda).merge_sort()
        lista_der_ordenada=Lista(lista_derecha).merge_sort()

        return Lista.merge(lista_izq_ordenada, lista_der_ordenada)

    @staticmethod
    def merge(lista_izquierda, lista_derecha):
        resultado = []
        i = 0
        j = 0

        while i<len(lista_izquierda) and j<len(lista_derecha):
            if lista_izquierda[i] < lista_derecha[j]:
                resultado.append(lista_izquierda[i])
                i+=1
            else:
                resultado.append(lista_derecha[j])
                j+=1
        
        resultado += lista_izquierda[i:]
        resultado += lista_derecha[j:]

        return resultado

    def indice_valor(self, valor):
        try:
            indice=self.lista.indez(valor)
            return indice
        except ValueError:
            return -1
        
