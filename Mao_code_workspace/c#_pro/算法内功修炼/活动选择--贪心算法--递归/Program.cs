using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 活动选择__贪心算法__递归
{
    class Program
    {

        static int[] s = { 0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12, 24 }; // 开始时间
        static int[] f = { 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 24 };//结束时间

        static void Main(string[] args)
        {
            List<int> list = ActivitySelection(1, 11, 0, 20);
            foreach (int tmp in list)
            {
                Console.WriteLine(tmp);
            }
            Console.ReadKey();

        }
        public static List<int> ActivitySelection(int startNumber, int endNumber, int startTime, int endTime)
        {
            if (startNumber > endNumber || startTime >= endTime) return new List<int>();
            // 找到结束时间最早的活动
            int tmpNumber = 0;
            for (int number = startNumber; number <= endNumber; number++)
            {
                if (s[number] >= startTime && f[number] <= endTime)
                {
                    tmpNumber = number;
                    break;
                }
            }
            List<int> list = ActivitySelection(tmpNumber + 1, endNumber, f[tmpNumber], endTime);
            list.Add(tmpNumber);
            return list;

        }


    }
}
