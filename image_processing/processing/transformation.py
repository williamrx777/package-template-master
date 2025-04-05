from skimage.transform import resize

def resize_image(image, proportions):
    assert 0 <= proportion <= 1, "Specify a valid proportion between 0 and 1"
    height = round(image.shape[0] * proportions)
    width = round(image.shape[1] * proportions)
    image_resized = resize(image, (height, width), anti_aliasing=True)
    return image_resized