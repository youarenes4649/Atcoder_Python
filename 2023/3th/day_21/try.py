from PIL import Image
import os

def convert_to_jpeg(input_path):
    # 入力ファイルの拡張子を取得
    file_name, extension = os.path.splitext(input_path)

    # PNGファイルの場合は、Image.open()を使用する
    if extension.lower() == '.png':
        with Image.open(input_path) as img:
            # JPEGに変換して保存
            img = img.convert('RGB')
            img.save(file_name + '.jpeg', 'JPEG')
            print(f'{input_path}を{file_name + ".jpeg"}に変換しました。')
    # それ以外の場合は、Pillow.Imageのopen()を使用する
    else:
        with Image.open(input_path) as img:
            # JPEGに変換して保存
            img = img.convert('RGB')
            img.save(file_name + '.jpeg', 'JPEG')
            print(f'{input_path}を{file_name + ".jpeg"}に変換しました。')

# 変換したい画像ファイルのパスを指定する
file_path = "/Users/tatsumiyuu/Desktop/Atcorder/2023/3th/day_21/IMG_3761.PNG"

# 画像ファイルをJPEG形式に変換する
convert_to_jpeg(file_path)
