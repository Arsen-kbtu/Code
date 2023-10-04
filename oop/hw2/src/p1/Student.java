package p1;

public class Student {
	public String name;
	String id;
	int yearOfStudy;
	public double grade;
	public void getName() {
		System.out.println(name);
	}
	public void getId() {
		System.out.println(id);
	}
	public void incrementYear() {
		yearOfStudy++;
	}
	public Student(String name,  double grade) {
		
		this.name=name;
		this.grade=grade;
	}
	public Student(String name) {
		this();
		this.name=name;
		
	}
	public Student(String name,  String id, int yearOfStudy) {
		this.id=id;
		this.name=name;
		this.yearOfStudy=yearOfStudy;
	}
	public Student() {
		id="0";
		name="N/A";
		yearOfStudy=-1;
		
	}
	
	public double getGrade() {
		return grade;
	}
	public String toString() {
		return "Student's name is: "+name+"\n"+"Student's id is: "+id+"\n"+"Student's year of study is: "+yearOfStudy+"\n" ;
	}
}

