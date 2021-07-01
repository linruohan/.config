namespace CmdGame
{
    partial class Program
    {
        public class GameState
        {
            public static GameState Instance { get; private set; } = new GameState();
            private GameState()
            {

            }
            public EGameState state;
            public int score;
            public override string ToString()
            {
                return $"state:{state};score:{score};\n";
            }
        }

    }
}
