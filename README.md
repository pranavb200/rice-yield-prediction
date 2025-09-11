# 🌾 Rice Yield Prediction using Machine Learning

This project predicts **rice yield before harvest** using Machine Learning.  
It uses features like **Crop Year, Area, Rainfall, Fertilizer, Pesticide, and Temperature** to forecast yield in tons/hectare.  

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
✅ Upload your own dataset to test the model  
✅ Easy to deploy on **Render/Heroku/Streamlit**  

---

## 📂 Project Structure
rice_yield_project/
│
├── model/
│   └── rice_yield_model.pkl         ← Trained machine learning model (saved using Pickle)
│
├── templates/
│   └── index.html                   ← Frontend HTML form (user input UI)
│
├── crop_yield_with_temp.csv         ← Cleaned dataset with added Temperature column
│
├── app.py                           ← Flask backend (loads model and handles prediction requests)
│
├── train_model.py                   ← Model training script (compares RF and GBR, saves best)
│
├── requirements.txt                 ← List of required Python libraries
│
├── README.md                        ← (Optional) Project overview and setup instructions