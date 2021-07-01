using System;

namespace CmdGame
{
    partial class Program
    {
        public class CmdRenderEngine : RenderEngine
        {
            // 0表示么有 >0正常显示,<0表示受伤
            int[,] mapData; //每一个点上面的信息
            public override void SetMapSize(int rowCount, int colCount)
            {
                base.SetMapSize(rowCount, colCount);
                mapData = new int[rowCount, colCount];
            }

            public override void Render(RenderInfos info)
            {
                Debug.Log($" {GetType().Name} Update");
                Console.Clear(); // 控制台清空以防一直打印下去,没有页面刷新的效果

                // 清空地图
                for (int row = 0; row < RowCount; row++)
                {
                    for (int col = 0; col < ColCount; col++)
                    {

                        mapData[row, col] = 0;
                    }
                }
                var infos = info.GetInfos();
                foreach (var item in infos)
                {
                    //ColCount=21
                    // -10 0 10 //玩家位置x
                    // 0 10 20 //显示列
                    //RowCount=21
                    //玩家 显示行
                    //10 20
                    //0  10
                    //-10  0
                    var halfColCount = (ColCount - 1) / 2;
                    var col = item.pos.x + halfColCount;
                    var halfRowCount = (RowCount - 1) / 2;
                    var row = item.pos.y + halfRowCount;
                    mapData[row, col] = item.color * item.type;
                }
                const int CharSpaceCount = 2;
                for (int row = 0; row < RowCount; row++)
                {
                    int lastIdx = -1;
                    for (int col = 0; col < ColCount; col++)
                    {
                        var val = mapData[RowCount - row - 1, col];
                        if (val == 0) continue;
                        var spaceCount = col - lastIdx - 1; // 打印一行中没有遇到玩家前的空白字符
                        lastIdx = col;
                        var spaceStr = new string(' ', spaceCount * CharSpaceCount);
                        Console.Write(spaceStr);
                        // 判断是否受伤设置需要打印的颜色  ,受伤打印红色,否则白色
                        var color = val < 0 ? ConsoleColor.Red : ConsoleColor.White;
                        Console.ForegroundColor = color;
                        //  打印actor, type=1 玩家 | type=2 怪物
                        var ch = (Math.Abs(val) == (int)EActorType.Enemy ? "M" : "P") + new string(' ', CharSpaceCount - 1);
                        Console.Write(ch);
                        Console.ForegroundColor = ConsoleColor.White; //颜色恢复初始状态
                    }
                    var endSpaceStr = new string(' ', (ColCount - lastIdx - 1) * CharSpaceCount);
                    Console.Write(endSpaceStr);
                    Console.ForegroundColor = ConsoleColor.White;
                    //  打印最后一列的边界线
                    Console.Write('|');
                    Console.WriteLine();



                }
                //  打印最后一行的边界线
                var endLineStr = new string('-', ColCount * CharSpaceCount);
                Console.Write(endLineStr + "\n");
                var extraInfos = info.GetExtraInfos();
                foreach (var item in extraInfos)
                {
                    Console.Write(item);
                }
            }

        }

    }
}
