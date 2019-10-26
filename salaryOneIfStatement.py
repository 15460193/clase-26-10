salary = int(input('Introduce el salario: \n'))

if salary <= 1000:
    new_salary = salary*1.15
else:
	new_salary = salary*1.12
 
print ('Salario nuevo: ' + str(new_salary))