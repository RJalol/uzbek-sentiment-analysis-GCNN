
````markdown
# 🇺🇿 Uzbek Sentiment Analysis with GCNN

Aspect-Based Sentiment Analysis (ABSA) for Uzbek reviews.  
Modelar: **CNN_Basic**, **LSTM**, **CNN_Gate_Aspect (GCNN)**.

---

## ⚙️ O‘rnatish

```bash
git clone https://github.com/RJalol/uzbek-sentiment-analysis-GCNN.git
cd uzbek-sentiment-analysis-GCNN
pip install -r requirements.txt
````

---

## 🚀 Modelni ishga tushirish

### GCNN (CNN_Gate_Aspect)

```bash
python -m run -lr 1e-2 -batch-size 32 -verbose 1 \
  -model CNN_Gate_Aspect -embed_file glove -r_l r -epochs 13
```

### CNN_Basic

```bash
python -m run -lr 1e-2 -batch-size 32 -verbose 1 \
  -model CNN_Basic -embed_file glove -r_l r -epochs 13
```

### LSTM

```bash
python -m run -lr 1e-2 -batch-size 32 -verbose 1 \
  -model LSTM -embed_file glove -r_l r -epochs 13
```

---

## 📦 `requirements.txt`

```txt
torch>=2.0.0
torchvision>=0.15.0
torchtext>=0.15.0
numpy>=1.23
pandas>=1.5
scikit-learn>=1.2
tqdm>=4.65
PyYAML>=6.0
transformers>=4.30
nltk>=3.8
spacy>=3.5
matplotlib>=3.7
seaborn>=0.12
```


## 👤 Muallif

**Jaloliddin Shamsiddin o‘g‘li Rajabov (RJalol)**
📧 [jaloliddin.rajabov@gmail.com](mailto:jaloliddin.rajabov@gmail.com)
💬 [@Jaloliddin_Shamsuddinovich](https://t.me/Jaloliddin_Shamsuddinovich)
🔗 [GitHub/RJalol](https://github.com/RJalol)
📜 Litsenziya

Ushbu loyiha ilmiy va ta’limiy maqsadlarda foydalanish uchun ochiq.
Tijoriy foydalanish uchun muallif bilan bog‘laning.

