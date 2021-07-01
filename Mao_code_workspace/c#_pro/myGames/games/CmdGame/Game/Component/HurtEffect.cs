using System;

namespace CmdGame
{
    partial class Program
    {
        public class HurtEffect : Component
        {
            public float duration = 0.3f; //攻击持续时间
            public float timer = 0;

            public override void Awake()
            {
                base.Awake();
                actor.OnHurtEvent += OnHurt; //TODO 会报错终端,待处理
            }
            void OnHurt(Actor actor)
            {
                timer = 0;
            }
            public override void Update(float dt)
            {
                base.Update(dt);
                timer += Time.deltaTime;
                if (timer > duration && actor.isHurt)
                {
                    actor.isHurt = false;
                }
            }
        }

    }
}
