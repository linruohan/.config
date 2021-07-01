using System;

namespace CmdGame
{
    partial class Program
    {
        public class Component
        {
            public Actor actor;
            public void Bind(Actor actor)
            {
                this.actor = actor;
            }
            public virtual void Awake()
            {
                Debug.Log($"{GetType().Name} Awake");
            }
            public virtual void Update(float dt)
            {
                Debug.Log($"\t\t {GetType().Name} Update");
            }

        }

    }
}
