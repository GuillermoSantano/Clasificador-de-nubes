from keras.models import load_model

def load_model_h5():
    
    model = load_model("mi_modelo.h5")
    
    return model