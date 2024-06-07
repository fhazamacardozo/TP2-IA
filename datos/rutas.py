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


def obtener_segmentos():
    segmentos = [
        # Buenos Aires
        ('Buenos Aires', 'Santa Fe', 300, 480, 500),
        ('Buenos Aires', 'Córdoba', 420, 700, 600),
        ('Buenos Aires', 'La Pampa', 350, 600, 400),
        ('Buenos Aires', 'Entre Ríos', 240, 400, 300),
        
        # Santa Fe
        ('Santa Fe', 'Buenos Aires', 300, 480, 500),
        ('Santa Fe', 'Entre Ríos', 120, 200, 150),
        ('Santa Fe', 'Córdoba', 180, 320, 200),
        ('Santa Fe', 'Santiago del Estero', 240, 400, 300),
        ('Santa Fe', 'Chaco', 220, 360, 250),
        ('Santa Fe', 'Corrientes', 300, 500, 400),

        # Córdoba
        ('Córdoba', 'Buenos Aires', 420, 700, 600),
        ('Córdoba', 'Santa Fe', 180, 320, 200),
        ('Córdoba', 'La Rioja', 240, 400, 300),
        ('Córdoba', 'San Luis', 180, 300, 200),
        ('Córdoba', 'Santiago del Estero', 220, 380, 250),
        ('Córdoba', 'Catamarca', 300, 500, 350),
        
        # La Pampa
        ('La Pampa', 'Buenos Aires', 350, 600, 400),
        ('La Pampa', 'Córdoba', 420, 700, 600),
        ('La Pampa', 'Mendoza', 300, 500, 400),
        ('La Pampa', 'Río Negro', 360, 600, 450),
        ('La Pampa', 'San Luis', 240, 400, 300),
        
        # Entre Ríos
        ('Entre Ríos', 'Buenos Aires', 240, 400, 300),
        ('Entre Ríos', 'Santa Fe', 120, 200, 150),
        ('Entre Ríos', 'Corrientes', 180, 300, 200),
        
        # Corrientes
        ('Corrientes', 'Entre Ríos', 180, 300, 200),
        ('Corrientes', 'Santa Fe', 300, 500, 400),
        ('Corrientes', 'Chaco', 120, 200, 150),
        ('Corrientes', 'Misiones', 240, 400, 300),
        
        # Misiones
        ('Misiones', 'Corrientes', 240, 400, 300),
        
        # Chaco
        ('Chaco', 'Santa Fe', 220, 360, 250),
        ('Chaco', 'Corrientes', 120, 200, 150),
        ('Chaco', 'Formosa', 180, 300, 200),
        ('Chaco', 'Santiago del Estero', 300, 500, 350),
        ('Chaco', 'Salta', 420, 700, 600),
        
        # Formosa
        ('Formosa', 'Chaco', 180, 300, 200),
        ('Formosa', 'Salta', 360, 600, 500),
        
        # Santiago del Estero
        ('Santiago del Estero', 'Santa Fe', 240, 400, 300),
        ('Santiago del Estero', 'Córdoba', 220, 380, 250),
        ('Santiago del Estero', 'Chaco', 300, 500, 350),
        ('Santiago del Estero', 'Tucumán', 200, 320, 250),
        ('Santiago del Estero', 'Catamarca', 240, 400, 300),
        ('Santiago del Estero', 'Salta', 420, 700, 600),
        
        # Tucumán
        ('Tucumán', 'Santiago del Estero', 200, 320, 250),
        ('Tucumán', 'Salta', 220, 360, 250),
        ('Tucumán', 'Catamarca', 120, 200, 150),
        
        # Catamarca
        ('Catamarca', 'Córdoba', 300, 500, 350),
        ('Catamarca', 'Santiago del Estero', 240, 400, 300),
        ('Catamarca', 'Tucumán', 120, 200, 150),
        ('Catamarca', 'La Rioja', 180, 300, 200),
        ('Catamarca', 'Salta', 360, 600, 500),
        
        # La Rioja
        ('La Rioja', 'Córdoba', 240, 400, 300),
        ('La Rioja', 'Catamarca', 180, 300, 200),
        ('La Rioja', 'San Juan', 180, 300, 200),
        ('La Rioja', 'San Luis', 300, 500, 400),
        
        # San Juan
        ('San Juan', 'La Rioja', 180, 300, 200),
        ('San Juan', 'Mendoza', 180, 300, 200),
        ('San Juan', 'San Luis', 360, 600, 500),
        
        # Mendoza
        ('Mendoza', 'San Juan', 180, 300, 200),
        ('Mendoza', 'San Luis', 180, 300, 200),
        ('Mendoza', 'La Pampa', 300, 500, 400),
        ('Mendoza', 'Neuquén', 420, 700, 600),
        
        # San Luis
        ('San Luis', 'La Pampa', 240, 400, 300),
        ('San Luis', 'Córdoba', 180, 300, 200),
        ('San Luis', 'La Rioja', 300, 500, 400),
        ('San Luis', 'San Juan', 360, 600, 500),
        ('San Luis', 'Mendoza', 180, 300, 200),
        
        # Neuquén
        ('Neuquén', 'Mendoza', 420, 700, 600),
        ('Neuquén', 'Río Negro', 240, 400, 300),
        ('Neuquén', 'La Pampa', 360, 600, 450),
        ('Neuquén', 'Chubut', 360, 600, 500),
        
        # Río Negro
        ('Río Negro', 'Neuquén', 240, 400, 300),
        ('Río Negro', 'Chubut', 300, 500, 400),
        ('Río Negro', 'La Pampa', 360, 600, 450),
        
        # Chubut
        ('Chubut', 'Río Negro', 300, 500, 400),
        ('Chubut', 'Neuquén', 360, 600, 500),
        ('Chubut', 'Santa Cruz', 480, 800, 700),
        
        # Santa Cruz
        ('Santa Cruz', 'Chubut', 480, 800, 700),
        ('Santa Cruz', 'Tierra del Fuego', 720, 1200, 1000),
        
        # Tierra del Fuego
        ('Tierra del Fuego', 'Santa Cruz', 720, 1200, 1000),
        
        # Salta
        ('Salta', 'Jujuy', 120, 200, 150),
        ('Salta', 'Formosa', 360, 600, 500),
        ('Salta', 'Chaco', 420, 700, 600),
        ('Salta', 'Santiago del Estero', 420, 700, 600),
        ('Salta', 'Catamarca', 360, 600, 500),
        ('Salta', 'Tucumán', 220, 360, 250),
        
        # Jujuy
        ('Jujuy', 'Salta', 120, 200, 150),
    ]
    return segmentos

