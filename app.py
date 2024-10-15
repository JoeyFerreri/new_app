import streamlit as st

import pandas as pd
# Title of the app
st.title('Interactive Sales Data Visualization App')

# Pre-loaded dataset for sales information
data = {
    'Students': ['Joey F.', 'Max S.', 'Maddie H,', 'Grace D.', 'Yubei S.'],
    'GPA': [4.33, 0, 4.33, 4.33, 4.33]
}
df = pd.DataFrame(data)

# Display the dataset
st.write("GPA's:")
st.write(df)

# Let the user select columns for the chart
columns = df.columns.tolist()

# Dropdowns for X and Y axes selection
x_axis = st.selectbox('Select column for X-axis', columns)
y_axis = st.selectbox('Select column for Y-axis', columns)

# Display chart based on user selections
st.bar_chart(df[[x_axis, y_axis]].set_index(x_axis))


