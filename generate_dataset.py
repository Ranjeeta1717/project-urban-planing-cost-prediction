import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n = 2000

# Generate synthetic data
data = {
    'project_id': range(1, n + 1),
    'area_sqkm': np.random.uniform(0.5, 50, n),
    'population_density': np.random.uniform(100, 5000, n),
    'infrastructure_type': np.random.choice(['Residential', 'Commercial', 'Mixed', 'Industrial', 'Public'], n),
    'land_cost_per_sqkm': np.random.uniform(50000, 500000, n),
    'construction_cost_index': np.random.uniform(0.8, 1.5, n),
    'distance_to_city_center': np.random.uniform(1, 30, n),
    'existing_infrastructure_score': np.random.uniform(0.2, 1.0, n),
    'environmental_factors': np.random.uniform(0.5, 1.0, n),
    'zoning_complexity': np.random.uniform(0.3, 1.0, n),
    'project_duration_years': np.random.uniform(1, 10, n),
}

df = pd.DataFrame(data)

# Generate target variable (total_cost_millions) with realistic relationships
df['total_cost_millions'] = (
    df['area_sqkm'] * df['land_cost_per_sqkm'] / 1000000 +
    df['population_density'] * 100 +
    df['construction_cost_index'] * 50000 +
    df['distance_to_city_center'] * 2000 +
    (1 - df['existing_infrastructure_score']) * 30000 +
    df['zoning_complexity'] * 20000 +
    df['project_duration_years'] * 5000 +
    np.random.normal(0, 5, n)
)

# Ensure positive costs
df['total_cost_millions'] = np.abs(df['total_cost_millions'])

# Round to 2 decimal places
df['total_cost_millions'] = df['total_cost_millions'].round(2)

# Save to CSV
df.to_csv('urban_planning_dataset.csv', index=False)
print(f'Dataset created with {len(df)} samples')
print(f'Dataset shape: {df.shape}')
print(f'\nFirst few rows:')
print(df.head())

