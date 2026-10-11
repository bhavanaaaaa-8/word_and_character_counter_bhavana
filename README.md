
## Project Description
The Paragraph Analyzer is a Python program that accepts a paragraph from the user and calculates the total number of characters, words, sentences, and spaces. It uses Python's built-in string methods and regular expressions to analyze the paragraph.

## Features
- **Character Count:** Counts all characters, including letters, numbers, spaces, and punctuation.
- **Word Count:** Uses `split()` to count words separated by whitespace.
- **Sentence Count:** Identifies sentence-ending punctuation such as periods (`.`), question marks (`?`), and exclamation marks (`!`).
- **Space Count:** Counts the spaces between words and other text.
- **Empty Input Validation:** Displays an error message if the user enters an empty paragraph or only whitespace.
- **Punctuation Handling:** Treats consecutive punctuation marks, such as `?!` and `...`, as a single sentence ending.

## Technologies Used
- Python 3
- `re` module for regular expressions
- Built-in string methods such as `split()`, `count()`, and `strip()`

## Requirements
- Python 3 installed on your computer.
- A code editor or terminal to run the program.

## How to Run
1. Save the Python code in a file named `paragraph_analyzer.py`.
2. Open a terminal or command prompt in the folder containing the file.
3. Run the following command:

   ```bash
   python paragraph_analyzer.py
   ```

4. Enter a paragraph when prompted.
5. View the character, word, sentence, and space counts.

## Example Output

```text
Enter a paragraph: Hello world! How are you?

--- Paragraph Analysis ---
Characters: 26
Words: 5
Sentences: 2
Spaces: 4
```

## Empty Input Example

```text
Enter a paragraph:

Error: Paragraph cannot be empty.
```

## Concepts Practiced
- Variables and data types
- User input using `input()`
- Conditional statements (`if` and `else`)
- Loops and character processing
- String methods
- Regular expressions
- Input validation

## Limitations
The sentence counter uses punctuation patterns and may not correctly identify every sentence in complex text. For example, abbreviations such as `Dr.` may be counted incorrectly.

## Future Improvements
- Improve sentence detection for abbreviations and decimal numbers.
- Display average word and sentence lengths.
- Save analysis results to a text file.

## Author
Created as a Python practice project to develop string manipulation, regular expression, and input-validation skills.

