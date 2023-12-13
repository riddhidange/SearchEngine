#Name: Riddhi Mahesh Dange
#CWID: 20012299
#Course: CS600 Advanced Algorithm Design and Implementation
#Semester: Fall 2023

# Install necessary libraries
# This is just to ensure program execution does not fail
import os
os.system('python3 -m pip install nltk > /dev/null')
os.system('python3 -m pip install bs4 > /dev/null')
os.system('python3 -m pip install tabulate > /dev/null')

# Importing necessary libraries
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from tabulate import tabulate  # Added for tabular formatting


# Constructing Trie structure node class to represent nodes in the trie
class TrieStructureNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Flag to indicate the end of a key in the trie
        self.end = False

# Code for Trie structure class for efficient word storage and retrieval
class TrieStructure:
    def __init__(self):
        # Initializing the trie with an empty root node
        self.root = self.create_node()

    def create_node(self):
        # Creating a new trie node
        return TrieStructureNode()

    def get_index(self, key_level):
        # Helper function to get the index for a given key level (character)
        return key_level

    def insert(self, key):
        # Inserting a key into the trie
        curr = self.root

        # Traversing the trie to insert each character of the key
        for level in range(len(key)):
            index = self.get_index(key[level])
            if index not in curr.children:
                curr.children[index] = self.create_node()
            curr = curr.children[index]

        # Marking the last node as the end of the key
        curr.end = True

    def search(self, key):
        # Searching for a key in the trie
        curr = self.root

        # Traversing the trie to search for each character of the key
        for level in range(len(key)):
            index = self.get_index(key[level])
            if index not in curr.children:
                return
            curr = curr.children[index]

        return curr

# Building occurrence map from HTML files
def build_occurrence_map(html_files_directory):
    # Dictionary to store word occurrences per HTML file
    occurrence_map = {}

    # Exclude punctuation
    translator = str.maketrans("", "", string.punctuation)

    # Iterate through HTML files in the specified directory
    html_files = os.listdir(html_files_directory)
    for html_file in html_files:
        with open(html_files_directory + html_file, 'r', encoding="utf8", errors='ignore') as file:
            # Parse HTML content using BeautifulSoup
            soup = BeautifulSoup(file, 'html.parser')
            text_data = soup.get_text()

            # Tokenize and filter words, excluding stop words and punctuation
            tokenized_data = word_tokenize(text_data)
            stop_words = set(stopwords.words('english'))
            filtered_data = [w.lower() for w in tokenized_data if
                             w.lower() not in stop_words and w.isalnum()]

            # Build occurrence map with stemmed words and their counts per HTML file
            for word in filtered_data:
                word = PorterStemmer().stem(word)
                if word not in occurrence_map:
                    occurrence_map[word] = {}
                if html_file not in occurrence_map[word]:
                    occurrence_map[word][html_file] = 0
                occurrence_map[word][html_file] += 1

    return occurrence_map

# Displaying search results with ranks and occurrences in tabular format
def get_search_results(occurrence_map, search_key):
    search_key = search_key.lower()
    translator = str.maketrans("", "", string.punctuation)
    search_key = search_key.translate(translator)
    stemmed_keys = [PorterStemmer().stem(word) for word in search_key.split()]

    # Check if all stemmed keys exist in the occurrence map
    if not all(key in occurrence_map for key in stemmed_keys) or not stemmed_keys:
        print('No search results found!')
        return

    # Get common files for all stemmed keys
    common_files = set(occurrence_map[stemmed_keys[0]].keys())
    for key in stemmed_keys[1:]:
        common_files &= set(occurrence_map[key].keys())

    # If no common files found, no results
    if not common_files:
        print('No search results found!')
        return

    # Calculate total occurrences for each file
    file_occurrences = {}
    for file in common_files:
        total_occurrences = sum(occurrence_map[key][file] for key in stemmed_keys)
        file_occurrences[file] = total_occurrences

    # Sort results by total occurrence count in descending order
    sorted_results = sorted(file_occurrences.items(), key=lambda x: x[1], reverse=True)

    headers = ["Rank", "File Name", "Total Occurrences"]
    data = []

    rank = 1
    for r in sorted_results:
        file_name = r[0]
        total_occurrences = r[1]
        data.append([rank, file_name, total_occurrences])
        rank += 1

    # Displaying tabular results
    print(tabulate(data, headers=headers, tablefmt="pretty"))

# Downloading necessary NLTK resources
def setup_nltk():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)

# Main function to orchestrate the search engine
def main():
    setup_nltk()

    trie = TrieStructure()

    html_files_directory = './html/'
    occurrence_map = build_occurrence_map(html_files_directory)

    # Insert keys into the trie
    keys = occurrence_map.keys()
    for key in keys:
        trie.insert(key)

    print("Welcome to the CS600 Search Engine by Riddhi Mahesh Dange")
    while True:
        search_key = input('Enter your search term (type quit to exit): ')
        if search_key.lower() == 'quit':
            break
        elif not search_key.strip():  # Check if the input is empty
            print("Please provide input")
        else:
            get_search_results(occurrence_map, search_key)

    print('Thanks for searching!')

# Entry point to start the program
if __name__ == '__main__':
    main()