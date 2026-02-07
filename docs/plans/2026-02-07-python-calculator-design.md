# 设计文档：Python 简单加法计算器

## 1. 概述
本项目旨在实现一个高质量、可重用的 Python 库函数，用于执行两个数值的加法运算，并包含严格的类型检查和异常处理。

## 2. 核心功能
实现 `add(a, b)` 函数，要求：
- 支持 `int` 类型。
- 支持 `float` 类型（Python 中即为双精度浮点数）。
- 严格校验：若输入非数值类型，抛出 `TypeError`。

## 3. 技术栈
- **语言**: Python 3
- **测试框架**: `pytest`
- **开发模式**: 测试驱动开发 (TDD)

## 4. 架构设计
### 4.1 目录结构
```
/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── core.py       # 核心逻辑
├── tests/
│   ├── __init__.py
│   └── test_core.py      # 测试用例
└── README.md
```

### 4.2 数据流
1. 调用方调用 `add(a, b)`。
2. 内部通过 `isinstance(x, (int, float))` 检查 `a` 和 `b`。
3. 校验失败抛出 `TypeError("All inputs must be numbers (int or float).")`。
4. 校验成功返回 `a + b`。

## 5. 异常处理
- **异常类型**: `TypeError`
- **触发条件**: 任何参数不属于 `(int, float)`。

## 6. 测试用例规划
- `test_add_integers`: 验证 `add(1, 2) == 3`。
- `test_add_floats`: 验证 `add(1.1, 2.2)` 的正确性。
- `test_add_mixed`: 验证 `add(1, 2.5) == 3.5`。
- `test_add_negative`: 验证负数加法。
- `test_add_invalid_types`: 验证输入字符串或列表时抛出 `TypeError`。
