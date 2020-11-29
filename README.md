# HolePlateMaker
穴を等間隔に開けた工作用プレートの3Dデータ(STLファイル)を自作できるライブラリです。
作成したSTLはお好みの３Dプリンタで出力してください。
(現状では[Da vinci nano w](https://www.xyzprinting.com/ja-JP/product/da-vinci-nano-w)で出力できることを確認しています。)

# How to use
先に以下のpythonパッケージをインストールしてください。

```shell:install
pip3 install numpy
pip3 install numpy-stl
pip3 install matplotlib
```

本githubを使いたいフォルダへcloneしてからご使用ください。
現時点ではbool型の値が入ったnumpy配列からプレートのメッシュを作成することができます。

```python:example
import numpy as np
from stl import mesh
from HolePlateMaker.NumpyArrayToPlate import NumpyBoolArrayToPlate

plateData = np.array([[True,False,True],
    [True,False,True],
    [True,True,True,],
    [False,False,True],
    [False,False,True],])

curMesh = NumpyBoolArrayToPlate(plateData)
curMesh.save('plate.stl')
```

出力される結果は、下記の写真のようにnumpy配列の[0][0]を原点0,0に揃え、行方向、列方向に沿ってプレートの穴部分を追加していきます。


<img width="600" alt="ユニバーサルプレートもどきの出力結果" src="https://github.com/henjin0/HolePlateMaker/blob/main/NumpyArrayToMesh.png">



Please see [LICENSE](https://github.com/henjin0/HolePlateMaker/blob/main/LICENSE).
