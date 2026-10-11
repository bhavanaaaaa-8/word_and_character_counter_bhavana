import re
paragraph = input("Enter a paragraph: ")
if not paragraph.strip():
    print("Error: Paragraph cannot be empty.")
else:
    # Count characters
    characters = len(paragraph)
    # Count words using split()
    words = len(paragraph.split())
    # Count sentences, including combined punctuation
    sentences = len(re.findall(r'[.!?]+(?=\s|$)', paragraph))
    # Count spaces
    spaces = paragraph.count(" ")
    # Display results
    print("\n--- Paragraph Analysis ---")
    print("Characters:", characters)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Spaces:", spaces)
