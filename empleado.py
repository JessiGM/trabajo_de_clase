import random

# Datos de ejemplo para los empleados
num_empleados = 1897
salario_base = 1300000 #3000
comision_porcentaje = 0.05
tasa_seguridad_social = 0.10

# Función para calcular el salario neto
def calcular_salario_neto(salario_base, comision, tasa_seguridad_social):
    salario_bruto = salario_base + comision
    deduccion_seguridad_social = salario_bruto * tasa_seguridad_social
    salario_neto = salario_bruto - deduccion_seguridad_social
    return salario_neto

# Generar información de los empleados
empleados = []
for i in range(num_empleados):
    ventas = random.uniform(10000, 50000)  # Ventas aleatorias entre 10,000 y 50,000
    comision = ventas * comision_porcentaje
    salario_neto = calcular_salario_neto(salario_base, comision, tasa_seguridad_social)
    empleados.append({
        'Empleado_ID': i + 1,
        'Ventas': round(ventas, 2),
        'Comision': round(comision, 2),
        'Salario_Neto': round(salario_neto, 2)
    })

# Imprimir listado de información
print(f"{'Empleado_ID':<12} {'Ventas':<10} {'Comision':<10} {'Salario_Neto':<15}")
print("="*47)
for empleado in empleados:
    print(f"{empleado['Empleado_ID']:<12} {empleado['Ventas']:<10.2f} {empleado['Comision']:<10.2f} {empleado['Salario_Neto']:<15.2f}")
