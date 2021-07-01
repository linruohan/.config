using System;
using System.Threading;

namespace CmdGame
{
    partial class Program
    {
        public class Driver
        {
            public static int FrameIntervalMS = 30;
            private static bool isNeedStop;

            public static void Start(Action<char> onGetInptut, Func<double, double, bool> onUpdate)
            {
                var thread = new Thread(() =>
                {
                    while (true)
                    {
                        var info = Console.ReadKey();
                        var inputCh = info.KeyChar;
                        onGetInptut(inputCh);
                    }
                });
                thread.Start();
                RepeatInvoke((timeSinceStart, dt) =>
                {
                    isNeedStop = onUpdate(timeSinceStart, dt);
                }, FrameIntervalMS);
            }

            static void RepeatInvoke(Action<double, double> func, int callIntervalMS)
            {
                var initTime = DateTime.Now;  //启动时间
                var lastTImestamp = DateTime.Now; //上次更新的时间
                while (true)
                {
                    try
                    {
                        Thread.Sleep(Math.Max(1, callIntervalMS));
                        var totalElipse = DateTime.Now - initTime;

                        var totalSec = totalElipse.TotalSeconds;
                        var elipse = DateTime.Now - lastTImestamp;
                        var dtSec = elipse.TotalSeconds;
                        lastTImestamp = DateTime.Now;
                        func(totalSec, dtSec);
                        if (isNeedStop) return;

                    }
                    catch (ThreadAbortException e)
                    {
                        return;
                    }
                    catch (Exception e)
                    {
                        Console.WriteLine(e.ToString());
                        return;
                    }
                }


            }
        }
    }
}
