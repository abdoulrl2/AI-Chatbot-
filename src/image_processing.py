# image_processing.py
import cv2
import argparse

def process_image(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    if image is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return
    
    # Processar a imagem (exemplo: converter para escala de cinza)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Mostrar a imagem original e a imagem em preto e branco
    cv2.imshow('Imagem Original', image)
    cv2.imshow('Imagem em Preto e Branco', gray_image)
    
    # Aguardar até que qualquer tecla seja pressionada
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processar uma imagem.")
    parser.add_argument('image_path', type=str, help='Caminho para a imagem a ser processada')
    args = parser.parse_args()
    
    process_image(args.image_path)
