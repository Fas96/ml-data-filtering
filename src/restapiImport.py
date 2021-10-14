import  pandas as pd
import  seaborn as sns

def seaborAPi():
    tips=sns.load_dataset('tips')
    print(tips.head())
    print(tips.head().drop([2]))

    print(tips.loc[0])



if __name__ == '__main__':
    seaborAPi()
