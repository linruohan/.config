namespace CmdGame
{
    partial class Program
    {
        public class Skill : Component
        {
            public float cd=1;
            public float cdTimer;
            public float atkDist = 2f;
            public override void Update(float dt)
            {
                base.Update(dt);
                //攻击有cd
                cdTimer += Time.deltaTime;
                if (cdTimer < cd) return;
                cdTimer = 0;
                var target = actor.FindTarget();
                if (target == null) return;
                // 攻击距离判定
                if ((target.pos - actor.pos).magnitude > atkDist) return;
                if(target != null)
                {
                    actor.Attack(target);
                }
            }
        }

    }
}
