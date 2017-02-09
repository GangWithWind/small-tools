# small-tools
一些python和shell的小工具  

## pmake.py:
使用python的简单c++编译工具
* 首次运行时使用类似如下的命令，生成pMakefile，并且编译链接   
`pmake.py *.cc res`或  
`pmake.py a.cc b.cc res`
* 一般编译时使用 pmake.py
* 使用`pmake.py clean` 清空.o文件
* 使用`pmake.py add a.cc b.cc`添加新的文件进入pMakefile并编译。
* 可以写一个alias，方便使用  
`alias pmake = 'python /Users/gangzhao/GitHub/small-tools/pmake.py`
