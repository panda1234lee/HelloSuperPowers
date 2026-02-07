# Python Calculator Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a robust `add(a, b)` function in Python with strict type checking and TDD.

**Architecture:** A simple Python package structure with a core module and a corresponding test suite.

**Tech Stack:** Python 3, Pytest.

---

### Task 1: Project Structure and Setup

**Files:**
- Create: `src/calculator/__init__.py`
- Create: `src/calculator/core.py`
- Create: `tests/__init__.py`
- Create: `tests/test_core.py`

**Step 1: Create directories and empty files**
Run: `mkdir -p src/calculator tests && touch src/calculator/__init__.py src/calculator/core.py tests/__init__.py tests/test_core.py` (Windows equivalent using PowerShell: `New-Item -ItemType Directory -Force src/calculator, tests; New-Item -ItemType File -Force src/calculator/__init__.py, src/calculator/core.py, tests/__init__.py, tests/test_core.py`)

**Step 2: Commit initial structure**
```bash
git add .
git commit -m "chore: 初始化项目结构"
```

---

### Task 2: Integer Addition (TDD)

**Files:**
- Modify: `src/calculator/core.py`
- Modify: `tests/test_core.py`

**Step 1: Write failing test for integer addition**
Add to `tests/test_core.py`:
```python
from calculator.core import add

def test_add_integers():
    assert add(1, 2) == 3
```

**Step 2: Run test to verify it fails**
Run: `pytest tests/test_core.py` (Expected: Import error or NameError)

**Step 3: Write minimal implementation**
Add to `src/calculator/core.py`:
```python
def add(a, b):
    return a + b
```

**Step 4: Run test to verify it passes**
Run: `pytest tests/test_core.py`
Expected: PASS

**Step 5: Commit**
```bash
git add src/calculator/core.py tests/test_core.py
git commit -m "feat: 实现基础整数加法"
```

---

### Task 3: Float Addition and Mixed Types (TDD)

**Files:**
- Modify: `tests/test_core.py`

**Step 1: Write failing tests for floats**
Add to `tests/test_core.py`:
```python
def test_add_floats():
    # 使用 pytest.approx 处理浮点数精度问题
    import pytest
    assert add(1.1, 2.2) == pytest.approx(3.3)

def test_add_mixed_types():
    assert add(1, 2.5) == 3.5
```

**Step 2: Run test to verify it fails/passes**
(Since Python's `+` already handles this, it might pass immediately. If so, we acknowledge and ensure types are checked in the next task).
Run: `pytest tests/test_core.py`

**Step 3: Commit**
```bash
git add tests/test_core.py
git commit -m "test: 增加浮点数和混合类型测试"
```

---

### Task 4: Strict Type Checking (TDD)

**Files:**
- Modify: `src/calculator/core.py`
- Modify: `tests/test_core.py`

**Step 1: Write failing test for invalid types**
Add to `tests/test_core.py`:
```python
import pytest

def test_add_invalid_types():
    with pytest.raises(TypeError, match="All inputs must be numbers"):
        add("1", 2)
    with pytest.raises(TypeError, match="All inputs must be numbers"):
        add(1, [2])
```

**Step 2: Run test to verify it fails**
Run: `pytest tests/test_core.py`
Expected: FAIL (It will likely perform string concatenation or raise a different TypeError)

**Step 3: Implement strict type checking**
Modify `src/calculator/core.py`:
```python
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("All inputs must be numbers (int or float).")
    return a + b
```

**Step 4: Run test to verify it passes**
Run: `pytest tests/test_core.py`
Expected: PASS

**Step 5: Commit**
```bash
git add src/calculator/core.py tests/test_core.py
git commit -m "feat: 增加严格类型检查"
```
