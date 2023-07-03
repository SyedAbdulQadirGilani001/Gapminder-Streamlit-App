import streamlit as st # Streamlit for the web app
import pandas as pd # Pandas for data manipulation
from sklearn import datasets # Scikit-learn for machine learning
from sklearn.ensemble import RandomForestClassifier # Random forest classifier

st.write("""  
# Simple Iris Flower Prediction App 
This app predicts the **Iris flower** type! 
""") # Markdown for the web app
st.sidebar.header('User Input Parameters') # Sidebar for user input parameters

def user_input_features(): # Function for user input features
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4) # Slider for sepal length
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4) # Slider for sepal width
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3) # Slider for petal length
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2) # Slider for petal width
    data = {'sepal_length': sepal_length, # Dictionary for user input features
            'sepal_width': sepal_width, # Dictionary for user input features
            'petal_length': petal_length, # Dictionary for user input features
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0]) # Dataframe for user input features
    return features # Return user input features

df = user_input_features() # User input features

st.subheader('User Input parameters') # Subheader for user input parameters
st.write(df) # Display user input parameters

iris = datasets.load_iris() # Load iris dataset
X = iris.data # Features
Y = iris.target # Target variable

clf = RandomForestClassifier() # Random forest classifier
clf.fit(X, Y) # Fit the model

prediction = clf.predict(df) # Prediction
prediction_proba = clf.predict_proba(df) # Prediction probability

st.subheader('Class labels and their corresponding index number') # Subheader for class labels and their corresponding index number
st.write(iris.target_names) # Display class labels and their corresponding index number

st.subheader('Prediction') # Subheader for prediction
st.write(iris.target_names[prediction]) # Display prediction
#st.write(prediction)

st.subheader('Prediction Probability') # Subheader for prediction probability
st.write(prediction_proba)  # Display prediction probability