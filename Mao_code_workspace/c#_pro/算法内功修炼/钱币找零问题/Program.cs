using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 钱币找零问题
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] count = { 3, 0, 2, 1, 0, 3, 5 };//纸币的数量
            int[] amount = { 1, 2, 5, 10, 20, 50, 100 }; // 纸币的面额
            int[] result = Change(320, count, amount);
            for (int i = 0; i < result.Length - 1; i++)
            {
                if (result[i] > 0)
                    Console.WriteLine($"{amount[i]}元使用了 {result[i]}张");
            }
            if (result[result.Length - 1] > 0) //没有换完
            {
                Console.WriteLine($"还剩余{result[result.Length - 1]}元,没有换出来");

            }
            Console.ReadKey();
        }


        public static int[] Change(int k, int[] count, int[] amount)
        {

            if (k == 0) return new int[amount.Length + 1];
            int total = 0;
            int index = amount.Length - 1;
            int[] result = new int[amount.Length + 1];
            while (true)
            {
                if (k <= 0 || index <= -1) break;
                if (k > count[index] * amount[index])//零钱金额小于要换的钱
                {
                    result[index] = count[index];
                    k -= count[index] * amount[index];
                }
                else
                {
                    result[index] = k / amount[index];
                    k -= result[index] * amount[index];
                }
                index--;
            }
            result[amount.Length] = k; // 只换了多少钱,剩余不够换的钱
            return result;
        }
    }
}
