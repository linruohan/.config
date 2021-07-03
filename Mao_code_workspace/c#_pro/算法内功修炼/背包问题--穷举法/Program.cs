using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 背包问题__穷举法
{
    class Program
    {
        static void Main(string[] args)
        {
            int m; // 包的重量
            int[] w = { 0, 3, 4, 5 };//每个物品的重量
            int[] p = { 0, 4, 5, 6 };//每个物品的价值
            Console.WriteLine(Exhaustivity(10, w, p));
            Console.WriteLine(Exhaustivity(3, w, p));
            Console.WriteLine(Exhaustivity(4, w, p));
            Console.WriteLine(Exhaustivity(5, w, p));
            Console.WriteLine(Exhaustivity(7, w, p));
            Console.WriteLine(Exhaustivity(8, w, p));

            Console.ReadKey();

        }
        // 穷举法
        public static int Exhaustivity(int m, int[] w, int[] p)
        {
            int i = w.Length; //物品的个数
            int maxPrice = 0;
            // j 表示可能的物品选择方案的十进制数表示
            for (int j = 0; j < Math.Pow(2, m); j++)//穷举最大次数 1 1 1 1 (2^(4-1))
            {
                // 取得j上某位的二进制值
                int weightTotal = 0;
                int priceTotal = 0;
                // 判断每一个二进制位是否为1,为1表示该物品被选中,0 未选择; 有多少个物品表示j有多少个位;
                for (int number = 1; number < i; number++)
                {
                    int result = Get2(j, number);
                    if (result == 1)
                    {
                        weightTotal += w[number];
                        priceTotal += p[number];
                        Console.WriteLine($"number:{number}");
                    }
                }
                if (weightTotal <= m && priceTotal > maxPrice)
                {
                    maxPrice = priceTotal;
                }

            }
            return maxPrice;
        }
        // 取得j上number位的二进制值是1还是0
        public static int Get2(int j, int number)
        {
            int A = j;
            int B = (int)Math.Pow(2, number - 1);
            int result = A & B;
            Console.WriteLine($"\t\tresult: {result}");
            if (result == 0)
            {
                return 0;
            }
            return 1;
        }


    }
}
