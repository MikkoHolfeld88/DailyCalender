def fahrenheit(T_in_celsius):
    return (T_in_celsius * 9 / 5) + 32 #return the temp in Fahrenheit based on Celsius

for t in (20,24,25.5):
    print(t, ": ", fahrenheit(t))

def begrueßen(name="Du da"):
    """ Begrüßt eine Person. """
    print("Hallo " + name + "!")

# calls begrueßen Funktion

begrueßen("Mikko")
begrueßen()

print("Docstring der Funktion begrueßen() ist: " + begrueßen.__doc__)
