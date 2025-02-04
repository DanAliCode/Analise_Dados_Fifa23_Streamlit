import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)
df_data = st.session_state["data"]
# df_data

# Criando o sidebar

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Club", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Name", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(player_stats["Photo"])
st.title(player_stats["Name"])

st.markdown(f"**Clube** {player_stats["Club"]}")
st.markdown(f"**Posição** {player_stats["Position"]}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade** {player_stats["Age"]}")
col2.markdown(f"**Altura** {player_stats["Height(cm.)"] / 100}")
col3.markdown(f"**Peso** {player_stats["Weight(lbs.)"]*0.453:.2f}")
st.divider()

# Criando a parte do Overall
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

#Criando dados de valores dos jogadores

col5, col6, col7, col8 = st.columns(4)
col5.metric(label="Valor de mercado", value=f"Euro{player_stats['Value(£)']:,}")
col6.metric(label="Remuneração semanal", value=f"Euro{player_stats['Wage(£)']:,}")
col7.metric(label="Cláusula de rescição", value=f"Euro{player_stats['Release Clause(£)']:,}")