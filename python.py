#a simple bill spillter which splits the bill accounting for service charge as well


event = input("What was the event or occasion? ")
cost = float(input("How much was it? ")) 
service_charge = int(input("Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): "))
group_size = int(input("How many people were in your group? "))
service_charge_total = (service_charge / 100) * cost
grand_total = service_charge_total + cost
total_per_person = grand_total / group_size
print()
print(f"The cost of the event is ${cost: .2f}, the total service charge is {service_charge_total: .2f} and every person must pay {total_per_person: .2f}")