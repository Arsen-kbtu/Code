package p2;

import java.util.Scanner;

public class StarTest {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n=scan.nextInt();
		StarTriangle s =new StarTriangle(n);
		System.out.println(s.toString());
		
	}

}
