# 必要な変数を対応ファイルから読み込み
from rent_roomsize import a, df


# 部屋の広さxを標準入力し、家賃y_hatを返す関数
def predict(x):
    y_hat = a * (x - df.mean()['x']) + df.mean()['y']
    return y_hat


def main():
    print("部屋の広さxから家賃を予測できます(30 <= x <= 50, 単位：平米)")
    room_size_input = float(input("広さを入力してください："))
    output_input_is_not_correct = "\n30以上50以下の数字を入力してください"
    while not 30 <= room_size_input <= 50:
        print(output_input_is_not_correct)
        room_size_input = float(input("広さを入力してください："))
    output = "広さ" + str(room_size_input) + "平米のお部屋の家賃はおおよそ" + str(predict(room_size_input)) + "円です"
    print(output)


if __name__ == "__main__":
    main()
