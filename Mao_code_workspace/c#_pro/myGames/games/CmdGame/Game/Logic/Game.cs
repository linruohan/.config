using System;

namespace CmdGame
{
    partial class Program
    {
        public class Game : ILifeCycle
        {
            public World world = new World();
            public EGameState state;

            public void Awake()
            {
                Debug.Log($"{GetType().Name} Awake");
                world = new World();
                world.Awake();
                // TODO create actors
                LoadSceneFromConfig();

                /*world.AddActor(CreatePlayer(1000, 200));
                world.AddActor(CreateEnemy(300, 10));
                world.AddActor(CreateEnemy(300, 11));
                world.AddActor(CreateEnemy(300, 12));*/

            }
            private void LoadSceneFromConfig()
            {
                var allLines = System.IO.File.ReadAllLines("../../config/init.txt");
                var nameSpace = GetType().Namespace;
                foreach (var item in allLines)
                {
                    var strs = item.Split(',');
                    int i = 0;
                    var fullName = $"{nameSpace}.Program.{strs[i++]}";
                    var actor = GetType().Assembly.CreateInstance(fullName) as Actor;
                    actor.health = int.Parse(strs[i++]);
                    actor.damage = int.Parse(strs[i++]);
                    actor.world = world;
                    actor.pos = world.GetRandomPos();
                    var compStrs = strs[i++].Split('|');
                    foreach (var compStr in compStrs)
                    {
                        var compFullName = $"{nameSpace}.{compStr}";
                        var comp = GetType().Assembly.CreateInstance(compFullName) as Component;
                        actor.AddComponent(comp);
                    }
                    world.AddActor(actor);
                }

            }

            Actor CreatePlayer(int health, int damage)
            {
                var player = new Player();
                InitActor(player, health, damage);
                player.AddComponent(new PlyerAI());
                return player;
            }

            Actor CreateEnemy(int health, int damage)
            {
                var enemy = new Enemy();
                InitActor(enemy, health, damage);
                enemy.AddComponent(new EnemyAI());
                return enemy;
            }

            private void InitActor(Actor actor, int health, int damage)
            {
                actor.damage = damage;
                actor.health = health;
                actor.world = world;
                actor.pos = world.GetRandomPos();
                //Console.WriteLine(actor.pos);
                actor.AddComponent(new HurtEffect());
                actor.AddComponent(new Skill());
            }

            public void Update()
            {
                Time.deltaTime = 0.1f;
                Debug.Log($"{GetType().Name} Update FrameCount {Time.frameCount}");
                world.Update();
                CheckGameState();
                world.Render();


                Time.frameCount++;
            }

            private void CheckGameState()
            {
                // 判定游戏胜负条件
                if (world.GetActorCount((int)EActorType.Player) == 0)
                {
                    GameState.Instance.state = EGameState.Loss;
                }
                if (world.GetActorCount((int)EActorType.Enemy) == 0)
                {
                    GameState.Instance.state = EGameState.Win;
                }
            }

            public Vector2 inputVec { get; set; }
            public void OnGetInput(char inputCh)
            {
                switch (inputCh)
                {
                    case 'w': InputManager.inputVec = new Vector2(0, 1); break;
                    case 's': InputManager.inputVec = new Vector2(0, -1); break;
                    case 'a': InputManager.inputVec = new Vector2(-1, 0); break;
                    case 'd': InputManager.inputVec = new Vector2(1, 0); break;
                }
            }

            public bool onUpdate(double timeSinceStart, double deltaTime)
            {
                Time.deltaTime = (float)deltaTime;
                Update();
                return false;
            }

        }

    }
}
