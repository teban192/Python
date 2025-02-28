miLista= ["Maria","Pepe","Martha","Antonio"]

miLista.append("Cristian")
miLista.insert(2,"Rodrigo")
miLista.extend(["Sandra","Ana","Lucia"])

print(miLista[:])
print(miLista.index("Pepe"))
miLista.remove("Martha")
miLista.pop()

print("Pepe" in miLista)
print(miLista)


miLista2=["Maria",5,True,78.35]
miLista3=["Sandra","Lucia"]
miLista4= miLista2+miLista3
print(miLista4[:])

