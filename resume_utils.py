import spacy
from keybert import KeyBERT

nlp = spacy.load("en_core_web_sm")
kw_model = KeyBERT()

def extract_keywords(text, top_n=10):
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]

def clean_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    return round(similarity[0][0] * 100, 2)

def find_missing_keywords(resume_keywords, jd_keywords):
    return list(set(jd_keywords) - set(resume_keywords))
