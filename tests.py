class Cilveks: 
    def __init__ (self,vards,vecums,dzimums):
        self.name=vards
        self.age=vecums
        self.sex=dzimums
    def jVards(self, jaunsVards):
        self.name= jaunsVards
    def dzimene(self):
 
        self.age +=1  
    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards
        # self.bazarsPaSevi()
    def mainit_dzimumu(self, jaunais_dzimums = ""):
        if jaunais_dzimums == "":
            if self.sex == "s":
                self.sex = "v"
            else :
                self.sex = "s"
        else:
            self.sex = jaunais_dzimums
        

    def bazarsPaSevi(self):
        if self.sex == "v":
            dzimums = "vīrietis"
        elif self.sex == "s":
            dzimums = "sieviete"
        else:
            dzimums = self.sex

        return "Sveiki, mani sauc {} man ir {} gadi un es esmu {}".format(self.name, self.age, dzimums ) 

    def __del__(self):
        print("atā")
        


class Sieviete(Cilveks):
    def __init__(self, name, hair_color, age = 0):
        super().__init__(name, age, "s")
        self.matu_krasa = hair_color
        # self.bazarsPaSevi()
    
    def bazarsPaSevi(self):
        super().bazarsPaSevi()
        print("Mana matu krāsa ir", self.matu_krasa)


# persona = Cilveks("Krišs", 18, "v")
# persona1 = Cilveks("Rada", 16, "s")
# persona2 = Sieviete("Baba", "Melni", 25 )
# persona.mainit_vardu("Anna")
# persona.mainit_dzimumu("")



# persona.dzimene()

# persona2.bazarsPaSevi()

