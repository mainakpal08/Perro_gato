
from keras.models import Sequential
from keras.models import model_from_json

def predict(model, X):
    return model.predict(X)

if __name__ == '__main__':
    import sys
    img_dir = sys.argv[1]
    from get_dataset import get_img
    img = get_img(img_dir)
    import numpy as np
    X = np.zeros((1, 64, 64, 3), dtype='float64')
    X[0] = img
    # Getting model:
    model_file = open('Data/Model/model.json', 'r')
    model = model_file.read()
    model_file.close()
    model = model_from_json(model)
    # Getting weights
    model.load_weights("Data/Model/weights.h5")
    print("\n\n<<--------------------------------------------------------------------->>\n\n")
    print    ("                           Let me think ...                             ")
    print("\n\n<<--------------------------------------------------------------------->>\n\n")
    print("According to me -- >\n")
    p_cat = float(predict(model, X)[0][0])
    p_dog = float(predict(model, X)[0][1])
    if p_cat > p_dog :
        print("It is a CAT ! ( Probability -- > "+str(p_cat*100)+"% )")
    if p_dog > p_cat :
        print("It is a DOG ! ( Probability -- > "+str(p_dog*100)+"% )")
    if p_dog == p_cat :
        print("It is a HARD TO PREDICT ! !")