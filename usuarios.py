from bank_account import CuentaBancaria
class Usuario:
    def __init__(self, name, email, numero_cuenta):
        self.name = name
        self.email = email
        self.mis_cuentas = []
        self.cuenta = CuentaBancaria(numero_cuenta, tasa_interes=0.02, balance=0)	# añadió esta línea
        self.mis_cuentas.append(self.cuenta)
    # otros métodos

    def abrir_nueva_cuenta(self,numero_cuenta):
        nueva_cuenta = CuentaBancaria(numero_cuenta, tasa_interes=0.02, balance=0)
        self.mis_cuentas.append(nueva_cuenta)
        return self

    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto)
        return self

    def hacer_retiro(self, monto):
        self.cuenta.retiro(monto)
        return self

    def mostrar_balance_usuario(self):
        self.cuenta.mostrar_info_cuenta()
        return self

    def mostrar_info_cuenta_usuario(self):
        for cuenta in self.mis_cuentas:
            print(f"La cuenta nro {cuenta.numero_cuenta} tiene un balance de {cuenta.balance}")
        return self

    def hacer_deposito_en_cuenta(self, numero_cuenta, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                cuenta.deposito(monto)
        return self

    def hacer_retiro_en_cuenta(self, numero_cuenta, monto):
        for cuenta in self.mis_cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                cuenta.retiro(monto)
        return self

