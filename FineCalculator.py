name = input("Enter your name: ")
speed_limit = int(input("Enter the speed limit (km/h): "))
actual_speed = int(input("Enter your actual speed (km/h): "))

excess_speed = actual_speed - speed_limit  # Calculate excess speed

# Check if speed limit was exceeded
is_excess_speed = False
if excess_speed > 0:
    is_excess_speed = True

# Fine starts counting only when speed limit has been exceeded
fine = 0
if is_excess_speed:
    fine = excess_speed * 5
    if fine > 194750:
        fine = 194750

# Print result
print(name + " your fine is: #" + str(fine))
