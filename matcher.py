import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

with open('linkage_matrix.pkl', 'rb') as f:
    Z = pickle.load(f)

with open('cluster_assignments.pkl', 'rb') as f:
    cluster_assignments = pickle.load(f)

data = pd.read_csv('medimatch_data.csv')
data['Cluster'] = cluster_assignments

def get_most_similar_medicine(query_medicine):
    if query_medicine not in data['Medicine Name'].values:
        raise ValueError(f"{query_medicine} is not in the dataset.")
    
    query_cluster = data[data['Medicine Name'] == query_medicine]['Cluster'].values[0]
    cluster_meds = data[data['Cluster'] == query_cluster].reset_index(drop=True)
    
    if query_medicine not in cluster_meds['Medicine Name'].values:
        raise ValueError(f"{query_medicine} not found in cluster {query_cluster}.")
    
    cluster_meds_processed = cluster_meds.drop(columns=['Medicine Name', 'Cluster'])
    scaler = StandardScaler()
    cluster_meds_processed_scaled = scaler.fit_transform(cluster_meds_processed)

    query_index = cluster_meds[cluster_meds['Medicine Name'] == query_medicine].index[0]
    nn = NearestNeighbors(n_neighbors=2, metric='euclidean')
    nn.fit(cluster_meds_processed_scaled)
    distances, indices = nn.kneighbors([cluster_meds_processed_scaled[query_index]])
    
    closest_medicine_index = indices[0][1]
    closest_medicine = cluster_meds.iloc[closest_medicine_index]['Medicine Name']
    
    return closest_medicine

query_medicine = "Zincold Tablet"
try:
    most_similar_medicine = get_most_similar_medicine(query_medicine)
    print(f"The most similar medicine to {query_medicine} is {most_similar_medicine}.")
except ValueError as e:
    print(e)
