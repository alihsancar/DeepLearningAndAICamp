from model_creation import Desert101Classifier
import torch

MODEL_SAVE_PATH = 'models/desert_classifier.pth'

loaded_model = Desert101Classifier(
    input_shape=3,
    hidden_units=32,
    output_shape=4
)

loaded_model.load_state_dict(torch.load(MODEL_SAVE_PATH))
