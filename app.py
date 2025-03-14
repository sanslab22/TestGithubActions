import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

import os

if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
    os.system(f"streamlit run app.py --server.port {port} --server.address 0.0.0.0")
else:
    os.system("streamlit run app.py")


# Title of the app
st.title("Simple Streamlit Demo App")

# Add a description
st.write("This is a simple Streamlit app that demonstrates a slider and a plot.")

# Slider for user input
x_value = st.slider('Select a value for x', 0, 100, 25)

# Generate data based on the slider value
x = np.linspace(0, 10, 100)
y = np.sin(x * x_value)

# Display the plot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f"Plot of sin(x * {x_value})")

# Show the plot in the Streamlit app
st.pyplot(fig)

# Display the selected value
st.write(f"You selected {x_value} for x, which is used in the sine function.")
