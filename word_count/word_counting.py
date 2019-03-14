"""Count words."""
import re


def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # Convert to lowercase
    lower_text = text.lower()

    # Split text into tokens (words), leaving out punctuation
    words = re.sub(r'[^a-zA-Z ]', '', lower_text).split()
    
    # Aggregate word counts using a dictionary
    counts = {x:words.count(x) for x in words}

    return counts


def main():
    with open("data.txt", "r") as f:
        text = f.read()
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    main()



