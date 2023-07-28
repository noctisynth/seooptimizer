# SEO Optimizer
搜索引擎优化是每一个网站初期都要头疼的事情. 尤其百度作为中国国内使用人数最多的搜索引擎的情况下, 毕竟百度的确是一个十分优秀的广告公司(bushi), 除非你付费将你的网站作为广告投放, 或者你的网站访问量惊人, 否则明明你的关键词唯一, 你的主页甚至都只能在第三页找到.

所以我们开发了 SEO Optimizer, 它旨在自动化控制你的浏览器点击和你相关的关键词, 借此来提高你的网站搜索指数.

最新版本的 SEO Optimizer 清理掉了古老而过时的 selenium, 毕竟它的算法令人痛苦, 我们采用了 [DrissionPage](https://gitee.com/g1879/DrissionPage) 作为自动化控制的基础.

同时, 你不再需要下载对应版本的`chromedriver`.

## 配置
安装最新版本的 Google Chrome (谷歌浏览器)，如果你已经安装了 Google Chrome, 请跳过此步骤。

[谷歌官方主页](https://www.google.cn/chrome/)下载, 下载速度与网络环境有关.

## 安装 SEO Optimizer
使用`pip`安装:
```
pip install seooptimizer
```

你也可以直接从仓库下载源代码, 或者使用 Git:
```sh
git clone https://gitee.com/unvisitor/seooptimizer.git
cd seooptimizer
python3 setup.py install
```
值得注意的是, 在 Windows 中你应该使用`python setup.py install`, 它不存在`python3`命令.

## 使用
创建一个 Python 脚本, 你可以命名为`demo.py`:
```python
from seooptimizer.main import run

def main(keyword, loop=False):
    while True:
        if run(keyword, wait=5.5, turn_wait=2, depth=3) and not loop:
            break

if __name__ == "__main__":
    main("未知访客", loop=True)
```

将`"未知访客"`替换为你想要进行 SEO 优化的关键词.

## 版权
Copyright © 2011-2023 Unknown Visitor. All rights reserved.