from PIL import Image
import os

def convert_to_jpeg(file_path):
    """
    画像ファイルをJPEG形式に変換する
    """
    try:
        # 画像ファイルを開く
        with Image.open(file_path) as im:
            # ファイル名と拡張子を分割する
            file_name, ext = os.path.splitext(file_path)
            # JPEG形式に変換して保存する
            im.convert('RGB').save(file_name + '.jpeg', 'JPEG')
            print(f"{file_path}をJPEG形式に変換しました")
    except Exception as e:
        print(f"{file_path}の変換に失敗しました：{e}")

# 変換したい画像ファイルのパスを指定する
file_path = "/Users/tatsumiyuu/Desktop/Atcorder/2023/3th/day_21/IMG_3974 2.png"

# 画像ファイルをJPEG形式に変換する
convert_to_jpeg(file_path)
