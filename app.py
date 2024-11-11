import streamlit as st
from cesar import cesar_encrypt, cesar_decrypt
from vigenere import vigenere_encrypt, vigenere_decrypt

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

st.set_page_config(page_title="Criptografía PIA", layout="centered")

# Sidebar for navigation
st.sidebar.title("Criptografía PIA")
page = st.sidebar.selectbox("Menú", ["Home", "Cesar", "Vigenère"])

# Home page
if page == "Home":
    st.title("Proyecto para PIA de criptografía y seguridad")
    st.write("Pedro Antonio González Soto")
    st.write("2006251")

    st.write("La siguiente aplicación tiene como propósito mostrar el funcionamiento \
        de al menos dos técnicas de cifrado y descifrado vistas en la clase de Criptografía y Seguridad.")
    st.write("Los métodos aquí utilizados son el método César y el método de Vigenère, se implementan con el abecedario en inglés (sin incluír ñ)")
    
    st.title("Método César")
    st.write("El método de cifrado Cesar es un método de cifrado simétrico que toma como clave un entero k\
        y para cada letra del texto plano a cifrar, se mueve k cantidad de veces a la derecha del abecedario para generar\
            la letra del texto cifrado (Esto tomando módulo el tamaño del abecedario)")
    st.write("Por ejemplo, si queremos cifrar el mensaje `HOLA` con la clave `CLAVE`, \
        repetimos la clave hasta que tenga el mismo tamaño que el mensaje, de modo que la clave se convierte en `CLAV`. \
        Luego, ciframos cada letra con el desplazamiento correspondiente.")
    st.write("Resultado del ejemplo: `JZLV`")

    st.title("Método Vigenère")
    st.write("El método de cifrado de Vigenère , a diferencia del cifrado César, \
        que utiliza un solo desplazamiento para todas las letras del mensaje, \
        utiliza una palabra clave (key) para determinar el desplazamiento \
        de cada letra de manera individual.")
    st.write("Por ejemplo, si queremos cifrar el texto claro EMPEZAR con una llave igual a 3, moveríamos cada\
        letra 3 espacios a la derecha en el abecedario, de manera que la letra E se convierte H, la M en P, la P en S,\
        la Z en C, la A en D y la R en U., dando el texto: HPSHCDU")

if page == "Cesar":
    st.title("Encriptado/Desencriptado por el método Cesar")

    # Input para cifrado Cesar
    option = st.radio("elige una opción:", ("Encriptar", "Desencriptar"))
    message = st.text_input("Ingrese el mensaje:")
    shift = st.slider("Seleccione la clave:", 1, 25, 3)

    
    if st.button("Ejecutar"):
        if option == "Encriptar":
            result = cesar_encrypt(message, shift, alphabet)
        else:
            result = cesar_decrypt(message, shift, alphabet)
        st.write("Resultado:", result)

# Página para cifrado de Vigenère
elif page == "Vigenère":
    st.title("Encriptado/Desencriptado por el método Vigenère")

    # Input
    option = st.radio("Eliga una opción:", ("Encriptar", "Desencriptar"))
    message = st.text_input("Ingrese el mensaje:")
    key = st.text_input("Ingrese la clave:")

    # Output
    if st.button("Ejecutar"):
        if option == "Encriptar":
            result = vigenere_encrypt(message, key, alphabet)
        else:
            result = vigenere_decrypt(message, key, alphabet)
        st.write("Resultado:", result)