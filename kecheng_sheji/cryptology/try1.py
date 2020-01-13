import random

# 选择素域，设置椭圆曲线参数
sm2_N = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFF7203DF6B21C6052B53BBF40939D54123', 16)
sm2_P = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFF', 16)
sm2_G = '32c4ae2c1f1981195f9904466a39c9948fe30bbff2660be1715a4589334c74c7bc3736a2f4f6779c59bdcee36b692153d0a9877cc62a474002df32e52139f0a0'  # G点
sm2_a = int('FFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFFFFFC',16)
sm2_b = int('28E9FA9E9D9F5E344D5A9E4BCF6509A7F39789F515AB8F92DDBCBD414D940E93',16)
sm2_a_3 = (sm2_a + 3) % sm2_P # 倍点用到的中间值
Fp = 256

def randomStr(len):#过得随机
    s = ''
    for i in range(len):
        a = hex(random.randint(0,16))
        s += str(a)[2]
    return s

if __name__ == '__main__':
    print(randomStr(10))
