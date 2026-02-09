from PIL import Image

def make_square_from_height(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size

    # Nouvelle image carrée (largeur = hauteur)
    new_size = h*5

    # Image transparente
    square_img = Image.new("RGBA", (new_size, new_size), (0, 0, 0, 0))

    # Centrage horizontal
    x_offset = 0
    y_offset = 0
    for i in range(5):
        for j in range(5):
            img = Image.open(f"sol{j+1}_{i+1}.png").convert("RGBA")
            print(f"sol{j+1}_{i+1}.png")
            square_img.paste(img, (x_offset+h*i, y_offset+h*j), img)
    
    square_img.save(output_path)

# Exemple
make_square_from_height("sol1_1.png", "test.png")
