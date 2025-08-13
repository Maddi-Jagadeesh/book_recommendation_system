# Book Recommendation System

This project implements a book recommendation system using a collaborative filtering approach. By analyzing user ratings, the system identifies patterns and similarities between users and books to provide personalized recommendations. The goal is to suggest new books that a user is likely to enjoy based on the preferences of similar users.

## Features

  - Collaborative Filtering The core of the system is a collaborative filtering algorithm that finds books with high similarity scores based on how users have rated them.
  - Data Preprocessing The system intelligently filters the dataset to include only users who have rated more than 200 books and famous books that have received at least 50 ratings to ensure meaningful recommendations and handle data sparsity.
  - Cosine Similarity The project uses cosine\_similarity from scikit-learn to calculate the similarity between books forming the basis of the recommendation logic.
  - Recommendation Function A dedicated recommend function takes a book title as input and returns the top 4 most similar books along with their author and a link to their image.

## Technologies Used

  * **Python** The main programming language.
  * **NumPy** Used for numerical operations particularly for handling arrays and indices.
  * **Pandas** Essential for data manipulation cleaning and creating the pivot table of user-book ratings.
  * **Scikit-learn** The cosine\_similarity function is used for calculating the similarity between books.

## How to Run Locally

1.  **Clone the repository**
    git clone [[https://github.com/Maddi-Jagadeesh/book-recommendation-system.git](https://github.com/Maddi-Jagadeesh/book_recommendation_system/tree/main)]
    cd book-recommendation-system
2.  **Install the dependencies**
    pip install numpy pandas scikit-learn
3.  **Prepare the Dataset**
    The system relies on a dataset containing book titles authors ratings and user IDs. Ensure your dataset is properly structured and available in the project directory.
4.  **Run the script**
    Execute the Python script to generate recommendations. The recommend() function can be called with a book title to get a list of suggested books.
