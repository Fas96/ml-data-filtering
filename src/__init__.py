import pandas as pd
import matplotlib.pylab as plt


def readExcel(dir):
    df1 = pd.read_csv(dir, engine='python',encoding='cp949')
    print(df1)

def readExcelisNull(dir):
    df1 = pd.read_csv(dir, engine='python',encoding='cp949')
    print(df1.isnull())

def readExcelNotNull(dir):
    df1 = pd.read_csv(dir, engine='python',encoding='cp949')
    print(df1.notnull())
    print(df1.notnull().sum(1))

def readExcelAndDropBadData(dir):
    df1 = pd.read_csv(dir, engine='python',encoding='cp949')
    print(df1)
    #print(df1.drop(4,0))

def readExcelAndDMatplot(dir):
    df1 = pd.read_csv(dir, engine='python',encoding='cp949')
    plt.boxplot(df1['나이'])
    plt.show()
    #print(df1.drop(4,0))
if __name__ == '__main__':
    #readExcel('6장데이터/bicycle.csv')
    #readExcelisNull('6장데이터/bicycle.csv')
    #readExcelNotNull('6장데이터/bicycle.csv')
    #readExcelAndDropBadData('6장데이터/bicycle_out.csv')
    readExcelAndDMatplot('6장데이터/bicycle_out.csv')
