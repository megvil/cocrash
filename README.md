# cocrash

#### 项目介绍
breakpad的运行脚本，可自动把崩溃文件dmp给转换成具体错误信息的txt文件

注意，该脚本仅能运行在64位的linux机器上。

#### 结构说明

`dmp`  存放崩溃原始文件的目录

`house`  存放生成的临时文件

`libso`  存放编译的动态链接库 .so文件和经过处理后的.so.sym文件

`output` 存放编译加工后的崩溃文件，包含具体的错误信息

`tool`  存放以上所有操作的工具

`dumpsym.sh`  该脚本是把libso/.so的文件编译为.so.sym文件，并存放在libso下面

`dumptxt.sh`  该脚本是把 dmp文件夹下的 .dmp 崩溃原始文件  和 libso/.so.sym 文件一起，解析为可读的 txt错误信息文件

`crashbuild.py`  该脚本是精准定位到错误的cpp行数，把解析后的错误信息和txt文件一起给合并成一个新的可读错误信息文件

`build.sh`  该脚本是自动化脚本，一次运行上面所有步骤的命令，只需要把原始文件放到dmp目录下，即可在output目录下获取最终的错误信息日志

#### 使用说明

1、把app生成的崩溃文件.dmp 放到 /dmp 目录

2、然后在根目录下直接执行 ./build.sh 脚本

3、然后在 /output 目录下面取相应的结果即可



