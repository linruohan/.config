using System;

namespace 二叉树__顺序结构
{
    partial class Program
    {
        //如果一个节点为空,节点所在的数组位置,设置为-1
        class BiTree<T>
        {
            private T[] data;
            private int count = 0;
            public BiTree(int capacity) // 容量,最大存放的数据个数
            {
                data = new T[capacity];
            }
            public bool Add(T item)
            {
                if (count >= data.Length)
                    return false;
                data[count] = item;
                count++;
                return true;
            }
            public void FirstTraversal()
            {
                FirstTraversal(0);
            }

            // 1. 前序遍历: 先打印当前值,再遍历左节点,再右节点
            private void FirstTraversal(int index)
            {
                if (index >= count) return;
                //获取要遍历的节点的编号
                int number = index + 1;
                if (data[index].Equals(-1)) return;
                Console.Write(data[index] + " ");
                int leftNumber = number * 2;
                int rightNumber = number * 2 + 1;
                FirstTraversal(leftNumber - 1);
                FirstTraversal(rightNumber - 1);
            }
            public void MiddleTraversal()
            {
                MiddleTraversal(0);
            }
            // 2. 中序遍历: 先遍历左节点,打印当前值,再右节点
            private void MiddleTraversal(int index)
            {
                if (index >= count) return;
                //获取要遍历的节点的编号
                int number = index + 1;
                if (data[index].Equals(-1)) return;
                int leftNumber = number * 2;
                int rightNumber = number * 2 + 1;
                MiddleTraversal(leftNumber - 1);
                Console.Write(data[index] + " ");
                MiddleTraversal(rightNumber - 1);

            }
            public void LastTraversal()
            {
                LastTraversal(0);
            }
            // 3. 后序遍历: 先遍历左节点,再右节点,最后打印当前值
            private void LastTraversal(int index)
            {
                if (index >= count) return;
                //获取要遍历的节点的编号
                int number = index + 1;
                if (data[index].Equals(-1)) return;
                int leftNumber = number * 2;
                int rightNumber = number * 2 + 1;
                LastTraversal(leftNumber - 1);
                LastTraversal(rightNumber - 1);
                Console.Write(data[index] + " ");
            }
            // 4. 层序遍历: 从根节点开始,一层一层遍历
            public void LayerTraversal()
            {
                for (int i = 0; i < count; i++)
                {
                    if (data[i].Equals(-1)) continue;// 无数据的情况,节点为空
                    Console.Write(data[i] + " ");
                }
                Console.WriteLine();
            }
            
        }

    }
}
