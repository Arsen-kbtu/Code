package p3;

public class Time {
	int hour, minute, second;
	public Time(int hour, int minute, int second) {
		this.hour=hour;
		this.minute=minute;
		this.second=second;
		if(this.hour>24 || this.minute>60 || this.second>60) {
			System.out.println("Invalid input");
			System.exit(0);
		}
	}
	public String toUniversal() {
		String s="";
		if(hour<10) {
			s+="0";
		}
		s+=hour+":";
		if(minute<10) {
			s+="0";
		}
		s+=minute+":";
		if(second<10) {
			s+="0";
		}
		s+=second+"\n";
		return s;
	}
	public String toStandart() {
		String s="";
		if(hour<10) {
			s+="0";
		}
		if(hour<=12) {
			s+=hour+":";
		}
		else {
			s+=(hour-12)+":";
		}
		if(minute<10) {
			s+="0";
		}
		s+=minute+":";
		if(second<10) {
			s+="0";
		}
		s+=second;
		if(hour<=12) {
			s+=" AM\n";
		}
		else {
			s+=" PM\n";
		}
		return s;
	}
	public void add(Time obj) {
		this.hour+=obj.hour;
		this.minute+=obj.minute;
		this.second+=obj.second;
		if(this.second>60) {
			this.minute++;
			this.second-=60;
		}
		if(this.minute>60) {
			this.hour++;
			this.minute-=60;
		}
		if(this.hour>24) {
			this.hour-=24;
		}
	}
}
