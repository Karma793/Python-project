class Vehicle:
    def __init__(self,make,model,weight,year,maintanence,trip):
        self.Make=make
        self.Model=model
        self.Year=year
        self.Weight=weight
        self.Nmaint=maintanence
        self.Trip=trip
    def maintanence(self):
        self.Nmaint=True
        if self.Nmaint==True:
            print("Your car needs to be repaired")
            self.Repair=input("If you want to repair your "+self.Model+" car please enter 'yes'\n If you dont want to then press 'no'\n")
            if self.Repair=='yes':
                self.Trip=0
                print("Your car has been repaired THANK YOU")
            elif self.Repair=='no':
                print("WARNING:Please dont drive your car at this condition")
            else:
                print("you have entered a wrong option please enter again")
class Car(Vehicle):
    def __init__(self,make,model,weigth,year,maintanence,trip,driving,repair):
        Vehicle.__init__(self,make,model,weigth,year,maintanence,trip)
        self.Drive=driving
        self.Repair=repair
    def start(self):
        self.Drive=True
    def stop(self):
        self.Drive=False
        self.Trip +=1
        if self.Trip >100:
            Vehicle.maintanence(self)
    def __str__(self):
        return("Make: "+self.Make+"\nModel: "+self.Model+"\nYear: "+str(self.Year)+"\nWeight: "+self.Weight+"\nNeed maintanence: "+str(self.Nmaint)+"\nTrip since maintanence: "+str(self.Trip))
minicooper=Car('german','XX20','450 KG',2010,False,0,False,'no')
swift=Car('japan','RR213','300 KG',2014,False,0,False,'no')
scorpio=Car('japan','TRF54','500 KG',2010,False,0,False,'no')
for run in range(80):
    minicooper.start()
    minicooper.stop()
for run in range(70):
    swift.start()
    swift.stop()
for run in range(103):
    scorpio.start()
    scorpio.stop()
print(minicooper)
print(swift)
print(scorpio)