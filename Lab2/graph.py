from graphviz import Digraph

dot = Digraph(comment='Semantic Analyzer Architecture', format='pdf')
# dot_data_val = dot.getvalue()
# dot_data_val = dot_data_val.replace('helvetica', 'MicrosoftYaHei')
dot.attr(fontname='Microsoft YaHei')  # 指定全局字体

# 类型系统
dot.node('Type', 'Type\n(BASIC | ARRAY | STRUCTURE | FUNCTION)', shape='record',fontname='Microsoft YaHei')
dot.node('FieldList', 'FieldList\nname | type | tail', shape='record',fontname='Microsoft YaHei')
dot.node('Function', 'Function\nargc | argv | returnType', shape='record',fontname='Microsoft YaHei')
dot.edge('Type', 'FieldList', label='STRUCTURE.field',fontname='Microsoft YaHei')
dot.edge('Type', 'Function', label='FUNCTION',fontname='Microsoft YaHei')

# 符号表项
dot.node('TableItem', 'TableItem\nsymbolDepth | field | nextSymbol | nextHash', shape='record',fontname='Microsoft YaHei')
dot.edge('TableItem', 'FieldList', label='field',fontname='Microsoft YaHei')

# 哈希表
dot.node('HashTable', 'HashTable\nhashArray[]', shape='record',fontname='Microsoft YaHei')
dot.edge('HashTable', 'TableItem', label='-> nextHash', style='dashed',fontname='Microsoft YaHei')

# 栈结构
dot.node('Stack', 'Stack\nstackArray[] | curStackDepth', shape='record',fontname='Microsoft YaHei')
dot.edge('Stack', 'TableItem', label='-> nextSymbol', style='dashed',fontname='Microsoft YaHei')

# 整体符号表
dot.node('Table', 'Table\nhash | stack | unNamedStructNum', shape='record',fontname='Microsoft YaHei')
dot.edge('Table', 'HashTable', label='hash',fontname='Microsoft YaHei')
dot.edge('Table', 'Stack', label='stack',fontname='Microsoft YaHei')

# 表项创建与语义处理模块
dot.node('AST Traversal', 'Traversal(pNode)\n→ 语法树遍历', shape='box',fontname='Microsoft YaHei')
dot.edge('AST Traversal', 'ExtDef', label='调用',fontname='Microsoft YaHei')
dot.edge('ExtDef', 'Specifier', label='处理类型',fontname='Microsoft YaHei')
dot.edge('ExtDef', 'FunDec', label='函数定义',fontname='Microsoft YaHei')
dot.edge('FunDec', 'VarList', label='函数参数',fontname='Microsoft YaHei')
dot.edge('ExtDef', 'ExtDecList', label='变量定义',fontname='Microsoft YaHei')
dot.edge('ExtDef', 'CompSt', label='函数体',fontname='Microsoft YaHei')

# 表项相关逻辑
dot.edge('VarList', 'ParamDec',fontname='Microsoft YaHei')
dot.edge('ParamDec', 'VarDec',fontname='Microsoft YaHei')
dot.edge('CompSt', 'DefList',fontname='Microsoft YaHei')
dot.edge('DefList', 'Def',fontname='Microsoft YaHei')
dot.edge('Def', 'DecList',fontname='Microsoft YaHei')
dot.edge('DecList', 'Dec',fontname='Microsoft YaHei')
dot.edge('Dec', 'VarDec',fontname='Microsoft YaHei')
dot.edge('Dec', 'Exp', label='初值',fontname='Microsoft YaHei')

# 表项查找/插入
dot.node('searchTableItem', 'searchTableItem', shape='ellipse',fontname='Microsoft YaHei')
dot.edge('searchTableItem', 'HashTable',fontname='Microsoft YaHei')
dot.edge('ExtDef', 'addTableItem', label='插入符号',fontname='Microsoft YaHei')
dot.edge('addTableItem', 'HashTable',fontname='Microsoft YaHei')
dot.edge('addTableItem', 'Stack',fontname='Microsoft YaHei')

# 表达式处理
dot.node('Exp', 'Exp\n表达式处理', shape='box',fontname='Microsoft YaHei')
dot.edge('Exp', 'searchTableItem', label='变量查找',fontname='Microsoft YaHei')
dot.edge('Exp', 'checkType', label='类型检查',fontname='Microsoft YaHei')

# 输出图
dot.render('semantic_structure', view=True)
