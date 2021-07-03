namespace 二叉排序树__链式存储
{
    partial class Program
    {
        class BSNode
        {
            public BSNode LeftChild { get; set; }
            public BSNode RightChild { get; set; }
            public BSNode Parent { get; set; }
            public int Data { get; set; }
            public BSNode()
            {

            }

            public BSNode(int item)
            {
                this.Data = item;
            }


        }
    }
}
