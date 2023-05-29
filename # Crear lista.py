# Crear lista
lista = [2,5,25,100,500]
print("inicial:",lista)

#Append()=agreagar un dato al final de la lista
lista.append(250)
print("Append: ",lista)

#Extend([])=edita una segunda lista para agregar un dato
lista2 = (75,125)
lista.extend(lista2)
print("Extend: ", lista)

#Insert(posicion valor) = agregar dato en posicion de la lista
lista.insert(2,400)
print("Insert: ",lista)

#remove(valor)=busca eliminar el valor seleccionado
lista.remove(400)
print("Remove: ",lista)

#Pop()=elimina el ultimo registro
#Pop(Posicion)=Elimina la opsicion asignada
lista.pop()
print("Pop:    ",lista)
lista.pop(2)
print("Pop(2): ",lista)

#Reverse=cambiar el orden de los factores
lista.reverse()
print("Reverse:",lista)

#Sort=odenar de meno a mayor
lista.sort()
print("Sort:   ",lista)

#Sort(Reverse=true)= ordena de mayor a menor
lista.sort(reverse=True)
print("Sort(r):",lista)