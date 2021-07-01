using System;

namespace CmdGame
{
    partial class Program
    {
        public class RandomUtil
        {
            private static Random random = new Random();
            public static int Range(int minVal, int maxVal)
            {
                return random.Next(minVal, maxVal + 1); //[minVal,maxVal)
            }
        }

    }
}
