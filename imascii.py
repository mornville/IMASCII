from PIL import Image
ASCII_CHARS = ['@', '#', '$', '%', '?', "*", "+", ";", ":", ',', '.']

def resize_image(image, new_width):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width*ratio)
    resize_image = image.resize((new_width, new_height))

    return resize_image

def convet_to_gray_scale(image):
    gray_image = image.convert("L")
    return gray_image

def pix_toAscii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

def main():
    path = input("Enter image path: ")
    new_width = int(input("Enter required width: "))
    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return

    new_image_data = pix_toAscii(convet_to_gray_scale(resize_image(image, new_width)))


    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    print(ascii_image)
    with open("out.txt", "w") as f:
        f.write(ascii_image)

    
main()