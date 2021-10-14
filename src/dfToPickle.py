import pickle
import pandas as pd


def dftoPickle():
    tmp = pd.DataFrame({'a': [1], 'b': [2]})
    tmp.to_pickle('6장데이터/pk.pkl')
    data = pd.read_pickle('6장데이터/pk.pkl')
    print(data)


if __name__ == '__main__':
    dftoPickle()
