#Segmento = [(Origen, Destino, Tiempo de Recorrido Promedio (minutos), 
#            Distancia (kms), Costo total de peajes en el recorrido (pesos)]
def obtener_segmentos_OLD():
    segmentos = [
        ('A', 'B', 120, 160, 1800),
        ('B', 'C', 180, 300, 0),
        ('C', 'D', 120, 160, 700),
        ('D', 'E', 100, 150, 500),
        ('E', 'F', 200, 250, 100),
        ('F', 'G', 150, 200, 300),
        ('G', 'H', 170, 220, 250),
        ('H', 'I', 140, 180, 400),
        ('I', 'J', 160, 200, 150),
        ('J', 'K', 180, 240, 200),
        ('K', 'L', 200, 260, 100),
        ('L', 'M', 120, 150, 350),
        ('M', 'N', 130, 170, 250),
        ('N', 'O', 150, 200, 200),
        ('O', 'P', 160, 210, 180),
        ('P', 'Q', 140, 180, 300),
        ('Q', 'R', 200, 250, 200),
        ('R', 'S', 180, 220, 400),
        ('S', 'T', 150, 190, 150),
        ('T', 'U', 170, 210, 250),
        ('U', 'V', 160, 200, 300),
        ('V', 'W', 180, 230, 200),
        ('W', 'X', 200, 260, 350),
        ('X', 'Y', 150, 180, 400),
        ('Y', 'Z', 170, 200, 200),
        ('Z', 'A', 200, 250, 300),
        ('B', 'G', 160, 200, 150),
        ('C', 'H', 180, 230, 250),
        ('D', 'I', 190, 240, 200),
        ('E', 'J', 170, 210, 300),
        ('F', 'K', 180, 230, 180),
        ('G', 'L', 160, 200, 250),
        ('H', 'M', 200, 250, 150),
        ('I', 'N', 150, 180, 200),
        ('J', 'O', 160, 200, 250),
        ('K', 'P', 170, 210, 180),
        ('L', 'Q', 150, 190, 300),
        ('M', 'R', 180, 230, 200),
        ('N', 'S', 190, 240, 150),
        ('O', 'T', 160, 200, 250),
        ('P', 'U', 170, 220, 180),
        ('Q', 'V', 180, 230, 200),
        ('R', 'W', 190, 240, 300),
        ('S', 'X', 160, 200, 180),
        ('T', 'Y', 170, 220, 250),
        ('U', 'Z', 190, 240, 200),
        ('V', 'A', 180, 230, 300),
        ('W', 'B', 170, 210, 180),
        ('X', 'C', 190, 240, 250),
        ('Y', 'D', 160, 200, 200),
        ('Z', 'E', 170, 220, 300),
        ('A', 'F', 180, 230, 180)
    ]
    return segmentos

#Segmento = [(Origen, Destino, Tiempo de Recorrido Promedio (minutos), 
#            Distancia (kms), Costo total de peajes en el recorrido (pesos)]
def obtener_segmentos():
    segmentos = [
        # Buenos Aires
        ('Buenos Aires', 'Santa Fe', 437, 642, 4229),
        ('Buenos Aires', 'Córdoba', 420, 700, 5489),
        ('Buenos Aires', 'La Pampa', 600, 837, 4306),
        ('Buenos Aires', 'Entre Ríos', 240, 321, 1720),
        
        # Santa Fe
        ('Santa Fe', 'Buenos Aires', 300, 480, 3560),
        ('Santa Fe', 'Entre Ríos', 300, 222, 1100),
        ('Santa Fe', 'Córdoba', 270, 369, 2730),
        ('Santa Fe', 'Santiago del Estero', 370, 611, 1800),
        ('Santa Fe', 'Chaco', 460, 693, 1900),
        ('Santa Fe', 'Corrientes', 450, 565, 900),

        # Córdoba
        ('Córdoba', 'Buenos Aires', 420, 700, 600),
        ('Córdoba', 'Santa Fe', 180, 320, 200),
        ('Córdoba', 'La Rioja', 240, 400, 300),
        ('Córdoba', 'San Luis', 180, 300, 200),
        ('Córdoba', 'Santiago del Estero', 220, 380, 250),
        ('Córdoba', 'Catamarca', 300, 500, 350),
        
        # La Pampa
        ('La Pampa', 'Buenos Aires', 612, 832, 3906),
        ('La Pampa', 'Córdoba', 661, 835, 2160),
        ('La Pampa', 'Mendoza', 720, 900, 1200),
        ('La Pampa', 'Río Negro', 360, 600, 950),
        ('La Pampa', 'San Luis', 480, 630, 1000),
        ('La Pampa', 'Neuquen', 300, 381, 900),
        
        # Entre Ríos
        ('Entre Ríos', 'Buenos Aires', 335, 323, 1050),
        ('Entre Ríos', 'Santa Fe', 336, 407, 1100),
        ('Entre Ríos', 'Corrientes', 494, 650, 900),
        
        # Corrientes
        ('Corrientes', 'Entre Ríos', 494, 650, 900),
        ('Corrientes', 'Santa Fe', 440, 417, 900),
        ('Corrientes', 'Chaco', 186, 243, 1800),
        ('Corrientes', 'Misiones', 518, 503, 1800),
        
        # Misiones
        ('Misiones', 'Corrientes', 518, 503, 1800),
        
        # Chaco
        ('Chaco', 'Santa Fe', 3880, 588, 1300),
        ('Chaco', 'Corrientes', 191, 243, 1800),
        ('Chaco', 'Formosa', 298, 371, 1800),
        ('Chaco', 'Santiago del Estero', 330, 438, 1500),
        ('Chaco', 'Salta', 452, 595, 900),
        
        # Formosa
        ('Formosa', 'Chaco', 354, 371, 2100),
        ('Formosa', 'Salta', 720, 986, 3000),
        
        # Santiago del Estero
        ('Santiago del Estero', 'Santa Fe', 384, 516, 1800),
        ('Santiago del Estero', 'Córdoba', 430, 436, 720),
        ('Santiago del Estero', 'Chaco', 434, 439, 2500),
        ('Santiago del Estero', 'Tucumán', 140, 164, 900),
        ('Santiago del Estero', 'Catamarca', 320, 290, 1300),
        ('Santiago del Estero', 'Salta', 431, 435, 900),
        
        # Tucumán
        ('Tucumán', 'Santiago del Estero', 144, 161, 900),
        ('Tucumán', 'Salta', 235, 304, 1800),
        ('Tucumán', 'Catamarca', 189, 231, 1500),
        
        # Catamarca
        ('Catamarca', 'Córdoba', 418, 443, 300),
        ('Catamarca', 'Santiago del Estero', 240, 400, 300),
        ('Catamarca', 'Tucumán', 185, 232, 1500),
        ('Catamarca', 'La Rioja', 120, 157, 700),
        ('Catamarca', 'Salta', 601, 534, 1800),
        
        # La Rioja
        ('La Rioja', 'Córdoba', 443, 467, 720),
        ('La Rioja', 'Catamarca', 122, 157, 500),
        ('La Rioja', 'San Juan', 423, 443, 1200),
        ('La Rioja', 'San Luis', 365, 524, 1400),
        
        # San Juan
        ('San Juan', 'La Rioja', 423, 443, 1200),
        ('San Juan', 'Mendoza', 142, 170, 600),
        ('San Juan', 'San Luis', 242, 325, 1500),
        
        # Mendoza
        ('Mendoza', 'San Juan', 143, 170, 600),
        ('Mendoza', 'San Luis', 186, 258, 975),
        ('Mendoza', 'La Pampa', 652, 829, 4200),
        ('Mendoza', 'Neuquén', 562, 788, 3600),
        
        # San Luis
        ('San Luis', 'La Pampa', 501, 638, 3000),
        ('San Luis', 'Córdoba', 305, 429, 2460),
        ('San Luis', 'La Rioja', 360, 521, 1400),
        ('San Luis', 'San Juan', 242, 325, 1500),
        ('San Luis', 'Mendoza', 186, 258, 975),
        
        # Neuquén
        ('Neuquén', 'Mendoza', 562, 788, 3600),
        ('Neuquén', 'Río Negro', 405, 556, 3000),
        ('Neuquén', 'La Pampa', 407, 382, 1450),
        ('Neuquén', 'Chubut', 708, 951, 3200),
        
        # Río Negro
        ('Río Negro', 'Neuquén', 405, 556, 3000),
        ('Río Negro', 'Chubut', 540, 873, 2600),
        ('Río Negro', 'La Pampa', 442, 519, 2450),
        
        # Chubut
        ('Chubut', 'Río Negro', 540, 873, 2600),
        ('Chubut', 'Neuquén', 708, 951, 3200),
        ('Chubut', 'Santa Cruz', 831, 960, 4000),
        
        # Santa Cruz
        ('Santa Cruz', 'Chubut', 831, 960, 4000),
        ('Santa Cruz', 'Tierra del Fuego', 818, 979, 4000),
        
        # Tierra del Fuego
        ('Tierra del Fuego', 'Santa Cruz', 818, 979, 4000),
        
        # Salta
        ('Salta', 'Jujuy', 353, 250, 1500),
        ('Salta', 'Formosa', 725, 983, 4000),
        ('Salta', 'Chaco', 453, 598, 900),
        ('Salta', 'Santiago del Estero', 431, 438, 900),
        ('Salta', 'Catamarca', 519, 537, 1800),
        ('Salta', 'Tucumán', 220, 360, 250),
        
        # Jujuy
        ('Jujuy', 'Salta', 353, 250, 1500),
    ]
    return segmentos

