from PIL import Image

def make_square_from_height(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size

    # Nouvelle image carrée (largeur = hauteur)
    new_size = h

    # Image transparente
    square_img = Image.new("RGBA", (new_size, new_size), (0, 0, 0, 0))

    # Centrage horizontal
    x_offset = (new_size - w) // 2
    y_offset = 0

    square_img.paste(img, (x_offset, y_offset), img)
    square_img.save(output_path)

# Exemple

print("Nom de l'objet")
nom = input(">>")
print("Nom de l'image:")
image = input(">>")
make_square_from_height(image, image)
print("Prix du batiment:")
prix = input(">>")
print("Type de sol")
sol = input(">>")
print("Production:")
prod = input(">>")

print(nom, """: {
          prix:""", prix, f""",
          sol: "{sol}",
          image: "./{image}",
          production: {prod},
      """, "}")