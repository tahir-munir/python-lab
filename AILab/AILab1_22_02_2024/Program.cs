using System;

namespace AILab1_22_02_2024
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello World!");
            //Console.WriteLine(args.Length);

            char a = 'G';
            int i = 12;
            short s = 123;
            long l = 1234567;
            float f =  3.44f;
            double d = 3456.67676;
            decimal dm = 123.56m;

            Console.WriteLine(a);
            Console.WriteLine(i);
            Console.WriteLine(s);
            Console.WriteLine(l);
            Console.WriteLine(f);
            Console.WriteLine(d);
            Console.WriteLine(dm);

            string strng = "Greeks";

            strng += "for";
            Console.WriteLine(strng);

            object obj;
            obj = 20;
            Console.WriteLine(obj);
            Console.WriteLine(obj);

            Console.WriteLine(obj.GetType());


            unsafe
            {
                int n = 10;
                int* p = &n;
                Console.WriteLine("Value :{0}",n);
                Console.WriteLine("Adddess  :{0}", (int)p);
            }

            var var1 = 123;
            var var2 = "String";
            var var3 = 123.3f;
            var var4 = 123.3d;
            var var5 = false;


            Console.WriteLine("Type of var1: " + var1.GetType());
            Console.WriteLine("Type of var2: " + var2.GetType());
            Console.WriteLine("Type of var3: " + var3.GetType());
            Console.WriteLine("Type of var4: " + var4.GetType());
            Console.WriteLine("Type of var5: " + var5.GetType());








            var Base = 13;
            var Height = 20;
            var Area = (Base * Height) / 2;

            Console.WriteLine("Height of triangle is: " + Height + "\nBase of the trinagle is: " + Base);
            Console.Write("Area of the triangle is: {0}", Area);

            var names = new[] { "bilal", "sonia", "shah", "Ali" };

            Console.WriteLine("List of author is: ");


            foreach(string data in  names){
                Console.WriteLine(data);
            }



            Calc calculator = new Calc();

            Console.WriteLine("Addition is: " + calculator.add());


        }
    }
}
