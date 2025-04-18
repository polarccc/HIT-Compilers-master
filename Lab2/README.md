# Lab2

### 文件目录：

* code: 程序源文件
* test: 必做以及选做的全部23个测试用例(.txt文件)
* txt: 错误类型说明

### 使用方法：

* 编译：

  ```
  make //在code目录下使用make命令进行编译
  ```

* 测试：

  ```
  make test_1
  make test_2
  ...
  make test_all //在code目录下使用make test命令进行测试 即./parser ../test/1.txt
  make test_extra
  ```

* 其他

  ```
  make clean //在code目录下使用make clean命令清除中间文件
  ```

### 说明与改进：
* 本实验所需的包是通过 conda install 安装，而非 apt install，所以编译时取消了 -lfl 链接 
* 同时，为解决指针删除异常导致内存泄露的问题，在sematic.c增加了删除保护机制