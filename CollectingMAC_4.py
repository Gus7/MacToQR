import qrcode
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



counter = 0
with open('input.txt') as f:
    for s in f:

        font = ImageFont.truetype("arial.ttf", 170)
        font2 = ImageFont.truetype("arial.ttf", 290)

        img = qrcode.make(s)

        '''textImage = qrcode.make(s)
        textImage = textImage.crop((0,0,290,25))
        textImage = textImage.resize((300,100))
        drawing = ImageDraw.Draw(textImage)
        drawing.text((25, 25), s, font=font)'''



        img = img.crop((39,39,img.size[0]-39,img.size[1]-39))
        img = img.resize((1200,1200))


        #textImage = textImage.resize((1200,400))




        testImage = Image.new("RGBA", (1500, 2000), (0, 0, 0, 0))
        draw = ImageDraw.Draw(testImage)

        draw.ellipse((0, 0, 600, 600), fill="white", outline="white")
        draw.ellipse((900, 0, 1500, 600), fill="white", outline="white")
        draw.ellipse((0, 1400, 600, 2000), fill="white", outline="white")
        draw.ellipse((900, 1400, 1500, 2000), fill="white", outline="white")

        draw.rectangle((0, 300, 750,1700), fill="white", outline="white")
        draw.rectangle((750, 300, 1500, 1700), fill="white", outline="white")
        draw.rectangle((300, 0, 1200, 600), fill="white", outline="white")
        draw.rectangle((300, 1400, 1200, 2000), fill="white", outline="white")

        testImage = testImage.rotate(90, expand=True)
        draw = ImageDraw.Draw(testImage)
        draw.text((190, 1250), s, font=font, fill="black")
        #draw.text((650, -20), s[3:7], font=font2, fill="black")

        testImage.paste(img,(425,50))



        counter += 1

        testImage.show()
        testImage.save('qr4.png', "PNG")