from bank_account import CuentaBancaria
# Crea 2 cuentas

# Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)

cuenta1 = CuentaBancaria(0.15, 100)
cuenta1.deposito(100).deposito(200).deposito(300).retiro(400).generar_interes().mostrar_info_cuenta()

# Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)

cuenta2 = CuentaBancaria(0.15, 100)
cuenta2.deposito(300).deposito(500).retiro(100).retiro(200).retiro(200).retiro(200).generar_interes().mostrar_info_cuenta()

# print(CuentaBancaria.todas_las_cuentas)
CuentaBancaria.imprime_cuentas_bancarias()