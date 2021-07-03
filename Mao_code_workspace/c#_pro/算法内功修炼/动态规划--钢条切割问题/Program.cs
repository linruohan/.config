using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 动态规划__钢条切割问题
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 5;
            int[] price = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 }; // 索引代码钢条的长度,值代表价格

            Console.WriteLine(UpDown(0, price));
            Console.WriteLine(UpDown(1, price));
            Console.WriteLine(UpDown(2, price));
            Console.WriteLine(UpDown(3, price));
            Console.WriteLine(UpDown(4, price));
            Console.WriteLine(UpDown(5, price));
            Console.WriteLine(UpDown(6, price));
            Console.WriteLine(UpDown(7, price));
            Console.WriteLine(UpDown(8, price));
            Console.WriteLine(UpDown(9, price));
            Console.WriteLine(UpDown(10, price));
            Console.ReadKey();

        }

        public static int UpDown(int n,int[] p) // 求得长度为n的最大收益
        {
            if (n == 0) return 0;
            int tempMaxPrice = 0;
            for (int i = 1; i < n+1; i++)
            {
                int maxPrice = p[i] + UpDown(n - i, p);
                if (maxPrice > tempMaxPrice)
                {
                    tempMaxPrice = maxPrice;
                }
            }
            return tempMaxPrice;
                
        }
    }
}
