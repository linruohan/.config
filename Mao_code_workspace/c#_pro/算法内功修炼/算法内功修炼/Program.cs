using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 算法内功修炼
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] priceArray = { 100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97 }; //股票数据
            int[] pf = new int[priceArray.Length - 1];//股票价格波动数组,第二天的减去第一天的差值,
            for (int i = 1; i < priceArray.Length; i++)
            {
                pf[i - 1] = priceArray[i] - priceArray[i - 1];
            }

            int total = pf[0];//默认数组的第一个元素,最大子数组的和,既收益值
            int startIndex = 0;
            int endIndex = 0;
            for (int i = 0; i < pf.Length; i++)
            {
                //取得以i为子数组七点的所有子数组

                for (int j = i; j < pf.Length; j++)
                {
                    //由I J确定了一个子数组
                    int totalTemp = 0;// 临时最大子数组的和
                    for (int index = i; index < j+1; index++)
                    {
                        totalTemp += pf[index];
                    }
                    if (totalTemp > total)
                    {
                        total = totalTemp;
                        startIndex = i;
                        endIndex = j;
                    }

                }

            }
            Console.WriteLine($"startIndex:{startIndex}");
            Console.WriteLine($"endIndex:{endIndex}");
            Console.WriteLine($"购买日期是第 {startIndex} 天; 出售日期是第 {endIndex+1} 天");
            Console.ReadKey();
        }
    }
}
