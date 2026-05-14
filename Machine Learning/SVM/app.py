#Import Libraries
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
st.set_page_config(page_title="SVM App")

# Background Image 
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url(https://thumbs.dreamstime.com/b/wildflower-iris-flower-frame-watercolor-style-isolated-full-name-plant-purple-aquarelle-wild-87355559.jpg);
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

#Title
st.title('IRIS FLOWERS PREDICTION APP')

#Dataset
data=load_iris()
X=data.data
y=data.target

#Train-Test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#Side Input 
st.sidebar.header('Enter Flower Details')
sepal_length=st.sidebar.slider("Sepal Length",4.0,8.0,5.0)
sepal_width=st.sidebar.slider("Sepal Width",2.0,5.0,3.0)
petal_length=st.sidebar.slider("Petal Length",1.0,7.0,4.0)
petal_width=st.sidebar.slider("Petal Width",0.1,3.0,1.0)

#Model
model=SVC(kernel='linear')
model.fit(X_train,y_train)

#Predictions
input_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]
prediction= model.predict(input_data)
flower_name = data.target_names[prediction[0]]

#Display Predictions
if st.button('Predict'):
    st.success(f"Predicted Flower:{flower_name}")

#Accuracy
y_pred=model.predict(X_test)
acc=accuracy_score(y_test,y_pred)

st.write("Model Accuracy",round(acc*100,2))