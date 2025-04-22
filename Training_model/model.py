import nltk


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Head.Mouth import speak

# Load your Q&A dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':', 1) for line in lines if ':' in line]
        dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
    return dataset


# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

# Train the TF-IDF vectorizer
def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

# Main function
def mind(text):
    dataset_path = r'C:\Users\Sanjana Baragi\PycharmProjects\Voice_assistant\Data\brain_data\qna_data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    print(answer)
    return answer
while True:
    inpt = str(input())
    text=mind(inpt)
    speak(text)


# try:
#     while True:
#         x = input()
#         mind(x)
# except KeyboardInterrupt:
#     print("\n👋 Program stopped by user. Goodbye!")

