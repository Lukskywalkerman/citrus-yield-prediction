# Machine Learning for Yield Prediction in the Brazilian Citrus Belt

This repository contains the dataset and predictive models (CatBoost) developed to forecast orange yield across the São Paulo-Minas Gerais citrus belt (1985–2024).

## 🚀 Highlights
- **Algorithm:** CatBoost Regressor (R²: 0.925).
- **Data Integration:** 40 years of Landsat/MODIS/SMAP imagery masked by MapBiomas Class 39 (Citrus).
- **Economic Insight:** Inclusion of global NPK (Urea, Phosphate, KCl) market prices as predictive variables.

## 📂 Repository Structure
- `/data`: Consolidates 21 variables including NDVI, NDWI, LST, and Soil Moisture.
- `/notebooks`: Colab-ready script for model training and SHAP analysis.
- `/supplementary`: Multi-temporal GIFs (Bebedouro & Casa Branca) showing orchard expansion.

## 🛠️ How to use
Click the badge below to run the analysis directly in Google Colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](SUA_URL_DO_COLAB_AQUI)

## 📄 License
This project is licensed under the MIT License.

## ✍️ Citation
If you use this data or code, please cite:
*Ames, G. (2025). Machine Learning for Yield Prediction in the Brazilian Citrus Belt.*
