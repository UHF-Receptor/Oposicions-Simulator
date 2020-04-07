import random
a = 1+ (70*random.random()) // 1
b=a
while b ==a:
    b =1+ (70*random.random()) // 1
c=b
while c == a or c ==b:
    c = 1+(70*random.random()) // 1

d=b
while d == a or d ==b or d==c:
    d = 1+(70*random.random()) // 1

e=b
while e == a or e ==b or e==c or e==d:
    e = 1+(70*random.random()) // 1

print('a:{}, b: {}, c:{}, d:{}, e:{}'. format(a,b,c,d,e))

temes = {1: 'Números naturales. Sistemas de numeración.',
2: 'Fundamentos y aplicaciones de la teoría de grafos. Diagramas de árbol.',
3: 'Técnicas de recuento. Combinatoria.',
4: 'Números enteros. Divisibilidad. Números primos. Congruencia',
5: 'Números racionales.',
6: 'Números reales. Topología de la recta real.',
7: 'Aproximación de números. Errores. Notación científica.',
8: 'Sucesiones. Términos general y forma recurrente. Progresiones aritméticas y geométricas. Aplicaciones.',
9: 'Números complejos. Aplicaciones geométricas.',
10: 'Sucesivas ampliaciones del concepto de número. Evolución histórica y problemas que resuelve cada una.',
11: 'Conceptos básicos de la teoría de conjuntos. Estructuras algebraicas.',
12: 'Espacios vectoriales. Variedades lineales. Aplicaciones entre espacios vectoriales. Teorema de isomorfía.',
13: 'Polinomios. Operaciones. Fórmula de Newton. Divisibilidad de polinomios. Fracciones algebraicas.',
14: 'Ecuaciones. Resolución de ecuaciones. Aproximación numérica de raíces.',
15: 'Ecuaciones diofánticas.',
16: 'Discusión y resolución de sistemas de ecuaciones lineales. Teorema de Rouche. Regla de Cramer. Método de Gauss-Jordan.',
17: 'Programación lineal. Aplicaciones.',
18: 'Matrices. Algebra de matrices. Aplicaciones al campo de las Ciencias Sociales y de la Naturaleza.',
19: 'Determinantes. Propiedades. Aplicación al cálculo del rango de una matriz.',
20: 'El lenguaje algebraico. Símbolos y números. Importancia de su desarrollo y problemas que resuelve. Evolución histórica del álgebra. ',
21: 'Funciones reales de variable real. Funciones elementales; situaciones reales en las que aparecen. Composición de funciones.',
22: 'Funciones exponenciales y logarítmicas. Situaciones reales en las que aparecen.',
23: 'Funciones circulares e hiperbólicas y sus recíprocas. Situaciones reales en las que aparecen.',
24: 'Funciones dadas en forma de tabla. Interpolación polinómica. Interpolación y extrapolación de datos.',
25: 'Límites de funciones. Continuidad y discontinuidades. T. de Bolzano. Ramas infinitas.',
26: 'Derivada de una función en un punto. Función derivada. Derivadas sucesivas. Aplicaciones.',
27: 'Desarrollo de una función en serie de potencias. T. de Taylor. Aplicaciones al estudio local de funciones.',
28: 'Estudio global de funciones. Aplicaciones a la representación gráfica de funciones.',
29: 'El problema del cálculo del área. Integral definida.',
30: 'Primitiva de una función. Cálculo de algunas primitivas. Aplicaciones de la integral al cálculo de magnitudes geométricas.',
31: 'Integración numérica. Métodos y aplicaciones.',
32: 'Aplicación del estudio de f. a la interpretación y resolución de problemas de la Economía, las C. Sociales y la Naturaleza.',
33: 'Evolución histórica del cálculo diferencial.',
34: 'Análisis y formalización de los conceptos geométricos intuitivos: incidencia, paralelismo, perpendicularidad, etc.',
35: 'Las magnitudes y su medida. Fundamentación de los conceptos relacionados con ellas.',
36: 'Proporciones notables. La razón áurea. Aplicaciones.',
37: 'La relación de semejanza en el plano. Consecuencias. Teorema de Thales. Razones trigonométricas.',
38: 'Trigonometría plana. Resolución de triángulos. Aplicaciones.',
39: 'Geometría del triángulo. ',
40: 'Geometría de la circunferencia. Ángulos en la circunferencia. Potencia de un punto a una circunferencia.',
41: 'Movimientos en el plano. Composición de movimientos. Aplicaciones al estudio de las teselaciones del plano. Frisos y mosaicos.',
42: 'Homotecia y semejanza en el plano.',
43: 'Proyecciones en el plano. Mapas. Planisferios terrestres: principales sistemas de representación.',
44: 'Semejanza y movimientos en el espacio.',
45: 'Poliedros. Teorema de Euler. Sólidos platónicos y arquimedianos.',
46: 'Distintas coordenadas para describir el plano o el espacio. Ecuaciones de curvas y superficies.',
47: 'Generación de curvas como envolventes.',
48: 'Espirales y hélices. Presencia en la Naturaleza, en el Arte y en la Técnica.',
49: 'Superficies de revolución. Cuádricas. Superficies regladas. Presencia en la Naturaleza, en el Arte y la Técnica.',
50: 'Introducción a las geometrías no euclídeas. Geometría esférica.',
51: 'Sistemas de referencia en el plano y en el espacio. Ecuaciones de la recta y del plano. Relaciones afines.',
52: 'Producto escalar de vectores. Producto vectorial y producto mixto. Aplicaciones a la resolución de problemas físicos y geométricos.',
53: 'Relaciones métricas: perpendicularidad, distancias, ángulos, áreas, volúmenes, etc.',
54: 'Las cónicas como secciones planas de una superficie cónica. Estudio analítico. Presencia en la Naturaleza, Arte y Técnica.',
55: 'La geometría fractal. Nociones básicas.',
56: 'Evolución histórica de la geometría.',
57: 'Usos de la estadística: estad. Descriptiva y estadística inferencial. Métodos básicos y aplicaciones de cada una de ellas.',
58: 'Población y muestra. Condiciones de representatividad de una muestra. Tipos de muestreo. Tamaño de una muestra. ',
59: 'Técnicas de obtención y representación de datos. Tablas y gráficas estadísticas. Tendenciosidad y errores más comunes.',
60: 'Parámetros estadísticos. Cálculo, significado y propiedades.',
61: 'Desigualdad de Tchebyschev. Coeficiente de variación. Variable normalizada. Aplicación al análisis, interpretación y comparación de datos estadísticos.',
62: 'Series estadísticas bidimensionales. Regresión y correlación. Significado y aplicaciones.',
63: 'Frecuencia y probabilidad. Leyes del azar. Espacios probabilísticos.',
64: 'Probabilidad compuesta. Probabilidad condicionada. Probabilidad total. Teorema de Bayes.',
65: 'Distribuciones de probabilidad de variable discreta. Características y tratamiento. Las distribuciones binomial y de Poisson. Aplicaciones.',
66: 'Distribución de probabilidad de variable continua. Características y tratamiento. La distribución normal. Aplicaciones.',
67: 'Inferencia estadística. Test de hipótesis.',
68: 'Aplicaciones de la estadística y el cálculo de probabilidades al estudio y toma de decisiones en problemas de Ciencias Sociales y Naturaleza. Evolución histórica.',
69: 'La resolución de problemas en matemáticas. Estrategias. Importancia histórica.',
70: 'Lógica proposicional. Ejemplos y aplicaciones al razonamiento matemático.',
71: 'La controversia sobre los fundamentos de la matemática. Las limitaciones internas de los sistemas formales. '}

print('**********************************************')
print('Els temes que han sortit són els següents')
print('a:       {}: {}'.format(a,temes[a]))
print('b:       {}: {}'.format(b,temes[b]))
print('c:       {}: {}'.format(c,temes[c]))
print('d:       {}: {}'.format(d,temes[d]))
print('e:       {}: {}'.format(e,temes[e]))
print('**********************************************')
print()
Melse = {2,3,4,5,7,9,15,16,18,22,23,26,29,30,31,36,37,38,39,40,45,49,50,51,54,57,62,65}
aprovo =5
if a not in Melse:
    print('El tema A:         No el sé')
    aprovo-=1
else: print('El tema A:         El sé')
if b not in Melse:
    print('El tema B:         No el sé')
    aprovo-=1
else: print('El tema B:         El sé')
if c not in Melse:
    print('El tema C:         No el sé')
    aprovo-=1
else: print('El tema C:         El sé')
if d not in Melse:
    print('El tema D:         No el sé')
    aprovo-=1
else: print('El tema D:         El sé')
if e not in Melse:
    print('El tema E:         No el sé')
    aprovo-=1
else: print('El tema E:         El sé')
print()
print('**********************************************')
if aprovo == 0:
    print('No aprovo tot i sabent {} temes'.format(len(Melse)))
else:
    print('Aprovo sabent un total de {} temes'.format(len(Melse)))
