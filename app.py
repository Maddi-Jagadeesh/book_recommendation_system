import streamlit as st
import pickle
import numpy as np

# -----------------------------
# Load Data
# -----------------------------
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

st.set_page_config(page_title="Book Recommendation System", layout="wide")

st.title("📚 Book Recommendation System")

# ===================================================
# Recommendation System First
# ===================================================
st.header("🔍 Get Book Recommendations")

book_list = pt.index.values
selected_book = st.selectbox("Type or select a book you like:", book_list)

if st.button("Recommend"):
    try:
        index = np.where(pt.index == selected_book)[0][0]
        similar_items = sorted(
            list(enumerate(similarity_scores[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:5]

        st.subheader("You might also like:")
        # Show recommendations in one row with columns
        cols = st.columns(len(similar_items))
        for col, i in zip(cols, similar_items):
            temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
            title = temp_df['Book-Title'].values[0]
            author = temp_df['Book-Author'].values[0]
            image_url = temp_df['Image-URL-M'].values[0]
            with col:
                st.image(image_url, width=150)
                st.markdown(f"**{title}**")
                st.caption(f"by {author}")
    except Exception as e:
        st.error(f"Could not recommend books: {e}")

st.header("🔥 Popular Books")

# Display popular books in rows of cards, 5 per row
for i in range(0, len(popular_df), 5):
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        if i + idx < len(popular_df):
            row = popular_df.iloc[i + idx]
            with col:
                st.image(row['Image-URL-M'], width=150)
                st.markdown(f"**{row['Book-Title']}**")
                st.caption(f"by {row['Book-Author']}")
                st.write(f"⭐ {row['avg_rating']} | 🗳 {row['num_ratings']}")
