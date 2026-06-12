try:
    import pytesseract
except ModuleNotFoundError:
    pytesseract = None

try:
    from PIL import Image
except ModuleNotFoundError:
    Image = None


def extract_text(image_path):

    if pytesseract is None or Image is None:
        return ""

    image = Image.open(image_path)

    text = pytesseract.image_to_string(
        image
    )

    return text
