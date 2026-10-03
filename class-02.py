import sys
from typing import List,NamedTuple
import numpy as np

# GM 片外显存
# LM 片上显存
# Tiling 
# Alignment 内存对齐
# Padding 当数据不满足对齐要求时，填充一些无用数据，使得数据满足对齐要求

#定义一个名为TileRecord的类,用于继承NameTuple(类似于C++中的struct),用于存储tile的相关信息
class TileRecord(NamedTuple):
    start:int  # tile的起始位置
    valid:int  # tile中有效数据的长度
    physical:int  # tile中物理数据的长度(包含填充数据)

# 定义一个函数 calculate_tile_info,用于计算tile的相关信息
def calculate_tile_info(
        #当前分块的序号(第0个,第一个...)
        tile_idx : int,
        #
        total_N: int,
        tile_size: int,
        align_granularity: int
)-> TileRecord:
    '''
    计算tile的相关信息
    tile_idx: 当前分块的序号(第0个,第一个...)
    total_N: 总数据长度
    tile_size: 每个tile的大小
    align_granularity: 对齐粒度
    '''
    # 计算当前tile的起始位置
    start = tile_idx * tile_size 
    if start >= total_N:
        # 如果起始位置大于等于总数据长度,则抛出异常
        raise TileRecord(start=start, valid=0, physical=0)

    valid = min(tile_size, total_N - start) 
    physical = ((valid + align_granularity - 1) // align_granularity) * align_granularity

    return TileRecord(start=start, valid=valid, physical=physical)

def fast_gelu_np(x: np.ndarray) -> np.ndarray:
    '''
    使用numpy实现快速GELU激活函数
    x: 输入的numpy数组
    返回: 输出的numpy数组
    '''
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))
