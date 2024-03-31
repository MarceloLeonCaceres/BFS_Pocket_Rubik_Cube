import utilEstado

start = (3, 4, 5, 0, 1, 2, 6, 7, 8, 9, 10, 11, 15, 16, 17, 12, 13, 14, 18, 19, 20, 21, 22, 23)
Ini = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
IgualIni = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
MayorQueIni = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24)
MenorQueIni = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 22)

EstadoStart = utilEstado.Estado(start)
EstadoIni = utilEstado.Estado(Ini)

print("start < Ini:") 
print(EstadoStart < EstadoIni)
print()

print("MayorQueIni < Ini:")
print(MayorQueIni < Ini)
print()

print("MenorQueIni < Ini:")
print(MenorQueIni < Ini)
print()

print("IgualIni < Ini:")
print(IgualIni < Ini)
print()
print("IgualIni > Ini:")
print(IgualIni > Ini)
print()
print("IgualIni == Ini:")
print(IgualIni== Ini)
print()
