# Rust 契约校验函数设计文档

## 1. 目标

将 Python 版本的 `validate_contract` 函数转译为 Rust，保持功能一致，使用 `Result<T, E>` 进行错误处理。

## 2. 原始 Python 代码分析

```python
def validate_contract(x, z, total, cores, tile):
    # 校验数据类型
    if not isinstance(x, list) or not isinstance(z, list):
        raise TypeError("输入的x和z必须是列表类型")
    # 校验列表长度对齐
    if len(x) != len(z):
        raise ValueError("输入的x和z长度不一致")
    # 校验计算资源和切片的合法性
    if cores <= 0 or tile <= 0:
        raise ValueError("计算核心数和切片大小必须为正整数")
    # 校验实际数据和声明总数保持一致
    if len(x) != total or len(z) != total:
        raise ValueError("输入的x和z长度与声明的总长度不一致")
```

## 3. Rust 实现方案

### 3.1 函数签名

```rust
pub fn validate_contract(
    x: &[f64],
    z: &[f64],
    total: usize,
    cores: i32,
    tile: i32,
) -> Result<(), ValidationError>
```

### 3.2 错误类型定义

```rust
#[derive(Debug, Clone)]
pub enum ValidationError {
    TypeMismatch(String),
    LengthMismatch(String),
    InvalidResource(String),
    TotalMismatch(String),
}
```

### 3.3 校验逻辑

1. 类型校验 - Rust 中由编译器保证，运行时无需检查
2. 长度一致性 - `x.len() == z.len()`
3. 资源合法性 - `cores > 0 && tile > 0`
4. 总数一致性 - `x.len() == total && z.len() == total`

### 3.4 错误信息

保持与 Python 版本一致的中文错误信息。

## 4. 文件结构

```
src/
├── lib.rs          # 库入口
├── validator.rs    # 校验函数实现
└── error.rs        # 错误类型定义
```

## 5. 测试

提供与 Python 版本一致的单元测试。

## 6. 使用示例

```rust
use validator::validate_contract;

fn main() {
    let x = vec![1.0, 2.0];
    let z = vec![3.0, 4.0];
    
    match validate_contract(&x, &z, 2, 2, 1) {
        Ok(()) => println!("校验通过"),
        Err(e) => println!("校验失败: {:?}", e),
    }
}
```
