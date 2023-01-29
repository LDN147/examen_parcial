# INGRESO DE DATOS
nombre = input("Escribir su Nombre: ")
sueldo_basico = input("Cual es su sueldo basico: ")
detener = True
while detener:
    try:
        sueldo_basico = int(sueldo_basico)
        detener = False
    except:
        print("El valor ingresado debe ser un numero entero")
        sueldo_basico = input("Cual es su sueldo basico: ")

# DIAS FALTA

diasfalta = input("Cuantos dias falto: ")
detener = True
while detener:
    try:
        diasfalta = int(diasfalta)
        detener = False
    except:
        print("El valor ingresado debe ser un numero entero")
        diasfalta = input("Cuantos dias falto: ")

# MINUTOS TARDANZA

minutosTardanza = input("Cuantos minutos tarde llego: ")
detener = True
while detener:
    try:
        minutosTardanza = int(minutosTardanza)
        detener = False
    except:
        print("El valor ingresado debe ser un numero entero")
        minutosTardanza = input("Cuantos minutos tarde llego: ")

# HORAS EXTRAS

horasExtras = input("Cuantas horas extras trabajo: ")
detener = True
while detener:
    try:
        horasExtras = int(horasExtras)
        detener = False
    except:
        print("El valor ingresado debe ser un numero entero")
        horasExtras = input("Cuantas horas extras trabajo: ")

# Bonificaciones


Pago_por_horas_extras = 1.50 * horasExtras * (sueldo_basico / 30 / 8)
movilidad = 1000
bonificación_suplementaria = 0.03 * sueldo_basico
bonificaciones = movilidad + bonificación_suplementaria + Pago_por_horas_extras
remuneracion_computable = sueldo_basico + movilidad + bonificación_suplementaria

# descuentos

Remuneracion_minima = sueldo_basico + bonificaciones
Descuento_Faltas = remuneracion_computable / (30 * diasfalta)
descuentoTardanzas = (((remuneracion_computable / 30) / 8) / 60) * minutosTardanza
descuentos = Descuento_Faltas + descuentoTardanzas

sueldo_neto = sueldo_basico + bonificaciones - descuentos
print("================================================")
print("Nombre del Trabajador:", nombre)
print("Sueldo base:", sueldo_basico)
print("================================================")
print("BONIFICACIONES")
print("Pago por horas extras:", Pago_por_horas_extras)
print("Movilidad", movilidad)
print("Bonificacion Suplementaria:", bonificación_suplementaria)
print("Bonificaion Total:", bonificaciones)
print("================================================")
print("DESCUENTOS")
print("Descuento por faltas:", Descuento_Faltas)
print("Descuento por tardanza:", descuentoTardanzas)
print("Descuento Total:", descuentos)
print("================================================")
print("Sueldo Total:", sueldo_neto)

