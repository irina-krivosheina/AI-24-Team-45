import streamlit as st

st.title("Fit Model")

st.header("Training Settings")

learning_rate = st.number_input("Learning Rate", min_value=0.0001, max_value=1.0, value=0.001, step=0.0001)
epochs = st.number_input("Epochs", min_value=1, max_value=100, value=10, step=1)
batch_size = st.number_input("Batch Size", min_value=1, max_value=128, value=32, step=1)

uploaded_file = st.file_uploader("Upload Dataset File", type=["zip"])

if st.button("Start Training"):
    st.info("This feature will be implemented in future versions.")
