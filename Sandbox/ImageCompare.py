import os
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
                    image2 = Image.open(image_path)
                    image1.show("Image 1")
                    image2.show("Image 2")
                    confirmation = input("These images look identical. Do you want to delete one of them? (yes/no): ")
                    if confirmation.lower() == "yes":
                        delete_confirmation = input("Which image do you want to delete? (1/2): ")
                        if delete_confirmation == "1":
                            os.remove(hash_dict[image_hash])
                            print(f"Image {hash_dict[image_hash]} has been deleted.")
                        elif delete_confirmation == "2":
                            os.remove(image_path)
                            print(f"Image {image_path} has been deleted.")
                else:
                    hash_dict[image_hash] = image_path
            except Exception as e:
                print(f"Unable to open image {image_path}. Error: {e}")

find_identical_images("/path/to/your/directory")