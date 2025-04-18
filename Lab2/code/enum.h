#ifndef ENUM_H
#define ENUM_H

// 标识语法树中终结符结点的类型
typedef enum _nodeType {
    TOKEN_INT,
    TOKEN_HEX,
    TOKEN_OCT,
    TOKEN_FLOAT,
    TOKEN_ID,
    TOKEN_TYPE,
    TOKEN_OTHER,
    NOT_A_TOKEN

}NodeType;

typedef enum _kind { BASIC, ARRAY, STRUCTURE, FUNCTION } Kind;
typedef enum _basicType { INT_TYPE, FLOAT_TYPE } BasicType;
typedef enum _errorType {
    UNDEF_VAR = 1,         // 未定义变量
    UNDEF_FUNC,            // 未定义函数
    REDEF_VAR,             // 重复定义的变量
    REDEF_FUNC,            // 重复定义的函数
    TYPE_MISMATCH_ASSIGN,  // 错误类型赋值
    LEFT_VAR_ASSIGN,       // 左边非变量
    TYPE_MISMATCH_OP,      // 错误类型操作
    TYPE_MISMATCH_RETURN,  // 错误类型返回
    FUNC_AGRC_MISMATCH,    // 函数变量错误
    NOT_A_ARRAY,           // 变量不是数组
    NOT_A_FUNC,            // 变量不是函数
    NOT_A_INT,             // 不是整数
    ILLEGAL_USE_DOT,       // 错误“.”用法
    NONEXISTFIELD,         // Non-existentfield
    REDEF_FEILD,           // Redefined field
    DUPLICATED_NAME,       // Duplicated name
    UNDEF_STRUCT           // Undefined structure
} ErrorType;

#endif
