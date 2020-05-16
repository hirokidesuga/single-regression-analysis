# モジュール導入
import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルの読み込み
# df = date frame
df = pd.read_csv('original.csv')

# データの中心化
df_c = df - df.mean()

# 成分抽出
xc = df_c['x']  # 中心化済みx
yc = df_c['y']  # 中心化済みy

# 予想直線 y_hat = a * x
# aを求める公式：a(傾き) = (xc * yc)の総和 / xc**2の総和
xx = xc ** 2
xy = xc * yc
a = xy.sum() / xx.sum()


#中心化解除
y_hat = a * xc + df.mean()['y']


# data frame表示関数
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
    plt.plot(df['x'], y_hat, label="y_hat", color="red")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
