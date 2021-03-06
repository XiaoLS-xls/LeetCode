class Solution:
    def climbStairs(self, n):
        def flower(n):
            if n == 0:                  #出口
                return 1
            elif n < 0:
                return 0
            return flower(n-1)+flower(n-2)           #左右的和（可以通过话递归树，找到当前状态到下一个状态的关系）


    def climbStairs2(self,n):                  #改进方法（改进不大，还是很大，很多重复运算） n=1:一种    n=2:两种
        def flower(n):                          #f(n) = f(n-1)+f(n-2)    (从n-1上来的一种，和n-2的一种)
            if n == 1:          # 出口
                return 1
            elif n == 2:
                return 2
            return flower(n - 1) + flower(n - 2)
        return flower(n)

    def climbStairs3(self,n):             #由于前两次的递归很多的重复计算，可以采用动态规划法
        if n == 1:
            return 1
        list1 = [0]*n
        list1[0]=1;list1[2]=2
        for i in range(1,n):
            list1[i] = list1[i-1] + list1[i-2]
        return list1[n-1]
                                            #这个推倒公式与斐波那契数列一样，就也可以通过矩阵来求

方法三：通项公式
思路：
f(n) 是齐次线性递推，根据递推方程 f(n) = f(n - 1) + f(n - 2)，我们可以写出这样的特征方程：x*x = x + 1
方程的解为： f(n) = c1 * x1^n + c2 * x2^n         根据f（1）=1，f（2）=2，再求得c1和c2

链接：https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
