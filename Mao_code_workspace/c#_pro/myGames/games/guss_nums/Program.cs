using System;

namespace guss_nums
{
    class Program
    {
        static Random random = new Random();
        static int totalCount = 0;
        static int systemNumber = 0;

        static int GenRandomInt()
        {
            var number = random.Next(0, 100);
            return number;
        }
        static void ResetStatus()
        {
            totalCount = 0;
            systemNumber = GenRandomInt();
            Console.WriteLine($"the sysmuber is {systemNumber}");
        }
        static void Main(string[] args)
        {

            systemNumber = GenRandomInt();
            Console.WriteLine($"the sysmuber is {systemNumber}");
            while (true)
            {
                Console.WriteLine("请输入一个0~99的数字,按回车键结束: ");
                totalCount++;
                var inputStr = Console.ReadLine();
                int intputNumber = int.Parse(inputStr);
                if (intputNumber == systemNumber)
                {
                    Console.WriteLine($"你太厉害了,你只猜了{totalCount}次,就答对了");
                    // break;
                    //重置游戏
                    ResetStatus();
                }
                else
                {
                    if (intputNumber > systemNumber)
                    {
                        Console.WriteLine("数字太大了");
                    }
                    else
                    {
                        Console.WriteLine("数字太小了");
                    }
                }

                Console.ReadLine();
            }
        }
    }
}