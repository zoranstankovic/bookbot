# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

# BookBot: A Text Analysis Tool

BookBot is a simple Python program that analyzes a text file (intended for books) and provides some basic statistics. It counts the total number of words and provides a frequency count of each letter appearing in the text.

## Description

The program takes the path to a text file as a command-line argument.  It then performs the following actions:

1.  **Reads the Book:** Loads the entire content of the specified text file.
2.  **Word Count:** Calculates the total number of words in the text.  It uses a simple split-based approach, so punctuation attached to words will be counted as part of the word (e.g., "hello!" is one word).
3.  **Character Count:**  Counts the occurrences of each character in the text.  This includes all characters (letters, numbers, punctuation, spaces, etc.).
4.  **Character Frequency Report:** Presents a sorted report showing the count of each *letter* (a-z, case-insensitive) in descending order of frequency.  Non-letter characters are ignored in the final report.
5. **Prints all results to standard output**
