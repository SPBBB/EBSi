# input informations about solar panel power and print it. 
solar_panel_area = float(input("solar panel area (m^2): "))
efficiency_rate = float(input("efficiency (%): "))/100
sunlight = float(input("sunlight (W/m^2): "))
hours = float(input("hours: "))
print("total generated energy={:.2f} kWh".format(solar_panel_area*efficiency_rate*sunlight*hours/1000))