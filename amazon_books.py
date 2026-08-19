import pandas as pd

# ==========================================
# 1. IMPORT DATA FROM CSV
# ==========================================

df = pd.read_csv("bestsellers.csv")

print("\n========== AMAZON BEST-SELLING BOOKS ANALYSIS ==========\n")

# Display first 5 records
print("First 5 rows:")
print(df.head())


# ==========================================
# 2. BASIC INFORMATION
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ==========================================
# 3. CHECK MISSING VALUES
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())


# ==========================================
# 4. REMOVE DUPLICATES
# ==========================================

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Dataset after removing duplicates:", df.shape)


# ==========================================
# 5. CLEAN COLUMN NAMES
# ==========================================

df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ==========================================
# 6. TOP 10 BEST-SELLING BOOKS
# ==========================================

print("\n========== TOP 10 BOOKS BY REVIEWS ==========\n")

top_books = df.sort_values(
    by="Reviews",
    ascending=False
).head(10)

print(
    top_books[
        ["Name", "Author", "Reviews", "User Rating", "Price"]
    ]
)


# ==========================================
# 7. TOP AUTHORS
# ==========================================

print("\n========== TOP 10 AUTHORS ==========\n")

top_authors = df["Author"].value_counts().head(10)

print(top_authors)


# ==========================================
# 8. HIGHEST RATED BOOKS
# ==========================================

print("\n========== HIGHEST RATED BOOKS ==========\n")

highest_rated = df.sort_values(
    by="User Rating",
    ascending=False
).head(10)

print(
    highest_rated[
        ["Name", "Author", "User Rating", "Reviews"]
    ]
)


# ==========================================
# 9. MOST REVIEWED BOOKS
# ==========================================

print("\n========== MOST REVIEWED BOOKS ==========\n")

most_reviewed = df.nlargest(10, "Reviews")

print(
    most_reviewed[
        ["Name", "Author", "Reviews", "User Rating"]
    ]
)


# ==========================================
# 10. AVERAGE RATING
# ==========================================

average_rating = df["User Rating"].mean()

print("\nAverage User Rating:")
print(round(average_rating, 2))


# ==========================================
# 11. AVERAGE PRICE
# ==========================================

average_price = df["Price"].mean()

print("\nAverage Book Price:")
print(round(average_price, 2))


# ==========================================
# 12. FICTION VS NON-FICTION
# ==========================================

print("\n========== BOOKS BY GENRE ==========\n")

genre_count = df["Genre"].value_counts()

print(genre_count)


# ==========================================
# 13. AVERAGE RATING BY GENRE
# ==========================================

print("\n========== AVERAGE RATING BY GENRE ==========\n")

genre_rating = df.groupby("Genre")["User Rating"].mean()

print(genre_rating.round(2))


# ==========================================
# 14. AVERAGE PRICE BY GENRE
# ==========================================

print("\n========== AVERAGE PRICE BY GENRE ==========\n")

genre_price = df.groupby("Genre")["Price"].mean()

print(genre_price.round(2))


# ==========================================
# 15. BOOKS PER YEAR
# ==========================================

print("\n========== BOOKS BY YEAR ==========\n")

books_per_year = df["Year"].value_counts().sort_index()

print(books_per_year)


# ==========================================
# 16. AVERAGE RATING BY YEAR
# ==========================================

print("\n========== AVERAGE RATING BY YEAR ==========\n")

rating_by_year = df.groupby("Year")["User Rating"].mean()

print(rating_by_year.round(2))


# ==========================================
# 17. AVERAGE PRICE BY YEAR
# ==========================================

print("\n========== AVERAGE PRICE BY YEAR ==========\n")

price_by_year = df.groupby("Year")["Price"].mean()

print(price_by_year.round(2))


# ==========================================
# 18. MOST EXPENSIVE BOOKS
# ==========================================

print("\n========== TOP 10 MOST EXPENSIVE BOOKS ==========\n")

expensive_books = df.sort_values(
    by="Price",
    ascending=False
).head(10)

print(
    expensive_books[
        ["Name", "Author", "Price", "User Rating"]
    ]
)


# ==========================================
# 19. BOOKS WITH 5 STAR RATING
# ==========================================

print("\n========== 5 STAR BOOKS ==========\n")

five_star_books = df[df["User Rating"] == 5.0]

print(
    five_star_books[
        ["Name", "Author", "User Rating", "Reviews"]
    ]
)


# ==========================================
# 20. TOP AUTHORS BY AVERAGE RATING
# ==========================================

print("\n========== TOP AUTHORS BY AVERAGE RATING ==========\n")

author_rating = (
    df.groupby("Author")["User Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(author_rating.round(2))


# ==========================================
# 21. SAVE RESULTS
# ==========================================

top_books.to_csv("top_10_books.csv", index=False)

top_authors.to_csv("top_authors.csv")

genre_rating.to_csv("average_rating_by_genre.csv")

print("\nAnalysis completed successfully!")
print("Result files have been created.")