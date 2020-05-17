# 単回帰分析
## rent_roomsize(部屋の広さを元に家賃を推測する)
original.csv：教師データ（データ数：100）
| x  |  y  |
| ---- | ---- |
|  部屋の広さ(単位：平米)  |  家賃(単位：円)  |

rent_roomsize.py：同一階層上の教師データ（original.csv）を学習させて、その詳細を出力するプログラム

answer_rent_by_roomsize：学習済みのrent_roomsize.pyを元に、部屋のサイズ（標準入力x）から予測した家賃(y_hat)を出力するプログラム
