namespace CmdGame
{
    partial class Program
    {
        static void Main(string[] args)
        {
            var game = new Game();
            game.Awake();
            char ch = ' ';

            Driver.FrameIntervalMS = 300; //100毫秒更新一次
            Driver.Start(game.OnGetInput, game.onUpdate);
           /* var thread = new Thread(()=>{
                while (true)
                {
                    var info = Console.ReadKey();
                    ch = info.KeyChar;
                }

            });
            thread.Start();
            while (true)
            {

                Thread.Sleep(300);
                game.Update();
                if (ch != ' ')
                {
                    Console.WriteLine("--------------------------------" + ch);
                }
                ch = ' ';
            }
            Console.ReadLine();*/

        }
    }
}
