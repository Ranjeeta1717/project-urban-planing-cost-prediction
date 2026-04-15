import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Urban Planning Cost Prediction",
    page_icon="🏙️",
    layout="wide"
)

# Title and description
st.title("🏙️ Urban Planning Cost Prediction")
st.markdown("""
This application predicts the total cost of urban planning projects based on various factors.
Enter the project details below to get an estimated cost prediction.
""")

# Load model and preprocessing objects
@st.cache_resource
def load_model():
    """Load the trained model and preprocessing objects"""
    try:
        model = joblib.load('models/urban_planning_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        label_encoder = joblib.load('models/label_encoder.pkl')
        return model, scaler, label_encoder
    except FileNotFoundError:
        st.error("Model files not found. Please run the Jupyter notebook first to train and save the model.")
        return None, None, None

model, scaler, label_encoder = load_model()

if model is not None:
    # Sidebar for input
    st.sidebar.header("📋 Project Details")
    
    # Input fields
    area_sqkm = st.sidebar.slider("Area (sq km)", min_value=0.5, max_value=50.0, value=10.0, step=0.5)
    population_density = st.sidebar.slider("Population Density", min_value=100, max_value=5000, value=1000, step=50)
    infrastructure_type = st.sidebar.selectbox(
        "Infrastructure Type",
        ['Residential', 'Commercial', 'Mixed', 'Industrial', 'Public']
    )
    land_cost_per_sqkm = st.sidebar.slider(
        "Land Cost per sq km", 
        min_value=50000, 
        max_value=500000, 
        value=200000, 
        step=10000
    )
    construction_cost_index = st.sidebar.slider(
        "Construction Cost Index", 
        min_value=0.8, 
        max_value=1.5, 
        value=1.0, 
        step=0.1
    )
    distance_to_city_center = st.sidebar.slider(
        "Distance to City Center (km)", 
        min_value=1.0, 
        max_value=30.0, 
        value=10.0, 
        step=1.0
    )
    existing_infrastructure_score = st.sidebar.slider(
        "Existing Infrastructure Score (0.2-1.0)", 
        min_value=0.2, 
        max_value=1.0, 
        value=0.6, 
        step=0.1
    )
    environmental_factors = st.sidebar.slider(
        "Environmental Factors (0.5-1.0)", 
        min_value=0.5, 
        max_value=1.0, 
        value=0.75, 
        step=0.05
    )
    zoning_complexity = st.sidebar.slider(
        "Zoning Complexity (0.3-1.0)", 
        min_value=0.3, 
        max_value=1.0, 
        value=0.6, 
        step=0.1
    )
    project_duration_years = st.sidebar.slider(
        "Project Duration (years)", 
        min_value=1, 
        max_value=10, 
        value=5, 
        step=1
    )
    
    # Prediction button
    if st.sidebar.button("🔮 Predict Cost", type="primary"):
        # Encode infrastructure type
        infrastructure_encoded = label_encoder.transform([infrastructure_type])[0]
        
        # Prepare input data
        input_data = pd.DataFrame({
            'area_sqkm': [area_sqkm],
            'population_density': [population_density],
            'land_cost_per_sqkm': [land_cost_per_sqkm],
            'construction_cost_index': [construction_cost_index],
            'distance_to_city_center': [distance_to_city_center],
            'existing_infrastructure_score': [existing_infrastructure_score],
            'environmental_factors': [environmental_factors],
            'zoning_complexity': [zoning_complexity],
            'project_duration_years': [project_duration_years],
            'infrastructure_type_encoded': [infrastructure_encoded]
        })
        
        # Scale the input
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Store prediction in session state
        st.session_state['prediction'] = prediction
        st.session_state['input_data'] = input_data
    
    # Display results
    if 'prediction' in st.session_state:
        st.header("💰 Cost Prediction Result")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Predicted Cost",
                f"${st.session_state['prediction']:,.2f} Million",
                help="Total project cost in millions"
            )
        
        with col2:
            st.metric(
                "Predicted Cost (USD)",
                f"${st.session_state['prediction'] * 1_000_000:,.0f}",
                help="Total project cost in USD"
            )
        
        with col3:
            # Calculate cost per sq km
            cost_per_sqkm = st.session_state['prediction'] / area_sqkm
            st.metric(
                "Cost per sq km",
                f"${cost_per_sqkm:,.2f} Million",
                help="Cost per square kilometer"
            )
        
        # Display input summary
        st.subheader("📊 Input Summary")
        input_summary = st.session_state['input_data'].T
        input_summary.columns = ['Value']
        input_summary.index = [
            'Area (sq km)',
            'Population Density',
            'Land Cost per sq km',
            'Construction Cost Index',
            'Distance to City Center (km)',
            'Existing Infrastructure Score',
            'Environmental Factors',
            'Zoning Complexity',
            'Project Duration (years)',
            'Infrastructure Type (encoded)'
        ]
        st.dataframe(input_summary, use_container_width=True)
        
        # Cost breakdown visualization
        #st.subheader("📈 Cost Breakdown Analysis")
        
        #col1, col2 = st.columns(2)
        
        #with col1:
            # Feature contribution (simplified)
            #features_contribution = {
              #  'Land Cost': (area_sqkm * land_cost_per_sqkm) / 1_000_000,
               # 'Population Factor': (population_density * 100) / 1_000_000,
                #'Construction Factor': (construction_cost_index * 50000) / #1_000_000,
                #'Distance Factor': (distance_to_city_center * 2000) / #1_000_000,
            #}
            
            #st.bar_chart(features_contribution)
        
        #with col2:
            # Cost range estimate
            #cost_range = {
              #  'Minimum Estimate': st.session_state['prediction'] * 0.85,
               # 'Predicted Cost': st.session_state['prediction'],
               # 'Maximum Estimate': st.session_state['prediction'] * 1.15
            #}
            #st.line_chart(cost_range)
    
    # Dataset information
    st.sidebar.markdown("---")
    
    
    # Main content area - Dataset preview
    st.header("📁 Dataset Preview")
    
    if os.path.exists('urban_planning_dataset.csv'):
        df = pd.read_csv('urban_planning_dataset.csv')
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Projects", len(df))
        with col2:
            st.metric("Average Cost", f"${df['total_cost_millions'].mean():.2f}M")
        with col3:
            st.metric("Min Cost", f"${df['total_cost_millions'].min():.2f}M")
        with col4:
            st.metric("Max Cost", f"${df['total_cost_millions'].max():.2f}M")
        
        # Show sample data
        #st.subheader("Sample Data")
        #st.dataframe(df.head(10), use_container_width=True)
        
        # Statistics
        #with st.expander("📊 Dataset Statistics"):
          #  st.dataframe(df.describe(), use_container_width=True)
    else:
        st.warning("Dataset file not found. Please ensure 'urban_planning_dataset.csv' is in the project directory.")

else:
    st.error("""
    ⚠️ Model files are missing. 
    
    Please follow these steps:
    1. Run the Jupyter notebook: `Urban_Planning_Cost_Prediction.ipynb`
    2. Execute all cells to train and save the model
    3. Refresh this Streamlit app
    """)

