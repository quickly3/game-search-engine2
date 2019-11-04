import hashlib  # 导入加密模块
import time  # 导入时间模块

# 定义一个区类，命名为maxBlockCoin


class maxBlockCoin:
    def __init__(self, index, timestamp, data, pre_hash):
        #区块中含有index(序号), timestamp(时间戳), data(交易数据), pre_hash(前一个区块的hash), hash(当前区块的hash)
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.pre_hash = pre_hash
        self.hash = self.hash_block()

    def hash_block(self):
        string = str(self.index) + str(self.timestamp) + \
            str(self.data) + str(self.pre_hash)
        sha = hashlib.sha256()
        sha.update(string.encode("utf-8"))
        return sha.hexdigest()

# 创建第一个区块(创始区块)的方法


def create_gensis_block():
    return maxBlockCoin(0, time.time(), "first_block", "0000000")

# 创建其它区块的方法


def create_block(pre_block):
    return maxBlockCoin(pre_block.index + 1, time.time(), "line_block", pre_block.hash)


# 打印出整个区块链
pre_block = create_gensis_block()
nums = 99
print(str(pre_block.index) + "---" + str(pre_block.timestamp) + "---" + str(pre_block.data) + "---hash:" +
      pre_block.hash)

for i in range(nums):
    add_block = create_block(pre_block)
    pre_block = add_block
    print(str(pre_block.index) + "---" + str(pre_block.timestamp) + "---" + str(
        pre_block.data) + "---pre_hash:" + pre_block.pre_hash + "---hash:" +
        pre_block.hash)
