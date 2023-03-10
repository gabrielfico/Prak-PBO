class Car:
    wheels = 4                              # globat atribut

    def __init__(self, color, model):
        self.color = color                  # atribut public
        self.model = model              
        self._mileage = 0                   # atribut protected
        self.__engine_status = False        # atribut private

    def start_engine(self):                 # fungsi menyalakan mobil
        self.__engine_status = True      
        print("Engine started")

    def stop_engine(self):                  # fungsi mematikan mobil
        self.__engine_status = False
        print("Engine stopped")

    def _update_mileage(self, distance):    # fungsi menambah odometer
        self._mileage += distance

    def drive(self, distance):              # fungsi untuk menjalankan mobil
        if self.__engine_status:
            self._update_mileage(distance)
            print(f"{self.color} {self.model} driven for {distance} km")
        else:
            print("Please start the engine first")

    def get_mileage(self):                  # fungsi untuk menampilkan odometer   
        return self._mileage

    def _reset_mileage(self):               # fungsi untuk mereset odometer
        self._mileage = 0


Mobil1 = Car("red", "Toyota")
print(f"Color: {Mobil1.color}") 
print(f"Model: {Mobil1.model}")
print(f"Wheels: {Mobil1.wheels}")

Mobil1.start_engine()
Mobil1.drive(50)
Mobil1.color = "blue"
print(f"New color: {Mobil1.color}")
print(f"Mileage: {Mobil1.get_mileage()} km")
Mobil1._reset_mileage()
