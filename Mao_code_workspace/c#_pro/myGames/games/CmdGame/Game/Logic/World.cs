using System;
using System.Collections.Generic;

namespace CmdGame
{
    partial class Program
    {
        public class World : ILifeCycle
        {
            public Vector2 xRange = new Vector2(-20, 20);
            public Vector2 yRange = new Vector2(-20, 20);
            RenderEngine renderEngine;
            private List<Actor> allActor = new List<Actor>();
            private const int MaxActorTypeCount = 100;
            public int[] actorCount = new int[(int)EActorType.EnumCount];
            private void OnActorCreate(Actor actor)
            {
                actorCount[actor.Type]++;
            }

            private void OnActorDestroy(Actor actor)
            {
                actorCount[actor.Type]--;
            }
            public int GetActorCount(int type)
            {
                return actorCount[type];
            }
            public Vector2 GetRandomPos()
            {
                var x = RandomUtil.Range(xRange.x, xRange.y);
                var y = RandomUtil.Range(yRange.x, yRange.y);
                //Console.WriteLine($"GetRandomPos x:{x} y:{y}");
                return new Vector2(x, y);
            }
            public void AddActor(Actor actor)
            {
                allActor.Add(actor);
                OnActorCreate(actor);
                actor.Awake(); //唤醒

            }

            public void RemoveActor(Actor target)
            {
                allActor.Remove(target);
            }

            public Actor FindTarget(Vector2 pos,int type)
            {
                // 找到离我最近的怪
                float lastDist = float.MaxValue;
                Actor target = null;
                foreach (var item in allActor)
                {
                    if(item.health>0 && item.Type != type)
                    {
                        var dist = (item.pos - pos).magnitude;
                        if (dist < lastDist)
                        {
                            target = item;
                            lastDist = dist;
                        }
                    }
                }
                return target;
            }
            public void Awake()
            {
                Debug.Log($"{GetType().Name} Awake");
                renderEngine = new CmdRenderEngine(); //TODO: 看环境配置
                renderEngine.SetMapSize(yRange.y - yRange.x + 1, xRange.y - xRange.x + 1);
                renderEngine.Awake();

            }
            List<Actor> allDiedActor = new List<Actor>();
            public void Update()
            {
                Debug.Log($"{GetType().Name} Update");
                // 逻辑
                foreach (var item in allActor)
                {
                    item.Update();
                }
                /*allDiedActor.Clear();
                foreach (var item in allActor)
                {
                    if (item.health <= 0)
                    {
                        allDiedActor.Add(item);
                    }
                }
                foreach (var item in allDiedActor)
                {
                    allActor.Remove(item);

                }*/
                // 倒着删除,不会和原来的list冲突
                for (int i = allActor.Count - 1; i >= 0; i--)
                {
                    if (allActor[i].health <= 0)
                    {
                        allActor.RemoveAt(i);
                        OnActorDestroy(allActor[i]);
                    }
                }

                Render();
            }

            public void Render()
            {
                // 渲染
                renderEngine.Render(GetRenderInfo()); //TODO
            }

            RenderInfos GetRenderInfo()
            {
                var val = new RenderInfos();
                foreach (var item in allActor)
                {
                    var info = new RenderInfo();
                    info.pos = item.pos;
                    info.color = item.isHurt ? -1 : 1;
                    info.type = item.Type;
                    val.AddInfo(info);

                }
                val.AddExtraInfos(allActor);
                val.AddExtraInfo(GameState.Instance);
                return val;
            }

            // 获取合法的坐标值,限制坐标移动
           public Vector2 GetValidPos(Vector2 pos) {
            if (pos.x < xRange.x) pos.x = xRange.x;
            if (pos.x > xRange.y) pos.x = xRange.y;
            if (pos.y < yRange.x) pos.y = yRange.x;
            if (pos.y > yRange.y) pos.y = yRange.y;
            return pos;
        }
        }

    }
}
