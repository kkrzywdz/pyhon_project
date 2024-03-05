import os
import shutil
import imagehash
from PIL import Image


def find_identical_images(directory):
    hash_dict = {}
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            try:
                image = Image.open(image_path)
                image_hash = imagehash.phash(image)
                if image_hash in hash_dict:
                    print(f"Found identical images: {hash_dict[image_hash]} and {image_path}")
                    image1 = Image.open(hash_dict[image_hash])
                    image1.show("Image 1")
                    image1.close()
                    destination = "C:\\temp\\" + filename
                    shutil.move(image_path, destination)
                    print(f"Image {image_path} has been moved to {destination}.")
                else:
                    hash_dict[image_hash] = image_path
            except Exception as e:
                print(f"Unable to open image {image_path}. Error: {e}")


main_directory = "C:\\Users\\Ashram\\Downloads\\"
for dirpath, dirnames, filenames in os.walk(main_directory):
    find_identical_images(dirpath)
