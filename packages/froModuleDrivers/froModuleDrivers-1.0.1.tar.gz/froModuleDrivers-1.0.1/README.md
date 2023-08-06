# 目录结构及说明


```
.
├── examples
|   └── xxx.py
├── froModuleDrivers
|   └── xxx.py
├── setup.py
└── README.md

```



### examples

提供了每个硬件驱动基础的测试例子

更多控制方法请参考每个硬件驱动的api文档



### froModuleDrivers

驱动文件夹，请勿随意修改



### setup.py

安装驱动到PC，安装完之后可以在任意目录来引用 from froModuleDrivers import xxx

##### 安装方法为：

在froModuleDrivers同目录下打开命令行，运行指令：pip install .

```python
pip install .
```

联网状态可以直接运行:pip install froModuleDrivers
```python
pip install froModuleDrivers
```