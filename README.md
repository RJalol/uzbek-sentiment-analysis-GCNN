# 🇺🇿 Uzbek Sentiment Analysis with GCNN

Bu loyiha **O‘zbek tili**da yozilgan matnlar uchun **Aspect-Based Sentiment Analysis (ABSA)** yechimini taqdim etadi.  
Model asosida **Gated Convolutional Neural Network (GCNN)** arxitekturasi qo‘llangan.

---

## 📌 Loyihaning asosiy maqsadi

- Restoran, xizmat va boshqa domenlarga oid izohlarni **aspektlar bo‘yicha** tahlil qilish  
- Har bir aniqlangan aspekt uchun **sentiment darajasini** (negative, neutral, positive, conflict) aniqlash  
- O‘zbek tili uchun maxsus **embedding** va **dataset**lardan foydalanish

---

## 📂 Papkalar tuzilishi

├── embedding/ # So‘z vektorlari (FastText / Word2Vec)

├── model_files/ # Saqlangan model fayllari (.pt, .pth)

├── output/ # Trening / test natijalari

├── uzabsa/ # Asosiy kod: model, train, evaluate, utils

│ ├── train.py

│ ├── evaluate.py

│ ├── predict.py

│ └── ...

├── absa_uzbek.csv # ABSA ma’lumotlar (CSV format)

├── absa_uzbek.json # ABSA ma’lumotlar (JSON format)

├── uz_getsemeval.ipynb # Notebook — eksperimentlar va vizualizatsiya

├── requirements.txt # Kerakli kutubxonalar ro‘yxati

└── README.md 

---

## ⚙️ O‘rnatish (Installation)

### 1. Virtual muhit yaratish


python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt


👉 Batafsil: requirements.txt

Agar GPU mavjud bo‘lsa, PyTorchni NVIDIA CUDA bilan mos holda o‘rnatish tavsiya qilinadi:
👉 https://pytorch.org/get-started/locally/

🚀 Modelni ishlatish
1. Trening
python uzabsa/train.py --config configs/config.yaml

2. Baholash (Evaluation)
python uzabsa/evaluate.py \
  --model_path model_files/best_model.pth \
  --test_data data/test.csv

3. Inference (yangi matnda sinash)
python uzabsa/predict.py \
  --model_path model_files/best_model.pth \
  --input "Restorandagi xizmat juda yaxshi edi"


👉 Natija:

{
  "aspect": "xizmat",
  "sentiment": "positive"
}

📊 Metodik yondashuv

Embedding — so‘z vektorlari (FastText yoki Word2Vec Uzbek)

GCNN — Gated Convolutional Neural Network yordamida aspektni kontekstdan ajratish

Sentiment klassifikatsiya — 4 sinf:

0 : Negative

1 : Neutral

2 : Positive

3 : Conflict

🧑‍💻 Muallif

Jaloliddin Shamsiddin o‘g‘li Rajabov (RJalol)
PhD candidate — Mirzo Ulug‘bek National University of Uzbekistan

📧 Email: jaloliddin.rajabov@gmail.com

💬 Telegram: @Jaloliddin_Shamsuddinovich

🔗 GitHub: RJalol

📜 Litsenziya

Ushbu loyiha ilmiy va ta’limiy maqsadlarda foydalanish uchun ochiq.
Tijoriy foydalanish uchun muallif bilan bog‘laning.
