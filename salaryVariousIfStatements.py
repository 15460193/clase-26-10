category = int(input('Introduce la categoria del empleado [1, 2, 3, 4]: \n'))

if category > 4 or category < 0:
	print ('Categoría no válida')
else:
	salary = int(input('Introduce el salario: \n'))

	if category == 1:
		new_salary = salary * 1.15
	elif category == 2:
		new_salary = salary * 1.10
	elif category == 3:
		new_salary = salary * 1.08
	elif category == 4:
		new_salary = salary * 1.07
	
	print("Salario nuevo: " + str(new_salary))