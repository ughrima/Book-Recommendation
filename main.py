import pickle
import streamlit as st
import numpy as np
import pandas as pd

st.header('Book Recommender System ')

# Load pre-trained model and data
model = pickle.load(open('Model.pkl', 'rb'))
book_names = pickle.load(open('Book_Names.pkl', 'rb'))
final_rating = pickle.load(open('Final_Rating.pkl', 'rb'))
book_pivot = pickle.load(open('Book_Pivot.pkl', 'rb'))

# Load URL DataFrame
url = pd.read_csv('url_data.csv')

def fetch_poster(suggestion):
    poster_url = []

    for book_id in suggestion:
        book_title = book_pivot.index[book_id]
       
        url_row = url[url['title'] == book_title]
        print(f"Looking for URL for book title: {book_title}")
        print(f"Found rows: {url_row}") 
        if not url_row.empty:
            poster_url.append(url_row.iloc[0]['url']) 
        else:
            poster_url.append('') 

    return poster_url

def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion[0]) 
    for i in suggestion[0]:  
        books_list.append(book_pivot.index[i])
    
    return books_list, poster_url

selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)
    
    num_cols = 3
    books_to_display = [(book, poster) for book, poster in zip(recommended_books, poster_url) if book != selected_books]
    num_recommended_books = len(books_to_display)
    rows_needed = (num_recommended_books + num_cols - 1) // num_cols  

    current_index = 0
    for row in range(rows_needed):
        cols = st.columns(num_cols)
        for col in cols:
            if current_index < num_recommended_books:
                book_title, book_poster = books_to_display[current_index]
                col.text(book_title)
                if book_poster:  
                    col.image(book_poster, use_column_width=True)
                current_index += 1
