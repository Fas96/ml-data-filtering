import pandas as pd


def df():
    df1 = pd.DataFrame(
        [['Dog', '12'], ['tiger', '14'], ['camiliion', '21'], ['house', '13'], ['mouse', '431'], ['cat', '21']],
        index=['0', '1', '2', '3', '4', '5' ], columns=['animal', 'age'])
    df2 = pd.DataFrame([['tiger', '14'], ['house', '13'], ['cat', '21'], ['tiger', '14'], ['house', '13'], ['a', '2']],
                       index=['0', '1', '2', '3', '4', '5'] , columns=['animal', 'age'])
    print(pd.concat([df2, df1], axis=1))
    print(pd.merge(df2, df1,how='right',on='animal'))


if __name__ == '__main__':
    df(),
