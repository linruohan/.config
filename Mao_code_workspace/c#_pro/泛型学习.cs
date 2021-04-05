using System;
using System.Collections.Generic;
namespace demo {
    class 泛型学习 {
        static void Main1 (string[] args) {
            var accounts = new List<Account> () {
                new Account ("Christian", 15000),
                new Account ("Steohanie", 2200),
                new Account ("Angela", 1200)
            };
            // Accumulate()方法的调用方式如下:
            decimal sumAmmount = Algorithm.AccumulateSimple (accounts);
            // 将Account类型定义为泛型类型参数,就可以调用新的Accumulate方法:
            decimal ammount0 = Algorithm.Accumulate<Account> (accounts);
            // 编译器会从方法的参数类型中自动推断出泛型类型参数,所以以如下方式调用Acc-ulateo
            // 方法是有效的,和上面一句是等效的
            decimal ammount0_1 = Algorithm.Accumulate (accounts);
            // 带委托的泛型方法,需要指定泛型参数的类型,第一个参数accounts集合是IEnumerable<Account>类型
            // 第二个参数使用lambda表达式表示Account和decimal类型的两个参数,返回一个小数,对于每一项使用Accumulate方法调用这个lambda表达式
            decimal ammount1 = Algorithm.Accumulate<Account, decimal> (accounts, (item, sum) => item.Balance);

            // 泛型方法的重载
            var test = new Me_overload ();
            test.Foo (12);
            test.Bar ("44");
            test.Bar (44);

        }

    }
    public class Account : IAccount {
        public string Name { get; private set; }
        public decimal Balance { get; private set; }
        public Account (string name, Decimal balance) {
            this.Name = name;
            this.Balance = balance;
        }

    }
    public interface IAccount {
        // IAccomt接口定义了只读属性Balance和 Name:
        decimal Balance { get; }
        string Name { get; }
    }
    public static class Algorithm {
        // 累加所有Account对象
        public static decimal AccumulateSimple (IEnumerable<Account> source) {
            // foreach语句使用 IEnumerable接口迭代集合的元素,所以AccumulateSimple方法的参数是 IEnummble类
            // 型。forcach语句处理实现IEnumerable接口的每个对象。这样,AccumulateSimple方法就可以用于
            // 所有实现IEnumerable<Account>的集合类。在这个方法的实现代码中,直接访问Account对象的Balance属 性:
            decimal sum = 0;
            foreach (Account a in source) {
                sum += a.Balance;
            }
            return sum;
        }
        //使用泛型方法
        public static decimal Accumulate<TAccount> (IEnumerable<TAccount> source)
        where TAccount : IAccount //泛型类型可以用where子句来限制
        {
            decimal sum = 0;
            foreach (TAccount a in source) {
                sum += a.Balance;
            }
            return sum;
        }
        //带委托的泛型方法
        public static T2 Accumulate<T1, T2> (IEnumerable<T1> source, Func<T1, T2, T2> action) {
            // 泛型类型实现IAccount接 口的要求过于严格。传递一个泛型委托修改Accumulate方法。
            // 这个Accumulate方法使用两个泛型参数T1和T2。第一个参数T1用于实现了IEnumerable参数的集合,
            // 第二个参数使用泛型委托Fun<T1,T2,TResult>其中,第 2个和第3个泛型参数都是T2类型。需要传递的方法有两个输入参数T1和T2)和一个T2类型的返回值:
            T2 sum = default (T2);
            foreach (T1 item in source) {
                sum = action (item, sum);
            }
            return sum;
        }
    }
    public class Me_overload {
        // 泛型方法可以重载,为特定的类型定义规范。这也适用于带泛型参数的方法
        //Foo方法定义了两个版本,第 1个版本接受一个泛型参数,第 2个版本是用于int参数的专用版本。在编译期间,
        // 会使用最佳匹配。如果传递了一个int,就选择带int参数的方法。对于任何其他参数类型,编译器会选择方法的泛型版本:
        public void Foo<T> (T obj) {
            Console.WriteLine ("Foo<T (T obj), obj type:{0}", obj.GetType ().Name);
        }
        public void Foo (int x) {
            Console.WriteLine ("Foo(int x)");
        }
        public void Bar<T> (T obj) {
            Foo (obj);
        }
    }

}