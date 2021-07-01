using System;
using System.Threading;

namespace CmdGame
{
    partial class Program
    {
       
        public class PlyerAI : AI
        {
            public override void Update(float dt)
            {
                base.Update(dt);
                var dir = InputManager.inputVec;
                /*var rawPos = actor.pos;
                rawPos.x += dir.x;
                rawPos.y += dir.y;
                actor.pos = rawPos;*/
                actor.pos += dir;
                InputManager.inputVec = Vector2.zero;
            }
        }


    }
}
