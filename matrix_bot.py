from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator
from sklearn.pipeline import make_pipeline
import numpy as np
import postgre_bot as pb

# Векторизируем вопросы в огромную матрицу
# Перемножив фразы на слова из которых они состоят получим числовые значения
vectorizer_q = TfidfVectorizer()  # создаем объект, который будет преобразовать коротки слова в числовые веторы
vectorizer_q.fit(pb.questions)  # запоминаем частоту каждого слова

matrix_big_q = vectorizer_q.transform(pb.questions)  # записываем в матрицу сколько раз встречалось каждое слово

# print('Размер матрицы: ')
# print(matrix_big_q.shape)

# сокращение матрицы
if pb.transform > 200:
    pb.transform = 200

svd_q = TruncatedSVD(n_components=pb.transform)
svd_q.fit(matrix_big_q)

matrix_small_q = svd_q.transform(matrix_big_q)


# тело программы поиска ответов
def softmax(x):
    # создание вероятности распределения
    proba = np.exp(-x)
    return proba / sum(proba)


# класс для случайного выбора одного из ближайших соседей
class NeighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature=10.0):
        self.k = k
        self.temperature = temperature

    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)

    def predict(self, X, random_state=None):
        distances, indices = self.tree_.query(X, return_distance=True)
        result = []
        for distance, index in zip(distances, indices):
            result.append(np.random.choice(index, p=softmax(distance * self.temperature)))
        return self.y_[result]


ns_q = NeighborSampler()

# link_c_id - код ответа в массиве
ns_q.fit(matrix_small_q, pb.link_c_id)
pipe_q = make_pipeline(vectorizer_q, svd_q, ns_q)
