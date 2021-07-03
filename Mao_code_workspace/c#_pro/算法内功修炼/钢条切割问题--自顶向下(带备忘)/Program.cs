using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 钢条切割问题__自顶向下_带备忘_
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 5;  // 要切割售卖钢条的长度
            int[] results = new int[11];

            int[] price = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 }; // 索引代码钢条的长度,值代表价格

            Console.WriteLine(UpDown(0, price, results));
            Console.WriteLine(UpDown(1, price, results));
            Console.WriteLine(UpDown(2, price, results));
            Console.WriteLine(UpDown(3, price, results));
            Console.WriteLine(UpDown(4, price, results));
            Console.WriteLine(UpDown(5, price, results));
            Console.WriteLine(UpDown(6, price, results));
            Console.WriteLine(UpDown(7, price, results));
            Console.WriteLine(UpDown(8, price, results));
            Console.WriteLine(UpDown(9, price, results));
            Console.WriteLine(UpDown(10, price, results));
            Console.ReadKey();

        }
        // 带备忘的自顶向下递归方法
        public static int UpDown(int n, int[] p, int[] results) // 求得长度为n的最大收益
        {
            if (n == 0) return 0;
            if (results[n] != 0) return results[n];
            int tempMaxPrice = 0;
            for (int i = 1; i < n + 1; i++)
            {
                int maxPrice = p[i] + UpDown(n - i, p, results);
                if (maxPrice > tempMaxPrice)
                {
                    tempMaxPrice = maxPrice;
                }
            }
            results[n] = tempMaxPrice;
            return tempMaxPrice;

        }
    }
}
