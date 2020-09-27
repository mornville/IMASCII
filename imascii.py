from PIL import Image
ASCII_CHARS = ['@', '#', '$', '%', '?', "*", "+", ";", ":", ',', '.']

class imascii():
    def __init__(self, path, format='txt', new_width=100):
        self.path = path
        self.format = format
        self.new_width = new_width

    def resize_image(self, image):
        width, height = image.size
        ratio = height/width
        new_height = int(self.new_width*ratio)
        resize_image = image.resize((self.new_width, new_height))

        return resize_image

    def convet_to_gray_scale(self, image):
        gray_image = image.convert("L")
        return gray_image

    def pix_toAscii(self, image):
        pixels = image.getdata()
        characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
        return characters

    def main(self):

        try:
            image = Image.open(self.path)
        except Exception as e:
            print(e)
            return

        new_image_data = self.pix_toAscii(self.convet_to_gray_scale(self.resize_image(image)))


        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i+self.new_width)] for i in range(0, pixel_count, self.new_width))
        if self.format=='txt':
            with open("out.txt", "w") as f:
                f.write(ascii_image)
        else:
            print(ascii_image)

        
a = imascii(path='pika.png',format='txt', new_width=100)
a.main()