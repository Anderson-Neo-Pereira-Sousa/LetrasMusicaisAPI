import requests
import streamlit as st

def buscarLetra(banda, musica):
    endpoint= f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    resposta =requests.get(endpoint)
    letra = resposta.json()["lyrics"] if resposta.status_code == 200 else ""
    return letra

st.image("https://imgur.com/SmktDIH.png")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda", key="banda")
musica = st.text_input("Digite o nome da música", key="musica")
pesquisar = st.button("Pesquisar")

if pesquisar:
    letra = buscarLetra(banda, musica)
    if letra:
        st.success("Letra encontrada")
        st.text(letra)
    else:
        st.error("Letra não encontrada")