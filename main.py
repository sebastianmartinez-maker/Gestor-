import random as r
import string as s

elements = s.ascii_letters + s.ascii_uppercase + s.digits + s.punctuation
psw = ""
lenght = int(input("Cuántos caracteres deseas"))

for i in range(lenght):
    psw += r.choice(elements)

print(f"Tu contraseña ha sido generada:{psw}")

print("Programa finalizado")