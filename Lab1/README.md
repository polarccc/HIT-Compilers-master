# 编译原理实验1 

## 在https://github.com/wyd010616/HIT-Compilers 基础上修改

### 文件目录：

* code: 程序源文件
* test: 必做以及附加功能的全部10个测试用例(.cmm文件)

### 使用方法：

* 编译：

  ```
  make //在code目录下使用make命令进行编译
  ```

* 测试：

  ```
  make test_all   //在code目录下使用make test命令对全部用例进行测试
  make test_[num] //在code目录下使用make test命令对第[num]个进行测试  
  即./parser ../test/test.cmm
  ```

* 其他

  ```
  make clean //在code目录下使用make clean命令清除中间文件
  ```

* 还存在的问题：对于空行，无";"的情况还存在不能正确识别行号的问题

附：C--语言文法：
![alt text](C--文法.png)