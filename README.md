# small-tools
一些python和shell的小工具  

## pmake.py:
使用python的简单c++编译工具
* 首次运行时使用类似如下的命令，生成pMakefile，并且编译链接   
`pmake.py *.cc res` 或 `pmake.py a.cc b.cc res`
* 一般编译时使用 pmake.py
* 使用`pmake.py clean` 清空.o文件
* 使用`pmake.py add a.cc b.cc`添加新的文件进入pMakefile并编译。
* 可以写一个alias，方便使用  
`alias pmake = 'python /Users/gangzhao/GitHub/small-tools/pmake.py`

## collectidea (废弃，不支持新版本的Jupyter)
Jupyter插件。我们平时总是遇到一些有价值的想法或者有趣的经验希望保存下来。collectidea提供了一种备选方法。在Jupyter notebook中新建一个或者数个cell，输入想要保存的想法。点击博士帽或者信封，可以将选中的单元格保存到knowledge.ipynb 和 inputbox.ipynb中。

安装方法：将文件夹拷贝到 /Users/gangzhao/anaconda3/share/jupyter/nbextensions中。需要nbextension支持。

## netconnect
当NIAOT网络中断时，自动登录连接
每次开机后运行run2.sh
运行日志查看log文件