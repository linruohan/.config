namespace CmdGame
{
    partial class Program
    {
        public class Boss : Enemy
        {
            protected override void OnDied()
            {
                GameState.Instance.score += 1000;
            }
            public override void Update()
            {
                base.Update();
                health += 1;

            }
        }

    }
}
