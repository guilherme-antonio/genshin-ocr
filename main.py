from PIL import Image
import pytesseract
from stats import Stats

image_to_string = pytesseract.image_to_string('genshin.png')

stats = Stats(image_to_string)

stats.show_stats()