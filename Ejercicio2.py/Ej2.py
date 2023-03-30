class Lista:
    def __init__(self, lista):
        self.lista=lista

    def multiplo_de_10_y_menor_que_200(self):
        for num in self.lista:
            if num%10==0 and num<200:
                print(num)
            elif num>300:
                break
        