# Demonstrate the unpacking of sequence of values into separate variables
name = input("Por favor, entre el primer nombre, segundo nombre y primer apellido: ? ").strip().title()
first_name, middle_name, last_name = name.split(' ')
print(first_name)
print(middle_name)
print(last_name)
print(f"Hello, {first_name} {middle_name}")


