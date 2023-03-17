
#ananconda详细网址
https://blog.csdn.net/lrx6666666/article/details/120539731

#anaconda创建python版本
conda create -n XXX(名称mytest) python=3.6
#查看各个python版本
conda env list
#使用某个版本
conda activate mytest

#如果使用国内镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

#安装源
pip install （安装包名称） -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
豆瓣(douban) http://pypi.douban.com/simple/ 
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/



pip install opencv-contrib-python -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com


conda create -n fzp3.8 python=3.8