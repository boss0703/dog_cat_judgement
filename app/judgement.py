from tensorflow.python.keras.applications.vgg16 import preprocess_input
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator

from dog_cat_judgement.settings import BASE_DIR
import numpy as np


model = load_model(str(BASE_DIR) + '/app/model_cat_vs_dog.h5')


def judgement(path):
    img_data = load_img(path, target_size=(224, 224))
    x_test = np.array([img_to_array(img_data)])
    x_test_preproc = preprocess_input(x_test.copy()) / 255.

    probs = np.array(model.predict_on_batch(x_test_preproc))

    ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        preprocessing_function=preprocess_input
    )

    return probs[0][0]
