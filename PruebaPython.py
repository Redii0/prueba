

animales = ["caballo","camello","gato","perro"]
 
while (True):
	print("Ingrese una opcion (1-añadir, 2-eliminar, 3-buscar, 4-ordenar, 0-terminar): ")
	Opcion = int( input())

	if Opcion == 1:
		print("verifiquemos la lista de animales:")
		print(animales)
		i = input("Ingrese el Animal: ")
		animales.append(i)

	if Opcion == 2:
		if animales >= 0:
			print("verifiquemos la lista de animales:")
			print(animales)
			i = input("Ingrese el Animal a borrar: ")
			animales.remove(i)

	if Opcion == 3:
		print("Ingrese el nombre del animal a buscar:")
		h = input()

		j = animales.index(h)
		print(j-1)
		print(j+1)

	else:
			print("el animal no se ha encontrado")

	if Opcion == 4:
		animales.sort()
		print(animales)

	if Opcion == 0:
		break
