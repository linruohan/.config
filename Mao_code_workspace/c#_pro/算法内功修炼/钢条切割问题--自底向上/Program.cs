using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 钢条切割问题__自底向上
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 5;  // 要切割售卖钢条的长度
            int[] results = new int[11];

            int[] price = { 0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30 }; // 索引代码钢条的长度,值代表价格
            Console.WriteLine(BottomUp(0,price,results));
            Console.WriteLine(BottomUp(1,price,results));
            Console.WriteLine(BottomUp(2,price,results));
            Console.WriteLine(BottomUp(3,price,results));
            Console.WriteLine(BottomUp(4,price,results));
            Console.WriteLine(BottomUp(5,price,results));
            Console.WriteLine(BottomUp(6,price,results));
            Console.WriteLine(BottomUp(7,price,results));
            Console.WriteLine(BottomUp(8,price,results));
            Console.WriteLine(BottomUp(9,price,results));
            Console.WriteLine(BottomUp(10,price,results));

            Console.ReadKey();
        }
        public static int BottomUp(int n, int[] p, int[] result)
        {
            for (int i = 1; i < n + 1; i++)
            {
                // 下面取得钢条长度为i的最大收益
                int tmpMaxPrice =-1;
                for (int j = 1; j <= i; j++)
                {
                    int maxPrice = p[j] + result[i - j];
                    if (maxPrice > tmpMaxPrice)
                    {
                        tmpMaxPrice = maxPrice;
                    }
                }
                result[i] = tmpMaxPrice;
            }
            return result[n];
        }
    }

}
