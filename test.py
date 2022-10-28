from bank_account import CuentaBancaria
from usuarios import Usuario


usuario1 = Usuario("Fernando Henriquez", "fh@gmail.com", 12345)
usuario1.cuenta.deposito(500)

usuario1.abrir_nueva_cuenta(23456)
usuario1.hacer_deposito_en_cuenta(23456, 400).hacer_retiro_en_cuenta(23456, 100)
usuario1.mostrar_info_cuenta_usuario()

