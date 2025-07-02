class ModuloBanco:
    _indice_cuenta = 100001

    def __init__(self, clave="", reserva=0.0, tasa=0.0):
        self._codigo = ModuloBanco._indice_cuenta
        ModuloBanco._indice_cuenta += 1
        self._clave = clave
        self._reserva = reserva
        self._tasa = tasa

    def aplicarInteres(self):
        diario = self._tasa / 365
        self._reserva += self._reserva * (diario / 100)

    def sumarFondos(self, cantidad):
        self._reserva += cantidad

    def extraerFondos(self, cantidad):
        if cantidad <= self._reserva:
            self._reserva -= cantidad
        else:
            print("No hay saldo suficiente.")

    def mostrarEstado(self):
        return (f"Cuenta #{self._codigo} | Documento: {self._clave} | "
                f"Saldo: {self._reserva:.2f} | Interés Anual: {self._tasa}%")