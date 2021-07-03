using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 最大子数组__分治算法
{
    class Program
    {
        // 最大子数组的结构体
        struct SubArray
        {
            public int startIndex;
            public int endIndex;
            public int total;
        }
        static void Main(string[] args)
        {
            int[] priceArray = { 100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97 }; //股票数据
            int[] pf = new int[priceArray.Length - 1];//股票价格波动数组,第二天的减去第一天的差值,
            for (int i = 1; i < priceArray.Length; i++)
            {
                pf[i - 1] = priceArray[i] - priceArray[i - 1];
            }
            SubArray subArray= GetMaxSubArray(0, pf.Length - 1, pf);
            Console.WriteLine($"startIndex:{subArray.startIndex}");
            Console.WriteLine($"endIndex:{subArray.endIndex}");
            Console.WriteLine($"购买日期是第 {subArray.startIndex} 天; 出售日期是第 {subArray.endIndex + 1} 天");
            Console.ReadKey();

        }
        static SubArray GetMaxSubArray(int low, int high, int[] array)
        {
            // 循环跳出条件
            if (low == high)
            {
                SubArray subArray = new SubArray();
                subArray.startIndex = low;
                subArray.endIndex = high;
                subArray.total = array[low];
                return subArray;
            }
            int mid = (low + high) / 2; //自动取整  低区间[low,mid]  高区间[mid+1,high]
            // 1. i和j都在低区间
            SubArray subArray1 = GetMaxSubArray(low, mid, array);
            // 2. i和j都在高区间
            SubArray subArray2 = GetMaxSubArray(mid + 1, high, array);
            // 3. i在低区间,j在高区间
            int total1 = array[mid]; //最大子数组的和
            int startIndex = mid;
            int totalTemp = 0;
            //3.1 从[low,mid]找到最大子数组[i,mid]
            for (int i = mid; i >= low; i--)
            {
                totalTemp += array[i];
                if (totalTemp > total1)
                {
                    total1 = totalTemp;
                    startIndex = i;
                }
            }
            // 3.2 从[mid+1,high]找到最大子数组[i,mid]
            int total2 = 0;
            total2 = array[mid + 1];
            int endIndex = mid + 1;
            totalTemp = 0;
            for (int j = (mid + 1); j < high; j++)
            {
                totalTemp += array[j];
                if (totalTemp > total2)
                {
                    total2 = totalTemp;
                    endIndex = j;
                }
            }
            SubArray subArray3 = new SubArray();
            subArray3.startIndex = startIndex;
            subArray3.endIndex = endIndex;
            subArray3.total = total1 + total2;

            // 4 比较最大的total
            if (subArray1.total>=subArray2.total && subArray1.total>=subArray3.total)
            {
                return subArray1;
            }else if (subArray2.total >= subArray1.total && subArray2.total >= subArray3.total)
            {
                return subArray2;
            }
            else
            {
                return subArray3;
            }



        }

    }
}
