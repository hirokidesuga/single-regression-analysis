from rent_roomsize import a, df


def predict(x):
    y_hat = a * (x - df.mean()['x']) + df.mean()['y']
    return y_hat


print("部屋の広さxから家賃を予測できます(30 <= x <= 50, 単位：平米)")
room_size_input = int(input("広さ："))
output = "広さ" + str(room_size_input) + "平米のお部屋の家賃はおおよそ" + str(predict(room_size_input)) + "円です"
print(output)
