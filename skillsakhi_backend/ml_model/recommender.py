import os
import pickle
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'ml_model' / 'career_model.pkl'


def rule_based_careers(profile):
    interests = [i.strip().lower() for i in profile.interests.split(',')]
    rules = {
        'cooking': ['Home Caterer', 'Food Blogger', 'Cloud Kitchen Assistant'],
        'teaching': ['Online Tutor', 'Pre-school Teacher'],
        'design': ['Graphic Designer', 'UI Designer'],
        'analysis': ['Data Analyst'],
    }
    suggestions = []
    for interest in interests:
        suggestions.extend(rules.get(interest, []))
    return list(dict.fromkeys(suggestions))


def load_model():
    if not MODEL_PATH.exists():
        return None
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)


def recommend_by_model(profile):
    model = load_model()
    if not model:
        return None
    input_df = pd.DataFrame([
        {
            'age': profile.age,
            'education': profile.education_level,
            'interests': profile.interests,
            'work_preference': profile.work_preference,
        }
    ])
    pred = model.predict(input_df)[0]
    probs = None
    if hasattr(model, 'predict_proba'):
        probs = float(np.max(model.predict_proba(input_df)))
    return pred, probs or 0.7
