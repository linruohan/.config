using System;
using System.Collections.Generic;

namespace CmdGame
{
    partial class Program
    {
        public class Actor
        {
            public virtual int Type => 0;
            public Vector2 _pos;
            public int damage;
            public int health;
            public int initHealth; //初始血量
            public bool isHurt;
            public World world;

            public Action<Actor> OnHurtEvent;

            public Actor FindTarget()
            {
                return world.FindTarget(pos, Type);
            }
            public void Attack(Actor target)
            {
                if (target.health < 0) return;
                target.health -= damage;
                isHurt = true;
                target.OnHurtEvent?.Invoke(this); //如果不为null就回调
                //血量小于0,先不删除
                if (target.health <= 0)
                {
                    //world.RemoveActor(target);
                    target.OnDied();
                }
            }

            protected virtual void OnDied()
            {
            }

            public Vector2 pos
            {
                get => _pos;
                set
                {
                    value = world.GetValidPos(value);
                    _pos = value;
                }
            }

            private List<Component> components = new List<Component>();

            public void AddComponent(Component comp)
            {
                components.Add(comp);
                comp.Awake();
                comp.Bind(this);//绑定角色到component上
            }
            public void Awake()
            {
                initHealth = health;
                Debug.Log($"{GetType().Name} Awake");
            }
            public virtual void Update()
            {
                Debug.Log($"\t {GetType().Name} Update");
                foreach (var item in components)
                {
                    item.Update(Time.deltaTime);
                }
            }
            public override string ToString()
            {
                return $" pos:{pos}; h:{health};type:{Type};isHurt:{isHurt}\n";
            }
        }

    }
}
