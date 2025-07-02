from enum import Enum

class EstadoSalud(Enum):
    BAJISIMO = -1
    ADECUADO = 0
    SOBRANTE = 1
    CRITICO = 2
    EXTREMO = 3

class Sujeto:
    _registro_global = 1

    def __init__(self, folio="", alias="", ciclo=0, tipo='M', masa=0.0, largo=0.0):
        self._folio = folio
        self._alias = alias
        self._ciclo = ciclo
        self._tipo = self._verificaTipo(tipo)
        self._masa = masa
        self._largo = largo
        self._identificador = self._generaID()

    @classmethod
    def parcial(cls, folio, alias, ciclo, tipo):
        return cls(folio, alias, ciclo, tipo)

    @classmethod
    def vacio(cls):
        return cls()

    def evaluarCorporal(self):
        if self._largo == 0:
            return None
        calculo = self._masa / ((self._largo / 100) ** 2)
        if calculo < 18.5:
            return EstadoSalud.BAJISIMO
        elif calculo <= 24.9:
            return EstadoSalud.ADECUADO
        elif calculo <= 29.9:
            return EstadoSalud.SOBRANTE
        elif calculo <= 39.9:
            return EstadoSalud.CRITICO
        else:
            return EstadoSalud.EXTREMO

    def esAdulto(self):
        return self._ciclo >= 18

    def _verificaTipo(self, tipo):
        return tipo if tipo in ('M', 'F') else 'M'

    def _generaID(self):
        temp = Sujeto._registro_global
        Sujeto._registro_global += 1
        return temp

    def describir(self):
        estado = self.evaluarCorporal()
        if estado:
            texto_estado = estado.name.capitalize()
        else:
            texto_estado = "Desconocido"
        genero = "Masculino" if self._tipo == 'M' else "Femenino"
        return (f"Hola {self._alias}, tu código dentro del sistema es {self._identificador}. "
                f"Tu identificación es {self._folio}. Tu edad es {self._ciclo} años. "
                f"Tu género es {genero}. Tu Peso es {self._masa} kg y tu Altura es {self._largo} cm. "
                f"Al calcular tu IMC concluimos que tu peso está: {texto_estado}.")

    @property
    def folio(self):
        return self._folio

    @folio.setter
    def folio(self, valor):
        self._folio = valor

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, valor):
        self._alias = valor

    @property
    def ciclo(self):
        return self._ciclo

    @ciclo.setter
    def ciclo(self, valor):
        self._ciclo = valor

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        self._tipo = self._verificaTipo(valor)

    @property
    def masa(self):
        return self._masa

    @masa.setter
    def masa(self, valor):
        self._masa = valor

    @property
    def largo(self):
        return self._largo

    @largo.setter
    def largo(self, valor):
        self._largo = valor

def main_sujeto():
    def obtener_datos():
        f = input("Folio: ")
        a = input("Alias: ")
        c = int(input("Ciclo (edad): "))
        t = input("Tipo (M/F): ").upper()
        m = float(input("Masa (kg): "))
        l = float(input("Largo (cm): "))
        return f, a, c, t, m, l

    f, a, c, t, m, l = obtener_datos()
    sujeto1 = Sujeto(f, a, c, t, m, l)
    sujeto2 = Sujeto.parcial(f, a, c, t)
    sujeto3 = Sujeto.vacio()
    sujeto3.folio = "X0001"
    sujeto3.alias = "Beatriz León"
    sujeto3.ciclo = 28
    sujeto3.tipo = 'F'
    sujeto3.masa = 55.5
    sujeto3.largo = 162.0

    lote = [sujeto1, sujeto2, sujeto3]

    for idx, p in enumerate(lote, 1):
        print(f"\n--- Sujeto {idx} ---")
        print("¿Es adulto?:", "Sí" if p.esAdulto() else "No")
        print(p.describir())

    repetir = input("\n¿Registrar otro sujeto? (S/N): ").strip().upper()
    if repetir == "S":
        main_sujeto()

# Descomenta para ejecutar
# main_sujeto()