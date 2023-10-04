package p2;

public class StarTriangle {
	int x;
	int c=1;
	String s="";
	public StarTriangle(int x) {
		this.x=x;
	}
	public String toString() {
		while(c<=x) {
			for(int i=0; i<c; i++) {
				s+="[*]";			
				}
			c++;
			s+="\n";
		}
	
		return s;
	}
}
