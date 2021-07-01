namespace CmdGame
{
    partial class Program
    {
        static int score = 200;
        public class Enemy : Actor {
            public override int Type => (int)EActorType.Enemy;

            protected override void OnDied()
            {
                GameState.Instance.score += score;
            }
        }

    }
}
