from PIL import Image


def addLogoAboveImage(imagePath, logoPath):
    image = Image.open(imagePath)
    logo = Image.open(logoPath)

    parentImageCoordinates = (
        int((image.size[0]/2) - logo.size[0]/2),
        int((image.size[1]/2) - logo.size[1])
    )

    image.paste(logo, parentImageCoordinates)
    image.save("brand-new-img.jpg")


imagePath = 'monty-python.jpg'
logoPath = 'python-logo.png'

# python main.py
addLogoAboveImage(imagePath, logoPath)
