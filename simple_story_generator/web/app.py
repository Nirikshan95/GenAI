import streamlit as st
import sys
sys.path.append(".") 
from main import main
st.title("Story Generator")
story_type = st.selectbox("Select a story type",["Adventure", "Mystery", "Fantasy", "Sci-Fi", "Horror", "Romance", "Thriller", "Comedy", "Drama", "Historical", "Crime", "Supernatural", "Western", "Dystopian", "Mythology", "Slice of Life", "Coming of Age", "Fairy Tale", "Noir", "Post-Apocalyptic", "Cyberpunk", "Steampunk", "Paranormal", "Psychological", "War", "Survival", "Time Travel", "Political", "Satire"]
)
if st.button("Generate Story"):
    with st.spinner("Generating story..."):
        response = main(story_type)
        st.success("Story generated!")
        st.write(response)