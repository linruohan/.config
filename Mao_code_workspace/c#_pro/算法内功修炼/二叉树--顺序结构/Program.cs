using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 二叉树__顺序结构
{
    partial class Program
    {
        static void Main(string[] args)
        {
            char[] data = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' };

            BiTree<char> tree = new BiTree<char>(data.Length);
            for (int i = 0; i < data.Length; i++)
            {
                tree.Add(data[i]);
            }
            tree.FirstTraversal();
            Console.WriteLine();
            tree.MiddleTraversal();
            Console.WriteLine();
            tree.LastTraversal();
            Console.WriteLine();
            tree.LayerTraversal();
            Console.ReadKey();
        }

    }
}
