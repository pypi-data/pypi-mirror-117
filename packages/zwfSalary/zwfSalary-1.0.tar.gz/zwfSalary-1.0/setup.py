# coding=utf-8
from distutils.core import setup
setup(
    name='zwfSalary',   #对外发布我的模块的名称
    version='1.0',    #版本号
    description='这是我第一个对外发布的模块，用于测试呀',  #描述
    author="zhengwf",   #作者
    author_email='1245172534@qq.com',
    py_modules=['zwfSalary.mysalary']   #要发布的模块，可以多个
)