A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

triangle = A*C / 2  # Para calcular é base vezes altura dividido por dois
circle = 3.14159 * C ** 2  # Para calcular o raio é pi*are²
trapezium = (A + B) * C / 2  # Para calcular é base menor + base maior * altura / 2
square = B*B  # Area * area
rectangle = A*B  # altura * largura

print('TRIANGULO: {:.3f}'.format(triangle))
print('CIRCULO: {:.3f}'.format(circle))
print('TRAPEZIO: {:.3f}'.format(trapezium))
print('QUADRADO: {:.3f}'.format(square))
print('RETANGULO: {:.3f}'.format(rectangle))


