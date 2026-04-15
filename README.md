# Urban Planning Cost Prediction - ML Project

A comprehensive machine learning project for predicting urban planning project costs using regression models and an interactive Streamlit web application.

## 📋 Project Overview

This project implements machine learning models to predict the total cost of urban planning projects based on various factors such as:
- Project area and location
- Population density
- Infrastructure type
- Land costs
- Construction costs
- Environmental factors
- Zoning complexity
- And more...

## 🚀 Features

- **Comprehensive Jupyter Notebook**: Complete data analysis, preprocessing, and model training
- **Multiple ML Models**: Linear Regression, Random Forest, and Gradient Boosting
- **Interactive Streamlit App**: User-friendly web interface for cost predictions
- **Dataset**: 2,000 synthetic urban planning projects with 11 features
- **Model Persistence**: Saved models for easy deployment
- **Visualizations**: Data exploration and model performance charts

## 📁 Project Structure

```
urban_planning_ml_project/
│
├── urban_planning_dataset.csv          # Dataset (2000 samples)
├── Urban_Planning_Cost_Prediction.ipynb  # Main Jupyter notebook
├── streamlit_app.py                    # Streamlit web application
├── generate_dataset.py                 # Dataset generation script
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── Project_Report.md                   # Detailed project report
└── models/                             # Saved models (created after running notebook)
    ├── urban_planning_model.pkl
    ├── scaler.pkl
    └── label_encoder.pkl
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone or download this project**

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Usage

### 1. Generate Dataset (Optional)

If you need to regenerate the dataset:
```bash
python generate_dataset.py
```

### 2. Run Jupyter Notebook

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open and run the notebook**
   - Open `Urban_Planning_Cost_Prediction.ipynb`
   - Run all cells sequentially
   - This will:
     - Load and explore the data
     - Train multiple ML models
     - Evaluate and compare models
     - Save the best model and preprocessing objects

### 3. Run Streamlit Application

1. **Start Streamlit app**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Use the web interface**
   - Open the URL shown in terminal (usually http://localhost:8501)
   - Input project parameters using the sidebar
   - Click "Predict Cost" to get predictions
   - View results and analysis

## 📈 Dataset Description

The dataset contains 2,000 urban planning projects with the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| area_sqkm | Project area in square kilometers | 0.5 - 50 |
| population_density | Population per sq km | 100 - 5000 |
| infrastructure_type | Type of infrastructure | Residential, Commercial, Mixed, Industrial, Public |
| land_cost_per_sqkm | Land cost per sq km | 50,000 - 500,000 |
| construction_cost_index | Construction cost multiplier | 0.8 - 1.5 |
| distance_to_city_center | Distance from city center (km) | 1 - 30 |
| existing_infrastructure_score | Infrastructure quality score | 0.2 - 1.0 |
| environmental_factors | Environmental impact score | 0.5 - 1.0 |
| zoning_complexity | Zoning regulation complexity | 0.3 - 1.0 |
| project_duration_years | Project duration in years | 1 - 10 |
| total_cost_millions | **Target variable** - Total cost | Variable |

## 🤖 Models Implemented

1. **Linear Regression**: Baseline linear model
2. **Random Forest Regressor**: Ensemble of decision trees
3. **Gradient Boosting Regressor**: Sequential boosting ensemble (Best performing)

## 📊 Model Performance

The models are evaluated using:
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **R² Score** (Coefficient of Determination)

## 🎯 Key Features of the Streamlit App

- **Interactive Input**: Sliders and dropdowns for easy parameter input
- **Real-time Predictions**: Instant cost estimates
- **Cost Breakdown**: Visual analysis of cost factors
- **Dataset Preview**: Explore the training data
- **Statistics**: View dataset statistics and metrics

## 📝 Project Report

See `Project_Report.md` for:
- Detailed methodology
- Model evaluation results
- Feature importance analysis
- Limitations and future work
- Business impact and applications

## 🔧 Troubleshooting

### Issue: Model files not found
**Solution**: Run the Jupyter notebook first to train and save the models

### Issue: Streamlit app shows errors
**Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

### Issue: Dataset not found
**Solution**: Run `python generate_dataset.py` to create the dataset

## 📚 Dependencies

- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Plotting and visualization
- seaborn: Statistical data visualization
- scikit-learn: Machine learning algorithms
- streamlit: Web application framework
- joblib: Model persistence
- jupyter: Notebook environment

## 🎓 Learning Outcomes

This project demonstrates:
- Data preprocessing and feature engineering
- Multiple regression model implementation
- Model evaluation and comparison
- Model deployment with Streamlit
- End-to-end ML pipeline

## 📄 License

This project is for educational purposes.

## 👥 Contributing

Feel free to fork, modify, and improve this project!

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Happy Predicting! 🏙️📊**

