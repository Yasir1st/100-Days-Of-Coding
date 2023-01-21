
package trialJava;
import java.util.Scanner;

public class trial {
    public static void main(String[] args) {
        Scanner cs = new Scanner(System.in);
        System.out.println("A :");
        int a = cs.nextInt();
        System.out.println("B :");
        int b = cs.nextInt();
        System.out.println("C :");
        int c = cs.nextInt();
        System.out.println("D :");
        int d = cs.nextInt();
        System.out.println("E:");
        int e = cs.nextInt();

        int x[] = new int[5];
        x[0] = a;
        x[1] = b;
        x[2] = c;
        x[3] = d;
        x[4] = e;

        int min = x[0];
        int max = x[0];
        for (int i = 0; i < x.length; i++) {
            if (min > x[i]) {

            } else {
                max = x[1];
            }
        }
        System.out.println("min : " + min);
        System.out.println("max : " + max);
    }
    public static void space(){
        System.out.println("=======================================");
        return;
    }
}
