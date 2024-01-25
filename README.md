## SearchEngine

# Introduction: 
This Search Engine is a simple Python-based search tool designed for processing HTML files, building an occurrence map, and providing ranked search results. This project implements a basic search engine utilizing a Trie data structure. The engine processes HTML files, builds an occurrence map, and allows users to search for terms, displaying ranked results based on occurrence counts.This README provides an overview of the approach, algorithms, and data structures employed in the project.

# Approach: 

1. Trie Structure

The Trie structure is utilized for efficient word storage and retrieval. It consists of two classes:
a. TrieStructureNode: Represents nodes in the Trie with a dictionary to store children nodes and a flag indicating the end of a key.
b. TrieStructure: Manages the Trie, with functions to create nodes, get indices, insert keys, and search for keys.

2. HTML File Processing

The engine processes HTML files to create an occurrence map. It uses the BeautifulSoup library for HTML parsing and the Natural Language Toolkit (NLTK) for text processing. The key steps include tokenization, removal of stopwords, and stemming to reduce words to their root form. The engine processes HTML files using BeautifulSoup for parsing and the steps include tokenization, removal of stopwords, and stemming to build an occurrence map. This map associates stemmed words with HTML files and their respective occurrence counts.

3. Occurrence Map

The occurrence map is a dictionary that associates each stemmed word with a sub-dictionary containing HTML file names and their respective occurrence counts. This map serves as the basis for ranking search results.

4. Search Functionality

The search functionality involves traversing the Trie and using the occurrence map to rank and display search results. The engine allows users to input search terms and provides ranked results based on the occurrence count of the stemmed words. Search results are ranked based on occurrence counts of stemmed words. The engine sorts and displays results in descending order of occurrence.

# Algorithms and Data Structures

Trie Insertion and Search

The Trie structure enables efficient insertion and search operations. The `insert` function traverses the Trie to insert each character of a word, marking the last node as the end of the key. The `search` function traverses the Trie to find a specific key.

HTML File Processing

The project employs BeautifulSoup for HTML parsing and NLTK for tokenization, stopwords removal, and stemming. These libraries enhance the accuracy of word extraction and processing.

Ranked Search Results

Search results are ranked based on the occurrence counts of stemmed words in HTML files. The engine uses sorting algorithms to present results in descending order of occurrence. 

Usage

1. Setup NLTK Resources:
   - Run the `setup_nltk` function to download necessary NLTK resources (`punkt` and `stopwords`).

2. Build Occurrence Map:
   - Use the `build_occurrence_map` function to process HTML files and create the occurrence map.

3. Search Engine Interaction:
   - Execute the `main` function to start the search engine.
   - Enter search terms when prompted, and the engine will display ranked results.
  
# Dependencies

- Python 3.x
- NLTK
- BeautifulSoup

# Trie Data Structure:
Trie is a tree-based data structure used for efficient string storage and searching. It provides fast and space-efficient searches for words or patterns in a collection of strings.

# Advantages:
Efficient Search: Trie searches in O(m) time, where m is the length of the search query. This makes it suitable for applications like auto-completion and spell-checking.
Memory Efficiency: Trie can be compressed by merging nodes with a single child, reducing memory usage without compromising search speed.


# Usage in the Code
The Trie structure is used to store a collection of words along with associated data. The insert() method adds words to the Trie, compress() reduces its size by merging nodes, and search() retrieves associated data for given words.


# Author

- Riddhi Mahesh Dange

