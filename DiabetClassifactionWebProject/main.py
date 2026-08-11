from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import torch
from model import DiabetClassifier

app = FastAPI()

# 1. Modeli Yükle
model = DiabetClassifier()
model.load_state_dict(torch.load("diabet_model.pth", map_location=torch.device('cpu')))
model.eval()  # Çıkarım (inference) moduna al


# 2. Gelen Veri Yapısını Tanımla (11 Özellik)
class PatientData(BaseModel):
    Gender: float
    AGE: float
    Urea: float
    Cr: float
    HbA1c: float
    Chol: float
    TG: float
    HDL: float
    LDL: float
    VLDL: float
    BMI: float


# 3. Tahmin Endpoint'i
@app.post("/predict")
def predict_diabetes(data: PatientData):
    # Veriyi PyTorch Tensörüne çevir
    input_tensor = torch.tensor([[
        data.Gender, data.AGE, data.Urea, data.Cr,
        data.HbA1c, data.Chol, data.TG, data.HDL,
        data.LDL, data.VLDL, data.BMI
    ]], dtype=torch.float32)

    # Modelden tahmini al
    with torch.inference_mode():
        logits = model(input_tensor)
        pred_class = torch.argmax(logits, dim=1).item()

    # Sınıf etiketleri (Önceki verilere göre 0, 1, 2)
    class_map = {
        0: "Non-Diabetic (Diyabet Değil)",
        1: "Diabetic (Diyabet)",
        2: "Predict-Diabetic (Diyabete Yatkın)"
    }

    return {
        "class_id": pred_class,
        "result_text": class_map.get(pred_class, "Bilinmeyen Durum")
    }


# 4. Frontend dosyalarını (HTML, CSS, JS) sunmak için static klasörünü bağla
app.mount("/", StaticFiles(directory="static", html=True), name="static")