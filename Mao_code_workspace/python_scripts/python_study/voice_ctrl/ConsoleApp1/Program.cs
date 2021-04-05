using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            //泛型类型的协变
            IIndex<Rectangle> rectangle = RectangleCollection.GetRectangles();
            IIndex<Shape> shapes = rectangle;
            for (int i = 0; i < shapes.Count; i++)
            {
                Console.WriteLine(shapes[i]);
            }
            //泛型类型的抗变
            IDisplay<Shape> shapeDisplay = new ShapeDisplay();
            IDisplay<Rectangle> rectangleDisplay = shapeDisplay;
            rectangleDisplay.Show(rectangle[0]);
            //结构泛型
            Nullable<int> x1;
            x1 = 3;
            //x = x + (int)3;
            if (x1.HasValue)
            {
                int y = x1.Value;
            }
            //x = null;

            int? x = GetNullableType();
            if (x==null)
            {
                Console.WriteLine("x is null");
            }
            else if (x < 0)
            {
                Console.WriteLine("x is smaller than 0");
            }



        }

        public class Shape
        {
            public double Width { get; set; }
            public double Height { get; set; }
            public override string ToString()
            {
                return string.Format("Width:{0},Height:{1}", Width, Height);


            }
        }

        public class Rectangle : Shape { }
        //==========  out  =====泛型接口的协变======T既可以作为输入，也可作为输出=========================================
        public interface IIndex<out T>
        {
            T this[int index] { get; }
            int Count { get; }

        }
        public class RectangleCollection : IIndex<Rectangle>
        {
            private Rectangle[] data = new Rectangle[3] {
                new Rectangle{Height=2,Width=5},
                new Rectangle{Height=3,Width=7},
                new Rectangle{Height=4,Width=2.9}
            };
            public static RectangleCollection GetRectangles()
            {
                return new RectangleCollection();

            }
            public Rectangle this[int index]
            {
                get
                {
                    if (index < 0 || index > data.Length)
                    {
                        throw new ArgumentOutOfRangeException("index");
                    }
                    return data[index];
                }


            }
            public int Count
            {
                get
                {
                    return data.Length;
                }
            }




        }

        //========  in =======泛型接口的抗变===只能用作方法的输入============================================

        public interface IDisplay<in T>
        {
            void Show(T item);
        }

        public class ShapeDisplay : IDisplay<Shape>
        {
            public void Show(Shape s)
            {
                Console.WriteLine("{0} Width: {1}, Height:{2}", s.GetType().Name, s.Width, s.Height);

            }

        }


        //======泛型结构=================================================
        public struct Nullable<T>
            where T : struct
        {
            public Nullable(T value)
            {
                this.hasValue = true;
                this.value = value;
            }
            private bool hasValue;
            public bool HasValue
            {
                get { return hasValue; }
            }
            private T value;
            public T Value
            {
                get
                {
                    if (!hasValue)
                    {
                        throw new InvalidOperationException("no value");

                    }
                    return value;
                }
            }

            public static explicit operator T(Nullable<T> value)
            {
                return value.Value;
            }
            public static implicit operator Nullable<T>(T value)
            {
                return new Nullable<T>(value);
            }


            public override string ToString()
            {
                if (!HasValue)
                {
                    return string.Empty;
                }
                return this.value.ToString();
            }
        }
    }

}
