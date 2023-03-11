from google_images_search import GoogleImagesSearch
import cv2
import numpy as np
from matplotlib import pyplot as plt

from creds.creds import __cx__, __apikey__


def main():
    local_path = "/home/khavernathy/git/artbot/data/"
    gis = GoogleImagesSearch(__apikey__, __cx__)

    np.random.seed(42)
    n_images_to_search = 10
    n_images_to_use = 3
    master_img = np.zeros((1000, 1000))
    source_imgs = []

    # define search params:
    _search_params = {
        'q': 'cool',
        'num': n_images_to_search,
        'safe': 'high',
    }

    ids_to_use = np.random.randint(low=0, high=n_images_to_search-1, size=n_images_to_use)

    gis.search(search_params=_search_params)
    results = gis.results()
    for image_id in ids_to_use:
        image = results[image_id]
        image.download(local_path)
                                    # image.resize(500, 500)
        img = cv2.imread(image.path)
        source_imgs.append(img)


        a=3
    a=3


if __name__ == '__main__':
    main()
    a=3
