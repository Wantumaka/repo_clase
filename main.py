import seaborn as sns
import streamlit as st

import pandas as pd
#import plotly.express as px

st.set_page_config(page_title="Iris Dataset", page_icon="🌺", layout="wide")

import geocoder

g = geocoder.ip('me')
st.write(g.latlng) 



def main():
    df = sns.load_dataset('iris')

    st.title("Iris Dataset")
    st.expander("Mostrar dataframe")
    #st.dataframe(df.head(1))
    
    

    col1, col2 = st.columns(2)

    with col1:
        sl = st.slider(label ='sepal_length', min_value = df['sepal_length'].min(), max_value = df['sepal_length'].max())
        sw = st.slider(label ='sepal_width', min_value = df["sepal_width"].min(), max_value = df["sepal_width"].max())
        

    with col2:
        pl =st.slider(label = 'petal_length', min_value = df['petal_length'].min(), max_value = df['petal_length'].max())
        pw =st.slider(label = 'petal_width', min_value = df['petal_width'].min(), max_value = df['petal_width'].max())
        
    
    eleccion = pd.DataFrame({'sepal_length': [sl], 'sepal_width': [sw], 'petal_length': [pl], 'petal_width': [pw], 'species': ['Sin definir']})
    df = pd.concat([df, eleccion])

    with col1:
        st.plotly_chart(px.scatter(data_frame=df, x="sepal_length", y="sepal_width", color="species"))

    with col2:
        st.plotly_chart(px.scatter(data_frame=df, x="petal_length", y="petal_width", color="species"))

    bot1, bot2, bot3 = st.columns([1.5, 1, 1])
    bot2.button("Predicción", help="Botón para predecir la especie de la flor", icon="🌺")


    with open("model.pkl", "rb") as file:
        model = pkl.load(file)

    # Interfaz en Streamlit para realizar predicciones
    if st.button("Predict"):
        # Valores de entrada (deben estar definidos previamente)
        x1, x2, x3, x4 = 1.0, 2.0, 3.0, 4.0  # Reemplazar con valores reales o dinámicos
        prediction = model.predict([[x1, x2, x3, x4]])[0]
        st.success(prediction)

if __name__ == "__main__":
    main()