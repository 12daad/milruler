# Milruler
这是一个在 Battlefield 2042 中用于辅助计算密位的工具，目前支持的武器搭配在`conf.json`中列出 

# 使用
install requirements 

```
pip install -r requirements.txt
```
run 
```
python .\src\main.py
```
在游戏中，请通过键盘`up, down, left, right`或鼠标滚轮调整密位位置（为了不影响游戏操作，请在游戏设置中关闭这些按键）

# 用前请看
在射击距离为$L$的物体时，需要将枪口抬高$n$个密位，$n$与$L$的关系大概为线性的
$$
y = {\rm dist\_per\_mil}\cdot n
$$
${\rm dist\_per\_mil}$也就是`.src.util.WeaponAccessory.pixel_per_mil`所定义的，$k$的数值与武器搭配有关，例如
```json
[
    {
        "weapon": "DXR-1", 
        "barrel": "长枪管", 
        "ammo": "高威力", 
        "scope": "X12", 
        "dist_per_mil": 560, 
        "pixel_per_mil": 100.0
    }
]
```
此外我们还需要知道每个密位对于屏幕上像素的个数`pixel_per_mil`，在使用时请替换成你的配置

