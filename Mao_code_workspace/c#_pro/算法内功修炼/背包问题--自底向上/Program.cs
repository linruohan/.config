using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 背包问题__自底向上
{
    class Program
    {
        static void Main(string[] args)
        {

            int m; // 包的重量
            int[] w = { 0, 3, 4, 5 };//每个物品的重量
            int[] p = { 0, 4, 5, 6 };//每个物品的价值
            Console.WriteLine(BottomUp(10, 3, w, p));
            Console.WriteLine(BottomUp(3, 3, w, p));
            Console.WriteLine(BottomUp(4, 3, w, p));
            Console.WriteLine(BottomUp(5, 3, w, p));
            Console.WriteLine(BottomUp(7, 3, w, p));
            Console.WriteLine(BottomUp(8, 3, w, p));

            Console.ReadKey();

        }
        public static int[,] result = new int[11, 4];
        // m 背包容量,i是物品个数,wp是重量和价值的数组
        public static int BottomUp(int m, int i, int[] w, int[] p)
        {
            for (int tmpM = 1; tmpM <= m; tmpM++)// 循环重量
            {
                if (result[m, i] != 0) return result[m, i];
                for (int tmpI = 1; tmpI <= i; tmpI++)//循环物品的数量
                {
                    if (result[tmpM, tmpI] != 0) continue;
                    if (w[tmpI] > tmpM)
                    {
                        result[tmpM, tmpI] = result[tmpM, tmpI - 1];
                    }
                    else
                    {
                        int maxValue1 = result[tmpM - w[tmpI], tmpI - 1] + p[tmpI];
                        int maxValue2 = result[tmpM, tmpI - 1];
                        if (maxValue1 > maxValue2)
                        {
                            result[tmpM, tmpI] = maxValue1;
                        }
                        else
                        {
                            result[tmpM, tmpI] = maxValue2;
                        }

                    }

                }
            }
            return result[m, i];
        }
    }
}
