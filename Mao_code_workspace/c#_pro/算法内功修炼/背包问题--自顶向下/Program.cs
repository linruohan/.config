using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 背包问题__自顶向下
{
    class Program
    {
        static void Main(string[] args)
        {

            int m; // 包的重量
            int[] w = { 0, 3, 4, 5 };//每个物品的重量
            int[] p = { 0, 4, 5, 6 };//每个物品的价值

            Console.WriteLine(UpDown(10, 3, w, p));
            Console.WriteLine(UpDown(3, 3, w, p));
            Console.WriteLine(UpDown(4, 3, w, p));
            Console.WriteLine(UpDown(5, 3, w, p));
            Console.WriteLine(UpDown(7, 3, w, p));
            Console.WriteLine(UpDown(8, 3, w, p));

            Console.ReadKey();


        }
        // m 背包容量,i是物品个数,wp是重量和价值的数组
        public static int UpDown(int m, int i, int[] w, int[] p)
        {
            if (i == 0 || m == 0) return 0; // 容量和物品数量都为0

            if (w[i] > m)// 当前物品重量超过背包容量
            {
                return UpDown(m, i - 1, w, p);

            }
            else
            {
                int maxValue1 = UpDown(m - w[i], i - 1, w, p) + p[i]; //放进去
                int maxValue2 = UpDown(m, i - 1, w, p);//不放
                if (maxValue1 > maxValue2)
                {
                    return maxValue1;
                }
                return maxValue2;
            }

        }

    }
}
