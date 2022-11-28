public class MyClass {
    public static void main(String args[]) {
      class A{
          int m = 1;
      }
      class B extends A{
          int m = 2;
      }
      class C extends B{
          int m = 3;
      }
      class D extends B{
          int m = 4;
      }
      class E extends C{
          int m = 5;
      }
      A a = new E();
      B b = (B)a;
      C c = (C)a;
      D d = (D)a;
      E e = (E)a;

      System.out.println(a instanceof A);
      System.out.println(a instanceof B);
      System.out.println(a instanceof C);
      System.out.println(a instanceof D);
      System.out.println(a instanceof E);
    }
}