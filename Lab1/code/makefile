

CC = gcc
FLEX = flex
BISON = bison
CFLAGS = -std=c99

# conda install -c conda-forge flex 
# conda install -c conda-forge bison

CFILES = $(shell find ./ -name "*.c")
OBJS = $(CFILES:.c=.o)
LFILE = $(shell find ./ -name "*.l")
YFILE = $(shell find ./ -name "*.y")
LFC = $(shell find ./ -name "*.l" | sed s/[^/]*\\.l/lex.yy.c/)
YFC = $(shell find ./ -name "*.y" | sed s/[^/]*\\.y/syntax.tab.c/)
LFO = $(LFC:.c=.o)
YFO = $(YFC:.c=.o)

parser: syntax $(filter-out $(LFO),$(OBJS))
	$(CC) -o parser $(filter-out $(LFO),$(OBJS)) 

syntax: lexical syntax-c
	$(CC) -c $(YFC) -o $(YFO)

lexical: $(LFILE)
	$(FLEX) -o $(LFC) $(LFILE)

syntax-c: $(YFILE)
	$(BISON) -o $(YFC) -d -v $(YFILE)

-include $(patsubst %.o, %.d, $(OBJS))

.PHONY: clean test
# 定义测试文件列表
TEST_FILES = $(wildcard ../test/test*.cmm)

# 定义测试目标模式规则
test_%: ../test/test%.cmm
	./parser $<

test_all:
	./parser ../test/test1.cmm
	./parser ../test/test2.cmm
	./parser ../test/test3.cmm
	./parser ../test/test4.cmm
	./parser ../test/test5.cmm
	./parser ../test/test6.cmm
	./parser ../test/test7.cmm
	./parser ../test/test8.cmm
	./parser ../test/test9.cmm
	./parser ../test/test10.cmm
clean:
	rm -f parser lex.yy.c syntax.tab.c syntax.tab.h syntax.output
	rm -f $(OBJS) $(OBJS:.o=.d)
	rm -f $(LFC) $(YFC) $(YFC:.c=.h)
	rm -f *~
