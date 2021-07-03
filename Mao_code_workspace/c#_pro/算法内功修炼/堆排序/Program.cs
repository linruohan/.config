using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 堆排序
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] data = { 50, 10, 90, 30, 70, 40, 80, 60, 20 };
            HeapSort(data);
            foreach (int i in data)
            {
                Console.Write($"{i} ");
            }


            Console.ReadKey();




        }

        public static void HeapSort(int[] data)
        {
            //  i 表示二叉树中的编号,不是index
            for (int i = data.Length / 2; i >= 1; i--)//遍历这个树的所有非叶节点,挨个把所有的子树变成大顶堆
            {

                HeapAdjust(i, data, data.Length);
            }
            // 经过上面的循环,将数据变成大顶堆  i=1不需要排序
            for (int i =data.Length; i >1; i--)
            {
                //把1和编号为i的位置的数据进行交换 
                // 把1到(i-1)构造成大顶堆
                int temp1 = data[0];
                data[0] = data[i - 1];
                data[i - 1] = temp1;
                HeapAdjust(1, data, i - 1);
            }
        }

        private static void HeapAdjust(int numberToAdjust,int[] data,int maxNumber)
        {
            

            int maxNodeNulber = numberToAdjust; //最大节点的编号
            int tempI = numberToAdjust;
            while (true)
            {
                //把i节点的子树变成大顶堆
                int leftChildNumber = tempI * 2;
                int rightChildNumber = leftChildNumber + 1;
                if (leftChildNumber <= maxNumber && data[leftChildNumber - 1] > data[maxNodeNulber - 1])// 左孩子存在,且值比最大值大
                {
                    maxNodeNulber = leftChildNumber;
                }
                if (rightChildNumber <= maxNumber && data[rightChildNumber - 1] > data[maxNodeNulber - 1])
                {
                    maxNodeNulber = rightChildNumber;
                }

                // 没有找到比i更大的子节点,交换i和maxNodeNumber的数据
                if (maxNodeNulber != tempI)
                {
                    int temp = data[tempI - 1];
                    data[tempI - 1] = data[maxNodeNulber - 1];
                    data[maxNodeNulber - 1] = temp;
                    tempI = maxNodeNulber;

                }
                else
                {
                    break;
                }
            }
        }
    }
}
