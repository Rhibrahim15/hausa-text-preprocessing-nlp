import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)        # remove URLs
    text = re.sub(r"@\w+", "", text)           # remove mentions
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text) # remove punctuation
    return text


def tokenize(text):
    return text.split()


def remove_short_words(tokens, min_length=2):
    return [word for word in tokens if len(word) >= min_length]


def preprocess(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_short_words(tokens)
    return tokens


if __name__ == "__main__":

    example = "@user Ina son wannan sabon fim sosai!!!"

    result = preprocess(example)

    print("Original:", example)
    print("Processed:", result)