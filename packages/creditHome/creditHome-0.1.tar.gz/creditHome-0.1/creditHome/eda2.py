################################################
## Tuğrul ve Burak kullandığı fonksiyonlar
################################################



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 170)


def control_df(df):
    print("Verinin boyutları:")
    print(df.shape)
    print("###############################################################")
    print("Verideki değişkenlerin boş değer oranı:")
    rate_null_columns = {}
    for col in df.columns:
        rate_null_columns[col] = df[col].isnull().sum() / len(train)
    print(pd.Series(rate_null_columns))
    print("###############################################################")
    return rate_null_columns


def grab_cat_num(df, cat=10):
    cat_cols = [col for col in df.columns if df[col].dtype == "O"]
    num_but_cat_cols = [col for col in df.columns if df[col].nunique() < cat and df[col].dtype != "O"]
    cat_but_num_cols = [col for col in df.columns if df[col].nunique() > 20 and df[col].dtype == "O"]
    cat_cols = cat_cols + num_but_cat_cols
    num_cols = [col for col in df.columns if col not in cat_cols]
    return cat_cols, num_cols


def num_analysis(df, col_name):
    print("#" * 25 + " " + f"{col_name.upper()}" + " " + "#" * 25)
    print(df[col_name].describe([0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]).T)


def cat_analysis(df, col_name, info=True):
    print(f"{col_name.capitalize()} adlı değişkenin gözlemlerinin yüzdesel oranı:")
    ratio = (df[col_name].value_counts() / len(df) * 100)
    print(f"{ratio}")
    if info:
        print("info".center(50, "#"))
        print(df.groupby(col_name).mean())
        print("\n\n")


def gg(df, target):
    col_names = [col for col in df.columns if col not in ["charges", "age", "bmi"]]
    # col_names=df.columns[~df.columns.str.contains("charges")]
    print(col_names)
    for col in col_names:
        ss = df.groupby(col)[target].mean()
        plt.ylabel(target)
        plt.title(f"{col} adlı değişken kırılımında ortalama")
        plt.legend()
        # sns.set(rc={'figure.figsize': (8, 10)})
        sns.barplot(x=ss.index, y=ss.values)
        plt.show()
        print("\n")
        print(ss)
        print("######################\n\n")

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()
    print("##########################################")


def one_hot_encoder(dataframe, categorical_cols, drop_first=False):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe


def grab_col_names(dataframe, cat_th=10, car_th=20):
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car



