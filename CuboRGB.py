import numpy as np
import matplotlib.pyplot as plt

def generate_slice(face, i):
    # Valida os inputs
    if face < 1 or face > 6 or i < 0 or i > 255:
        raise ValueError("Face deve ser de 1 a 6 e i deve ser de 0 a 255")
    
    # Inicializa a matriz de zeros
    slice_rgb = np.zeros((256, 256, 3), dtype=np.uint8)
    
    if face == 1:
        # Face 1: R constante, varia G e B
        slice_rgb[:, :, 0] = i
        slice_rgb[:, :, 1] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 2] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    elif face == 2:
        # Face 2: G constante, varia R e B
        slice_rgb[:, :, 1] = i
        slice_rgb[:, :, 0] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 2] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    elif face == 3:
        # Face 3: B constante, varia R e G
        slice_rgb[:, :, 2] = i
        slice_rgb[:, :, 0] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 1] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    elif face == 4:
        # Face 4: R constante, varia G e B (oposta à Face 1)
        slice_rgb[:, :, 0] = 255 - i
        slice_rgb[:, :, 1] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 2] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    elif face == 5:
        # Face 5: G constante, varia R e B (oposta à Face 2)
        slice_rgb[:, :, 1] = 255 - i
        slice_rgb[:, :, 0] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 2] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    elif face == 6:
        # Face 6: B constante, varia R e G (oposta à Face 3)
        slice_rgb[:, :, 2] = 255 - i
        slice_rgb[:, :, 0] = np.linspace(0, 255, 256, dtype=np.uint8)[:, np.newaxis]
        slice_rgb[:, :, 1] = np.linspace(0, 255, 256, dtype=np.uint8)
        
    return slice_rgb

def show_slice(slice_rgb):
    plt.imshow(slice_rgb)
    plt.axis('off')
    plt.show()

def main():
    # Solicita a entrada do usuário
    while True:
        try:
            face = int(input("Escolha a face (1 a 6): "))
            profundidade = int(input("Escolha a profundidade (0 a 255): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros válidos.")
    
    # Gera a fatia com base nos inputs do usuário
    slice_rgb = generate_slice(face, profundidade)
    
    # Mostra a fatia gerada
    show_slice(slice_rgb)

if __name__ == "__main__":
    main()
