from PIL import Image
import pytesseract
import pandas as pd

print(pytesseract.image_to_string(Image.open('./tumblr/1c95gof.jpg')))

df = pd.read_parquet()