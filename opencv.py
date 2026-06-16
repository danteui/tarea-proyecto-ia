import cv2

# 1. Cargar la imagen original (BGR)
imagen = cv2.imread('entrada.jpg')

if imagen is None:
    print("Error: No se encontró la imagen 'entrada.jpg'")
    exit()

# 2. Convertir a Escala de Grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 3. Convertir a HSV (Hue, Saturation, Value - Ideal para detectar colores)
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# 4. Mostrar los diferentes espacios de color
cv2.imshow('Original (BGR)', imagen)
cv2.imshow('Escala de Grises', gris)
cv2.imshow('Espacio HSV', hsv)

print("Presiona cualquier tecla con las ventanas activas para salir...")
cv2.waitKey(0)
cv2.destroyAllWindows()
