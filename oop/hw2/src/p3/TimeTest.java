package p3;
import java.util.Scanner;
public class TimeTest {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int H=scan.nextInt(), M=scan.nextInt(), S=scan.nextInt();
		Time t=new Time(H, M, S);
		System.out.println(t.toUniversal());
		System.out.println(t.toStandart());
		
		
	}
}
