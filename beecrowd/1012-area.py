'''
Problema: beecrowd | 1012
Data: 2026.04.23
Estudante: Ian Forbeck
'''

# Objetivo: 

# --- ANÁLISE (LIAC) ---
# Entrada: As variáveis "A" "B" "C"
# Processamento: * e / para calcular a área das formas
# Saída: Resultado dos cálculos das áreas

A, B, C = input().split()
# Vai receber os valores das variávies

A = float(A)
B = float(B)
C = float(C)
# Transforma as variáveis em pontos flutuantes
triangulo = (A * C / 2)
# Fórmula da área do triângulo
circulo = (3.14159 * C**2)
# Fórmula da área do círculo
trapezio = ((A + B)*C/2)
# Fórmula da área do trapezio
quadrado = (B * B)
# Fórmula da área do quadrado
retangulo = (A * B)
# Fórmula da área do retangulo

print(f"TRIANGULO: {triangulo:.3F}")
print(f"CIRCULO: {circulo:.3f}")
print(f"TRAPEZIO: {trapezio:.3f}")
print(f"QUADRADO: {quadrado:.3f}")
print(f"RETANGULO: {retangulo:.3f}")
# Mostra o valor das áres calculadas