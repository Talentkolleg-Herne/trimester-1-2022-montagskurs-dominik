meineVariable = "Hallo Welt"
meineZahl = 11

print(meineVariable)
print(meineZahl)


print("Zahl " + "5")
print(10 + 5)


# +
# -
# *
# /

alter = 24
meinAlterInMonaten = alter * 12
meinAlterInTagen = 24 * 365
meinAlterInStunden = meinAlterInTagen * 24
meinAlterInMinuten = meinAlterInStunden * 60

print(24 * 12)
print(meinAlterInMonaten)
print(meinAlterInTagen)

print(meinAlterInStunden)
print(meinAlterInMinuten)

# (1) Umrechnung von Celsius nach Kelvin
# (2) Umrechnung von Celsius nach Fahrenheit
# (3) Umrechnung von Kelvin nach Celsius
# (4) Umrechnung von Kelvin nach Fahrenheit
# (5) Umrechnung von Fahrenheit nach Celsius
# (6) Umrechnung von Fahrenheit nach Kelvin

# Celsius = 5/9 * (Fahrenheit - 32).
# Celsius = Kelvin - 273.15.
# Die tiefste mögliche Temperatur ist den absoluten Nullpunkt 0K.
# °C = (°F - 32) * 5/9 (von Fahrenheit in Celsius) °F = °C * 1,8 + 32 (von Celsius nach Fahrenheit)
# 20 = Kelvin - 273,15

# 20 + 273,15 = Kelvin

temperaturInCelsius = 20

celsiusNachKelvin = temperaturInCelsius + 273.15
celsiusNachFahrenheit = (temperaturInCelsius * 1.8) + 32

print(celsiusNachKelvin)
print(celsiusNachFahrenheit)