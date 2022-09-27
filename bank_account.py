class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Fondos Insuficientes")
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print("Balance actual: ", self.balance)
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.tasa_interes)  
        return self

    # BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria

    @classmethod
    def imprime_cuentas_bancarias(cls): 
        # utilizamos cls para referirnos a la clase
        for account in cls.todas_las_cuentas:
            account.mostrar_info_cuenta()
