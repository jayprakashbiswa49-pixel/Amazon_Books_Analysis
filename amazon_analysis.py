import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("bestsellers.csv")

# -------------------------------
# BASIC INFORMATION
# -------------------------------

print("Amazon Best-Selling Books Analysis")
print("-----------------------------------")

print("Total Books:", len(df))
print("Average Rating:", round(df["User Rating"].mean(), 2))
print("Average Price:", round(df["Price"].mean(), 2))

# -------------------------------
# 1. TOP 10 MOST REVIEWED BOOKS
# -------------------------------

top_books = df.sort_values(
    by="Reviews",
    ascending=False
).head(10)

plt.figure(figsize=(12, 6))

plt.bar(
    top_books["Name"],
    top_books["Reviews"]
)

plt.title("Top 10 Most Reviewed Amazon Books")
plt.xlabel("Book")
plt.ylabel("Number of Reviews")

plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# -------------------------------
# 2. FICTION VS NON-FICTION
# -------------------------------

genre_count = df["Genre"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    genre_count.values,
    labels=genre_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Amazon Best-Selling Books by Genre")

plt.show()


# -------------------------------
# 3. BOOKS BY YEAR
# -------------------------------

books_year = df["Year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))

plt.plot(
    books_year.index,
    books_year.values,
    marker="o"
)

plt.title("Amazon Best-Selling Books by Year")
plt.xlabel("Year")
plt.ylabel("Number of Books")

plt.grid()
plt.tight_layout()
plt.show()


# -------------------------------
# 4. AVERAGE RATING BY GENRE
# -------------------------------

rating_genre = df.groupby(
    "Genre"
)["User Rating"].mean()

plt.figure(figsize=(7, 5))

plt.bar(
    rating_genre.index,
    rating_genre.values
)

plt.title("Average Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")

plt.ylim(0, 5)
plt.tight_layout()
plt.show()


# -------------------------------
# 5. AVERAGE PRICE BY GENRE
# -------------------------------

price_genre = df.groupby(
    "Genre"
)["Price"].mean()

plt.figure(figsize=(7, 5))

plt.bar(
    price_genre.index,
    price_genre.values
)

plt.title("Average Book Price by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Price ($)")

plt.tight_layout()
plt.show()


print("\nAnalysis completed successfully!")