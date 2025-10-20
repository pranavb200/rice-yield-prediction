# 🌾 Rice Yield Prediction using Machine Learning

This project predicts **rice yield before harvest** using Machine Learning.  
It uses features like **Area, Annual_Rainfall, Fertilizer, Pesticide, and Temperature** to forecast yield in tons/hectare.  

The app is built with:
- 🐍 Python (Flask API backend)
- 📊 scikit-learn (Random Forest & Gradient Boosting Regressors)
- 🌐 HTML + CSS frontend
- 📁 CSV dataset (with temperature feature)

---

## 🚀 Features
✅ Predict rice yield before planting/harvest  
✅ Compare ML models (Random Forest vs Gradient Boosting)  
✅ Simple web interface for predictions  
✅ Easy to deploy on **Render/Heroku**  

---

## 📂 Project Structure
```
rice_yield_project/
│
├── model/
│   └── rice_yield_model.pkl
├── templates/
│   └── index.html
├── crop_yield_with_temp.csv
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/rice-yield-prediction.git
cd rice-yield-prediction
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model
```bash
python train_model.py
```

### 4️⃣ Run the Flask app
```bash
python app.py
```

App will be live at 👉 
(https://rice-yield-predictor.onrender.com)

---

## 🌍 Deployment
You can deploy using:
- [Render](https://render.com/) (recommended for Flask)
- [Heroku](https://www.heroku.com/)

---

## 🎯 Future Scope
- Integration with **real-time weather APIs**
- Support for **multiple crops**
- Mobile app for farmer-friendly access

---

👨‍💻 Developed with ❤️ for Smart Agriculture
