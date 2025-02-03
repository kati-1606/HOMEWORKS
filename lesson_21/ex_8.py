# Dictionaries Exercise:
# Create a dictionary of book titles and their authors.
# Write a function to search for a book by its title and return the author's name.

def find_author_by_title(book_dict, title):
    if title in book_dict:
        return book_dict[title]
    else:
        return "Book not found."

book_dict = {
    "To Kill a Mockingbird": "Harper Lee",
    "1984": "George Orwell",
    "The Great Gatsby": "Scott Fitzgerald",
    "Moby Dick": "Herman Melville"
}

title = "1984"
author = find_author_by_title(book_dict, title)

print(f"The author of '{title}' is {author}")
