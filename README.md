# NepaliWordCounter

NepaliWordCounter is a Python-based project designed to analyze the frequency of unique Nepali words in a given text file. The tool processes the text by removing punctuation, handling Unicode characters, and counting the occurrences of each unique word. The results are then saved in a text file for easy reference.

## Features

- Removes punctuation and unwanted Unicode characters from the text.
- Counts the occurrences of each unique word.
- Outputs the sorted word frequency data to a text file.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Run the `uniqueNepaliWords` function:

    ```python
    python uniqueNepaliWords.py
    ```

2. The output will be saved in `U_Nepali_words.txt`.

## Code Overview

The core functionality is implemented in the `uniqueNepaliWords` function:

```python
import re
import string

def uniqueNepaliWords(test_file):
    temp = test_file.read()
    temp = temp.translate(temp.maketrans('', '', string.punctuation))  # remove punctuation
    temp = re.sub(r"[\b“”‘’•–।br]", " ", temp)  # replace unicode char with single space
    sep_temp = re.sub("\s+", " ", temp).split(" ")  # replace more than one spaces with single space
    uq_words = []
    occurance = []
    for i in sep_temp:
        if i not in uq_words:
            uq_words.append(i)
            occurance.append(sep_temp.count(i))
    
    # sorting in ascending order by their occurance
    for i in range(0, len(occurance) - 1):
        for j in range(0, len(occurance) - 1 - i):
            if occurance[j] > occurance[j + 1]:
                occurance[j], occurance[j + 1] = occurance[j + 1], occurance[j]
                uq_words[j], uq_words[j + 1] = uq_words[j + 1], uq_words[j]
    
    # convert into a dict & write in .txt file
    uWord = dict(zip(uq_words, occurance))
    with open("U_Nepali_words.txt", "w", encoding="UTF-8") as op:
        for word, ocr in uWord.items():
            op.write('%s --> %s\n' % (word, ocr))
    op.close()
    test_file.close()

uniqueNepaliWords(open("nepalitext.txt", "r", encoding="UTF-8"))
```

### Output

The output file `U_Nepali_words.txt` will contain the unique Nepali words and their occurrences in the following format:

```
word1 --> 5
word2 --> 3
word3 --> 1
```

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any enhancements or bug fixes.

## Contact

For any questions or suggestions, please reach out to aniketbera.ab@gmail.com .

---
