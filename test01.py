def validate_contract(x,z,total,cores,tile):
    '''
    定义的校验函数:进行/切片计算前,确保输入的所有参数符合标准预期
    x(list)= 输入的数据列表x
    z(list)= 输入的数据列表z
    total(int)= 声明的数据总长度(必须和x和z的长度相匹配)
    cores(int)= 声明的计算核心数(必须为正整数)
    tile(int)= 声明的切片大小(必须为正整数)
    '''
    # 1.校验数据类型
    # 目的,确保x和z是列表结构
    if not isinstance(x,list) or not isinstance(z,list):
        # 如果x和z不是列表,则抛出异常
        raise TypeError("输入的x和z必须是列表类型")

    # 2.校验列表长对齐
    # 目的,确保x和z的长度与total一致
    if len(x) != len(z):
        # 如果x和z的长度不一致,则抛出异常
        raise ValueError("输入的x和z长度不一致")
    # 3.校验计算资源和切片的合法性
    # 目的,确保cores和tile是正整数
    if cores <= 0 or tile <= 0:
        # 如果cores或tile不是正整数,则抛出异常
        raise ValueError("计算核心数和切片大小必须为正整数")

    # 4.校验实际数据和声明总数保持一致
    # 目的,确保x和z的长度与total一致
    if len(x) != total or len(z) != total:
        # 如果x和z的长度与total不一致,则抛出异常
        raise ValueError("输入的x和z长度与声明的总长度不一致")

print("测试1,传入正确的参数")
# 列表x有两个元素,列表z有两个元素,声明的总长度为2,计算核心数为2,切片大小为1
validate_contract(x=[1.0,2.0], z=[3.0,4.0], total=2, cores=2, tile=1)
print("测试1通过,没有抛出异常")

print("测试2,传入错误的参数")
# 输入一个x列表和一个z列表,但是x和z的长度不一致,声明的总长度为2,计算核心数为2,切片大小为1
try:
    validate_contract(x=[1.0,2.0], z=[3.0], total=2, cores=2, tile=1)
except ValueError as e:
    print("测试2通过,捕获到异常:", e)

print("测试3,传入错误的参数")
# 输入一tile=0,这是一个非法的切片大小,声明的总长度为2,计算核心数为2
try:
    validate_contract(x=[1.0,2.0], z=[3.0,4.0], total=2, cores=2, tile=0)
except ValueError as e:
    print("测试3通过,捕获到异常:", e)