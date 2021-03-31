def stringOfPermutation(str):
    """
    输出一个字符串的全排列
    例如输入 'abc'
    输出： 'abc','acb','bac','bca','cab','cba'
    输出总个数为 字符串长度的阶乘 len(str)!

    思路1、递归法

    :param str:
    :return:
    """
    # 递归法
    """
    递归终止条件：
    长度唯一的字符串的全排序就是自身
    """
    if len(str) <= 1:
        return str

    # 结果，直接用set做去重
    res = set()

    """
    递归条件
    1、i 从 0 开始遍历整个str的各个字母str[i]
    2、每次都递归得到一个除自身外所有字母的全排序
    3、将字母str[i]+ 得到的其他所有全排序
    """
    for i in range(len(str)):
        # 每一个 one_case 是 Permutation(ss[:i]+ss[i+1:]) 这个list中不同排列组合的一种case
        all_case = stringOfPermutation(str[:i] + str[i + 1:])
        for one_case in all_case:
            res.add(str[i] + one_case)
    return list(res)

if __name__ == '__main__':
    rs =  stringOfPermutation("abcd")
    print(rs)
   # str = 'abcd'
   # i = 0
   # print(str[:i]) 
   # print(str[i + 1:])