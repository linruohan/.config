using System;

namespace 数组学习 {
    class 数组学习 {
        static void Main (string[] args) {
            // 数组初始化
            int[] myArray1 = new int[4]; //托管堆
            int[] myArray2_0 = new int[4] { 2, 3, 4, 1 };
            int[] myArray2_1 = new int[] { 2, 3, 4, 1 };
            int[] myArray3 = { 2, 4, 5, 6 };
            // 访问数组
            int v1 = myArray1[0];
            myArray1[3] = 33;
            int len = myArray1.Length;
            for (int i = 0; i < myArray1.Length; i++) {
                Console.WriteLine (myArray1[i]);
            }
            foreach (var val in myArray1) {
                Console.WriteLine (val);
            }
            Person[] myPersons = new Person[2];
            myPersons[0] = new Person { FirstName = "Array", LastName = "Senana" };
            myPersons[1] = new Person { FirstName = "Michael", LastName = "Schumacher" };
            // 数组初始化器:
            Person[] myPersons2 = {
                new Person { FirstName = "Array", LastName = "Senana" },
                new Person { FirstName = "Michael", LastName = "Schumacher" }
            };
            // 二维数组
            int[, ] twodim = new int[3, 3];
            twodim[0, 0] = 1;
            twodim[0, 1] = 2;
            twodim[0, 2] = 3;
            twodim[1, 0] = 4;
            twodim[1, 1] = 5;
            twodim[1, 2] = 6;
            twodim[2, 0] = 7;
            twodim[2, 1] = 8;
            twodim[2, 2] = 9;
            int[, ] twodim1 = { { 1, 2, 3 },
                { 4, 5, 6 },
                { 7, 8, 9 },
            };
            // 三维数组[3,2]
            int[, , ] threein = { { { 1, 2 }, { 3, 4 } },
                { { 5, 6 }, { 7, 8 } },
                { { 9, 12 }, { 13, 14 } },

            };
            // 锯齿数组:每一行都可以有不同的大小
            int[][] jagged = new int[3][];
            jagged[0] = new int[2] { 1, 2 };
            jagged[1] = new int[5] { 1, 2, 5, 13, 54 };
            jagged[2] = new int[3] { 1, 2, 4 };
            for (int row = 0; row < jagged.Length; row++) {
                for (int element = 0; element < jagged[row].Length; element++) {
                    Console.WriteLine ("row:{0},element:{1},value:{2}", row, element, jagged[row][element]);
                }
            }
            CreateArray.create ();

            // 复制数组
            int[] intArrays3 = { 1, 2 };
            int[] intArrays4 = (int[]) intArrays3.Clone (); //值复制
            // 数组排序

            string[] names = {
                "CHristmas",
                "Shrad",
                "Beyond",

            };
            Array.Sort (names);
            foreach (var name in names) {
                Console.WriteLine (name);

            }

            // 现在可以按照姓氏对persons对象对应的数组排序:
            Person[] persons = {
                new Person { FirstName = "safs", LastName = "Fsdfas" },
                new Person { FirstName = "Nike", LastName = "Fsdfas" },
                new Person { FirstName = "Add", LastName = "Fsdfas" },
                new Person { FirstName = "Gra", LastName = "Fsdfas" },
            };
            Array.Sort (persons);
            foreach (var p in persons) {
                Console.WriteLine (p);
            }

            Array.Sort (persons, new PersonComparer (PersonCompareType.FirstName));
            foreach (var p in persons) {
                Console.WriteLine (p);
            }
        }

    }
    public class Person : IComparable<Person> {
        // 修改Person类,使之实现1C玩叩田洫矧h的少接口。对lastName的值进行比较。lastName是string类型,而 string类已经实现了ICommble接口,所以可以使用 string类中CompareTo()方法的实现代码。
        // 如果LastNme的值同,就比较firstname
        public int CompareTo (Person other) {
            if (other == null) throw new ArgumentNullException ("other");
            int result = this.LastName.CompareTo (other.LastName);
            if (result == 0) {
                result = this.FirstName.CompareTo (other.FirstName);
            }
            return result;
        }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public override string ToString () {
            return String.Format ("{0} {1}", FirstName, LastName);
        }

    }
    public enum PersonCompareType {
        FirstName,
        LastName
    }

    public class PersonComparer : IComparer<person> {
        private PersonCompareType compareType;
        public PersonComparer (PersonCompareType compareType) {
            this.compareType = compareType;
        }
        public int Compare (Person x, Person y) {
            if (x == null) throw ArgumentNullException ("x");
            if (y == null) throw ArgumentNullException ("y");
            switch (compareType) {
                case PersonCompareType.FirstName:
                    return x.FirstName.CompareTo (y.FirstName);
                case PersonCompareType.LastName:
                    return x.LastName.CompareTo (y.LastName);
                default:
                    throw new ArgumentException ("unexpected compare type");
            }
        }
    }
    public static class CreateArray {
        public static void create () {
            Array intArrays = Array.CreateInstance (typeof (int), 5);
            for (int i = 0; i < 5; i++) {
                intArrays.SetValue (33, i);
            }
            for (int i = 0; i < 5; i++) {
                Console.WriteLine (intArrays.GetValue (i));
            }
            // 将已创建的数组强制转换成声明为int[]的数组:
            int[] intArrays2 = (int[]) intArrays;
            // 可以创建多维数组和不基于0的数组。下面的例子就创建了一个包含2×3个元素的二维数组。第一维基于1,第二维基于10g
            int[] lengths = { 2, 3 };
            int[] lowerBounds = { 1, 10 };
            Array racers = Array.CreateInstance (typeof (Person), lengths, lowerBounds);
            // SetValue方法设置数组的元素,其参数是每一维的索引:
            racers.SetValue (new Person {
                FirstName = "Alain",
                    LastName = "Prost"
            }, 1, 10);
            racers.SetValue (new Person {
                FirstName = "Emerpson",
                    LastName = "Fittipaldi"
            }, 1, 11);
            racers.SetValue (new Person {
                FirstName = "Ayrton",
                    LastName = "Senna"
            }, 1, 12);

            racers.SetValue (new Person {
                FirstName = "Ralf",
                    LastName = "Schumacher"
            }, 2, 10);
            racers.SetValue (new Person {
                FirstName = "Fernando",
                    LastName = "Alonso"
            }, 2, 11);
            racers.SetValue (new Person {
                FirstName = "Jenson",
                    LastName = "Button"
            }, 2, 12);

            // 尽管数组不是基于0,但可以用一般的C#表示法将它赋予一个变量。只需注意不要超出边界即可:
            Person[, ] racers2 = (Person[, ]) racers;
            Person first = racers2[1, 10];
            Person last = racers2[2, 12];
        }

    }
}