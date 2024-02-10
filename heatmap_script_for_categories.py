import pandas as pd
import folium
from folium.plugins import HeatMap

# Step 1: Data Preprocessing
excel_file = r'C:\Users\philip.otieno\Desktop\Mappings_Nairobi\Nairobi heat map\2_wheeler.xlsx'  # Update with your Excel file name
data = pd.read_excel(excel_file)
columns_to_extract = ['Latitude', 'Longitude', 'Category']  # Include 'Category' in the columns to extract
filtered_data = data[columns_to_extract]

# Step 2: Map Generation with Folium
kenya_coords = [-1.2921, 36.8219]
m = folium.Map(location=kenya_coords, zoom_start=10)

# Handle missing values in Latitude and Longitude
filtered_data = filtered_data.dropna(subset=['Latitude', 'Longitude'])  # Drop rows with missing location values

# Add color-coded markers to the map based on the 'Category' column
for index, row in filtered_data.iterrows():
    category = row['Category']
    color = 'lightgreen' if category == 'Trips' else 'red' if category == 'Driver Cancellation' else 'yellow' if category == 'Rider Cancellation' else 'lightblue' if category == 'No Drivers Found' else 'gray'
    folium.Marker(location=(row['Latitude'], row['Longitude']), icon=folium.Icon(color=color), popup=category).add_to(m)


# Save the map as an HTML file
m.save('category_map.html')
