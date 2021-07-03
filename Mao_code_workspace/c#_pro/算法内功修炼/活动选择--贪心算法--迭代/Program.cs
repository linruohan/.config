using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 活动选择__贪心算法__迭代
{
    class Program
    {
        static void Main(string[] args)
        {

            int[] s = { 0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12, 24 }; // 开始时间
            int[] f = { 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24 };//结束时间

            int startTime = 0; int endTime = 24;
            List<int> list = new List<int>();
            for (int number = 1; number <= 11; number++)//活动循环
            {
                if (s[number] >= startTime && f[number] <= endTime)
                {
                    list.Add(number);
                    startTime = f[number]; //循环开始时间==上一个活动结束时间
                }
            }
            foreach (int i in list)
            {
                Console.WriteLine(i);
            }
            Console.ReadKey();
        }
    }
}
