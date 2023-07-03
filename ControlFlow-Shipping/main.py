weight=41.5
normalground=0
#Ground shipping
if weight<=2:
  normalground=weight*1.50+20.00
elif weight>2 and weight<=6:
  normalground=weight*3.00+20.00
elif weight>6 and weight<=10:
  normalground=weight*4.00+20.00
else:
  normalground=weight*4.75+20
print("Ground Shipping: $" + str(normalground))
cost_ground_premium=125
print("Ground shipping Premium: $" + str(cost_ground_premium))
#Drone Shipping
if weight<=2:
  drone=weight*4.50
elif weight>2 and weight<=6:
  drone=weight*9.00
elif weight>6 and weight<=10:
  drone=weight*12.00
else:
  drone=weight*14.25
print("Drone Shipping: $" + str(drone))