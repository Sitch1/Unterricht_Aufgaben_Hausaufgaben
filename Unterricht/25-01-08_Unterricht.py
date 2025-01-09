# class Vehicles:
#     def __init__(
#         self, vehicle_brand_name, vehicle_model_name, average_consumption_in_l
#     ):
#         self.brand_name = vehicle_brand_name
#         self.model_name = vehicle_model_name
#         self.consumption = average_consumption_in_l
#         self.km_driven = 0

#     def get_description(self):
#         return self.brand_name + ", " + self.model_name

#     def drive(self, km_driven):
#         self.km_driven = self.km_driven + km_driven

#     def get_total_consumption(self):
#         cons_in_l_per_km = self.consumption / 100

#         return cons_in_l_per_km * self.km_driven


# my_vehicle = Vehicles("VW", "Golf", 10)
# my_vehicle.drive(1000)
# my_vehicle.drive(50)
# my_vehicle.drive(4000)
# print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")
# Geteilt in


class Vehicles:
    def __init__(
        self,
        vehicle_brand_name,
        vehicle_model_name,
        average_consumption_in_l,
        tanke_grosse,
    ):
        self.brand_name = vehicle_brand_name
        self.model_name = vehicle_model_name
        self.consumption = average_consumption_in_l
        self.km_driven = 0
        self.tanke_grosse = tanke_grosse

    def get_description(self):
        return self.brand_name + ", " + self.model_name

    def drive(self, km_driven):
        self.km_driven = self.km_driven + km_driven

    def get_total_consumption(self):
        cons_in_l_per_km = self.consumption / 100

        return cons_in_l_per_km * self.km_driven

    def anzeig_tanke(self):
        nutz_tank = self.km_driven * self.get_total_consumption()
        if self.tanke_grosse > nutz_tank:
            print("Auto kannt weiter fahren.")
        else:
            print("Auto mussst tanken")


my_vehicle = Vehicles("VW", "Golf", 10, 100)
my_vehicle.drive(1000)
my_vehicle.drive(50)
my_vehicle.drive(4000)
my_vehicle.anzeig_tanke()
print(f"Der gesamte Verbauch liegt bei: {my_vehicle.get_total_consumption()}")



