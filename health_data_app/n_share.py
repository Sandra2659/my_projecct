import numpy as np
from PIL import Image
from random import randrange
def generate_shares(data, share = 2):
    data = Image.open(data, 'r')
    data = np.array(data, dtype='u1')

    # Generate image of same size
    img1 = np.zeros(data.shape).astype("u1")
    img2 = np.zeros(data.shape).astype("u1")

    # Set random factor
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            for k in range(data.shape[2]):
                n = int(np.random.randint(data[i, j, k] + 1))
                img1[i, j, k] = n
                img2[i, j, k] = data[i, j, k] - n

    # Saving shares
    img1 = Image.fromarray(img1)
    img2 = Image.fromarray(img2)
    irand = randrange(1, 99999999)
    filename=str(irand)+'1'+'.png'
    filename1=str(irand)+'2'+'.png'
    share1="media/crypto/"+filename
    share2="media/crypto/"+filename1

    img1.save(share1, "PNG")
    img2.save(share2, "PNG")
    share1="crypto/"+filename
    share2="crypto/"+filename1

    return share1,share2

def compress_shares(img1, img2):
    # Read images
    img1 = np.asarray(Image.open(img1)).astype('int16')
    img2 = np.asarray(Image.open(img2)).astype('int16')

    img = np.zeros(img1.shape)

    # Fit to range
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(img.shape[2]):
                img[i, j, k] = img1[i, j, k] + img2[i, j, k]

    # Save compressed image
    img = img.astype(np.dtype('u1'))

    img = Image.fromarray(img)
    img.save("media/crypto/compress.png", "PNG")
    return
