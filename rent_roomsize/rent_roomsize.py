# モジュール導入
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
# df = date frame
df = pd.read_csv('original.csv')

# データの中心化
df_c = df - df.mean()

# 成分抽出
xc = df_c['x']
yc = df_c['y']

# 公式代入
xx = xc ** 2
xy = xc * yc
a = xy.sum() / xx.sum()
y = a * xc + df.mean()['y']


# data frame表示
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')


def main():
    # データフレーム表示
    print_full(df.describe())

    # 中心化済みデータフレーム表示
    print_full(df_c.describe())

    # 中心化した　実際の値の分散と予想直線の描写
    plt.scatter(df['x'], df['y'], label="y")
    plt.plot(df['x'], y, label="y_hat", color="red")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
