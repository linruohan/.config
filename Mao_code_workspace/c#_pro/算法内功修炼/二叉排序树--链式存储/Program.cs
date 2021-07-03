using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 二叉排序树__链式存储
{
    partial class Program
    {
        static void Main(string[] args)
        {

            BSTree tree = new BSTree();
            int[] data = { 62, 58, 88, 47, 73, 99, 35, 51, 93, 37 };
            foreach (int t in data)
            {
                tree.Add(t);

            }

            tree.MiddleTraversal();
            Console.WriteLine();
            Console.WriteLine(tree.Find(99));
            Console.WriteLine(tree.Find(100));
            tree.Delete(35);
            tree.MiddleTraversal();
            Console.WriteLine();
            tree.Delete(62);
            tree.MiddleTraversal();
            Console.WriteLine();
            Console.ReadKey();



        }
    }
}
