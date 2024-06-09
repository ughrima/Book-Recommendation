# Book Recommendation System 

## Overview

A book recommendation system that uses collaborative filtering to suggest books to users based on their reading preferences. This system is built using Python and has a Streamlit frontend for easy interaction.

## Features

- **Collaborative Filtering**: Recommends books based on user similarities.
- **Streamlit Frontend**: Interactive web interface to get book recommendations.
- **Dataset**: Uses book ratings, book information, and user information for recommendations.

## Dataset Description

The dataset contains three files:
1. **Books**: Information about books (author, title, publication year, etc.).
2. **Users**: Information about users (user id, location).
3. **Ratings**: Ratings given by users to books.

## Preprocessing

- Removed unnecessary columns.
- Renamed columns for easier use.
- Filtered users with at least 200 ratings and books with at least 50 ratings.

## Building the Model

- Created a pivot table with user ids as columns, book titles as rows, and ratings as values.
- Converted the pivot table to a sparse matrix.
- Trained a Nearest Neighbors model using the sparse matrix.

## Streamlit Interface

### Installation

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

### Usage

- Select a book from the dropdown menu.
- Click the "Show Recommendation" button to get recommended books along with their images.


## Conclusion

This book recommendation system efficiently recommends books based on user preferences using collaborative filtering and provides an interactive interface for users to get book recommendations.

---
