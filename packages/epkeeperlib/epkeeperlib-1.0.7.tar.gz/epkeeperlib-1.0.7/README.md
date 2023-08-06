
电管家通用功能包
---


###打包过程：
安装更新setuptools、wheel、twine
```shell
python -m pip install --upgrade setuptools wheel twine
```
打包
```shell
python setup.py sdist bdist_wheel
```
上传pypi.org
```shell
twine upload dist/*
```
安装包
```shell
pip install -i https://pypi.org/project epkeeperlib
```
更新包
```shell
pip install -i https://pypi.org/project --upgrade epkeeperlib
```

