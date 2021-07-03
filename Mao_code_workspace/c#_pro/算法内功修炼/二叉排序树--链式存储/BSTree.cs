using System;

namespace 二叉排序树__链式存储
{
    partial class Program
    {
        class BSTree
        { //binary search tree
            BSNode root = null;

            // 添加数据
            public void Add(int item)
            {
                // 默认存储类型为int
                BSNode newNode = new BSNode(item);
                if (root == null)
                {
                    root = newNode;
                }
                else
                {
                    BSNode temp = root;
                    while (true)
                    {
                        if (item >= temp.Data)//放在temp的右边
                        {
                            if (temp.RightChild == null)
                            {
                                temp.RightChild = newNode;
                                newNode.Parent = temp;
                                break;
                            }
                            else
                            {
                                temp = temp.RightChild;
                            }
                        }
                        else// 放在temp的左边
                        {
                            if (temp.LeftChild == null)
                            {
                                temp.LeftChild = newNode;
                                newNode.Parent = temp;
                                break;
                            }
                            else
                            {
                                temp = temp.LeftChild;
                            }
                        }

                    }
                }



            }

            // 中序遍历
            public void MiddleTraversal()
            {
                MiddleTraversal(root);
            }
            private void MiddleTraversal(BSNode node)
            {
                if (node == null) return;
                MiddleTraversal(node.LeftChild);
                Console.Write($"{node.Data} "); //访问数据
                MiddleTraversal(node.RightChild);
            }
            // 查找
            public bool Find(int item)
            {
                //return Find(item, root);
                // find代码优化2
                BSNode temp = root;
                while (true)
                {
                    if (temp == null) return false; //循环终止条件
                    if (temp.Data == item) return true;
                    if (item > temp.Data)
                    {
                        temp = temp.RightChild;
                    }
                    else
                    {
                        temp = temp.LeftChild;
                    }
                }

            }
            private bool Find(int item, BSNode node)
            {
                if (node == null) return false; //循环终止条件
                if (node.Data == item)
                {
                    return true;
                }
                else
                {
                    // find代码优化1
                    //if (Find(item, node.LeftChild)) return true;
                    //if (Find(item, node.RightChild)) return true;
                    if (item > node.Data)
                    {
                        return Find(item, node.RightChild);
                    }
                    else
                    {
                        return Find(item, node.LeftChild);
                    }
                }
                //return false;   //代码优化1
            }



            public bool Delete(int item)
            {
                // 1. 查找该节点
                BSNode temp = root;
                while (true)
                {
                    if (temp == null) return false; //循环终止条件
                    if (temp.Data == item)
                    {
                        Delete(temp);
                        return true;

                    }
                    if (item > temp.Data)
                    {
                        temp = temp.RightChild;
                    }
                    else
                    {
                        temp = temp.LeftChild;
                    }
                }
            }

            public void Delete(BSNode node)
            {
                //  1.  删除叶子节点
                if (node.LeftChild == null && node.RightChild == null)
                {
                    if (node.Parent == null)
                    {
                        root = null;
                    }
                    else if (node.Parent.LeftChild == node)// 删除的节点是左孩子
                    {
                        node.Parent.LeftChild = null;
                    }
                    else if (node.Parent.RightChild == node// 删除的节点是右孩子
                    {
                        node.Parent.RightChild = null;
                    }
                    return;

                }
                //  2.  删除只有左子节点或右子节点的节点
                if (node.LeftChild == null && node.RightChild != null)//只有左子节点
                {
                    node.Data = node.RightChild.Data; // 可以修改链接关系,也可以直接修改数据
                    node.RightChild = null;
                    return;
                }
                if (node.LeftChild != null && node.RightChild == null)//只有右子节点
                {

                    node.Data = node.LeftChild.Data; // 可以修改链接关系,也可以直接修改数据
                    node.LeftChild = null;
                    return;
                }

                //  3.删除既有左子节点又有右子节点的节点   找到最小的节点将它重新关联到被删除的位置上
                BSNode temp = node.RightChild;
                while (true)
                {
                    if (temp.LeftChild != null)
                    {
                        temp = temp.LeftChild;
                    }
                    else
                    {
                        break;
                    }
                }
                node.Data = temp.Data;
                Delete(temp);  // 递归删除
            }
        }
    }
}
