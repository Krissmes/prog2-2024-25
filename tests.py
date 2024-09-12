class Cilveks: 
    def __init__ (self,vards,vecums,dzimums):
        self.name=vards
        self.age=vecums
        self.sex=dzimums
    def dzimene(self):
        self.age +=1  

    def BazarsPaSevi(self):
        if self.sex == "v":
            dzimums = "vīrietis"
        elif self.sex == "s":
            dzimums = "sieviete"
        else:
            dzimums = self.sex

        print("Sveiki, mani sauc {} man ir {} gadi un es esmu {}".format(self.name, self.age, dzimums ) )


persona = Cilveks("Krišs", 18, "v")
persona1 = Cilveks("Rada", 16, "s")



persona.dzimene()

persona.BazarsPaSevi()

