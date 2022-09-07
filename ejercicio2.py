import pickle

class Vehiculo:
    ruedas = 4
    puertas = 5
    marca = 'Honda'

    def getMarca(self):
        return self.marca


# Save
v1 = Vehiculo()
f = open('vehiculo.bin', 'wb')
pickle.dump(v1, f)
f.close()

# Load
f = open('vehiculo.bin', 'rb')
carro = pickle.load(f)
f.close()
print(type(carro))
print(carro.getMarca())
