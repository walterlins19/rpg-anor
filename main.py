import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Portal do Aventureiro",
    page_icon="⚔️",
    layout="wide",
)

# Estilo CSS personalizado para a página inicial
st.markdown(
    """
    <style>
    .big-font {
        font-size:4.5em !important;
        font-weight: bold;
        color: #a67324;
        text-shadow: 2px 2px 4px #000000;
    }
    .welcome-text {
        font-size:1.5em;
        color: #ffffff;
    }
    .container {
        background-image: url('https://i.pinimg.com/originals/f3/69/82/f36982d78930af3d70c805966b7c86ff.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        padding: 40px;
        border-radius: 10px;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .button-link {
        background-color: #a67324;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .button-link:hover {
        background-color: #805919;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Container principal com fundo temático
st.markdown(
    """
    <div class="container">
        <h1 class="big-font">Bem vindo ao mundo de Anor Lombo</h1>
        <p class="welcome-text">
            Seja bem-vindo, bravo herói! Prepare-se para embarcar em aventuras épicas e trilhar um caminho lendário.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# Botões de direcionamento para outras páginas
st.markdown("<br>", unsafe_allow_html=True) # Add some space
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📜 Criar Personagem", key="btn1"):
        st.switch_page("pages/1_Criar_Personagem.py")
with col2:
    if st.button("🗺️ Mapa do Mundo", key="btn2"):
        st.switch_page("pages/2_Mapa_do_Mundo.py")
with col3:
    if st.button("🎲 Simulador de Combate", key="btn3"):
        st.switch_page("pages/3_Simulador_de_Combate.py")

# Nota de rodapé
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #ffffff;'>Criado com a magia da tecnologia e paixão por RPG!</p>",
    unsafe_allow_html=True,
)