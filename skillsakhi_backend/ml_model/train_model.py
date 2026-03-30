import pickle
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / 'data' / 'career_dataset.csv'
MODEL_PATH = BASE_DIR / 'ml_model' / 'career_model.pkl'


def train():
    df = pd.read_csv(DATA_PATH)
    X = df[['age', 'education', 'interests', 'work_preference']]
    y = df['career']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['education', 'interests', 'work_preference']),
        ],
        remainder='passthrough',
    )

    model = Pipeline(
        steps=[
            ('prep', preprocessor),
            ('clf', KNeighborsClassifier(n_neighbors=3)),
        ]
    )

    model.fit(X, y)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)


if __name__ == '__main__':
    train()
    print(f'Model saved to {MODEL_PATH}')
