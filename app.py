from flask import Flask, request, render_template, send_from_directory
from PIL import Image, ImageDraw, ImageFont
import os
import random

app = Flask(__name__)

MEME_FOLDER = 'static/memes'
if not os.path.exists(MEME_FOLDER):
    os.makedirs(MEME_FOLDER)

FONT_PATH = os.path.join(os.path.dirname(__file__), 'static', 'fonts', 'DejaVuSans-Bold.ttf')

@app.route('/')
def index():
    return render_template('index.html')


def get_font_size(image_width, top_text, bottom_text, max_font_size=30, mid_font_size=20, min_font_size=10):
    text_length = max(len(top_text), len(bottom_text))
    scale_factor = image_width / 300 # 300 = base width (the calculations below are based on image with width=300)

    if 1 <= text_length <= 13:
        font_size = max_font_size
    elif 14 <= text_length <= 23:
        font_size = mid_font_size
    else:
        font_size = min_font_size

    font_size = int(font_size * scale_factor)

    font_size = max(min_font_size, min(font_size, max_font_size))

    return font_size


@app.route('/generateMeme', methods=['POST'])
def generate_meme():
    top_text = request.form.get('top_text')
    bottom_text = request.form.get('bottom_text')
    image_file = request.files['image']

    img = Image.open(image_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, get_font_size(img.width, top_text, bottom_text))

    width, height = img.size

    top_text_bbox = draw.textbbox((0, 0), top_text, font=font)
    bottom_text_bbox = draw.textbbox((0, 0), bottom_text, font=font)

    top_text_width = top_text_bbox[2] - top_text_bbox[0]

    bottom_text_width = bottom_text_bbox[2] - bottom_text_bbox[0]
    bottom_text_height = bottom_text_bbox[3] - bottom_text_bbox[1]

    top_text_position = (width // 2 - top_text_width // 2, 10)
    bottom_text_position = (width // 2 - bottom_text_width // 2, height - bottom_text_height - 10)

    draw.text(top_text_position, top_text, font=font, fill="white")
    draw.text(bottom_text_position, bottom_text, font=font, fill="white")

    meme_filename = f"meme_{random.randint(1000, 9999)}.png"
    meme_path = os.path.join(MEME_FOLDER, meme_filename)
    img.save(meme_path)

    return send_from_directory(MEME_FOLDER, meme_filename)


if __name__ == '__main__':
    app.run()
