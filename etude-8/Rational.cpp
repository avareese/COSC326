#include "Rational.h"
#include "Integer.h"
#include <vector>
#include <iostream>
#include <string>
#include <sstream>
#include <regex> 
#include <cstring>

/** @authors Ava Reese and Katherine Butt
 * Rational.cpp
 */

namespace cosc326 {

	/* default constructor that creates Rational with a value of 0*/
	Rational::Rational() {
		(Rational(Integer("0")));

	}
/* numerator*/
	Integer Rational::getI() const{
		return i;
	}
/* denomitator*/
	Integer Rational::getX() const{
		return x;
	}

	

/* constructor string which takes care of proper, improper and mixed fractions*/ 
	Rational::Rational(const std::string& str) {

		using namespace std;


		Integer w, tempI, tempX;
		Integer t = Integer("1");
		vector<string> strVec;
		string s = str;

		if(s.empty()){
			new (this) Rational();
		} else{
			if(s[0] == '+'){
				s.erase(0,1);
			}
			if(str[0] == '-'){
				t = Integer("-1");
				s.erase(0,1);
			}
	

			std::string delm = "."; 
			int temp = -1; 
			temp = s.find(delm);
			if(temp != -1) {
				std::string token = s.substr(0,temp);
				s.erase(0,temp+1);
				strVec.push_back(token); 
			}
			std::string delm2 = "/"; 
			int temp2 = -1; 
			temp2 = s.find(delm2);
			if(temp2 != -1) {
				std::string token2 = s.substr(0,temp2);
				s.erase(0,temp2+1);
				strVec.push_back(token2); 
			}
			strVec.push_back(s);

		}
		// mixed fraction
		if(strVec.size() ==3){
			w = Integer(strVec.at(0))*t;
			tempI = Integer(strVec.at(1))*t;
			tempX = Integer(strVec.at(2));
			new (this) Rational(w, tempI, tempX);
		//proper or imporoper fraction
		} else if(strVec.size()==2){
			tempI = Integer(strVec.at(0))*t;
			tempX = Integer(strVec.at(1));
			new (this) Rational(tempI, tempX);
		//whole number
		} else if (strVec.size()==1){
			new (this) Rational(Integer(strVec.at(0))*t);
		} else{
			std::cerr << " Error" << std::endl;
		}


	}
/* Copy constructor which duplicates the provided rational*/
	Rational::Rational(const Rational& r) : i(Integer(r.getI())), x(Integer(r.getX())) {

	}

	Rational::Rational(const Integer& a) : i(Integer(a)), x(Integer("1")) {

	}
/*This method prevents any rationals being initlised as 0 */
	Rational::Rational(const Integer& a, const Integer& b) {
		if(b == Integer("0")){
			std::cerr << "rational has to have denominator not equal to 0" << std::endl;
			std::cerr << "demoninator is initalised to 1" << std::endl;
			new (this) Rational(a);
		} else{
			i = a;
			x = b;
		}

	}

	Rational::Rational(const Integer& a, const Integer& b, const Integer& c) {
		Rational s = Rational(a);
		Rational t = Rational(b,c);
		*this = s+t; 

	}

	Rational::~Rational() {

	}

/* this method will copy the sign and number */
	Rational& Rational::operator=(const Rational& r) {
		x = r.x;
		i = r.i;
		return *this;
	}
/* unary operator -, changes the sign of rational from + to -*/
	Rational Rational::operator-() const {
		Rational r = Rational(*this);
		r.i = -r.i;
		return r;
	}
/* unary operator +, makes sure the sign of rational is positive */
	Rational Rational::operator+() const {
		Rational r = Rational(*this);

		if(r.i < Integer("0")){
			r.i = -r.i;
		}
		return r;
	}

/* compund assignment operator, uses rational addition and calls simplify */
	Rational& Rational::operator+=(const Rational& r) {

		if(x == r.x) i+=r.getI();
		else{
			i = i*r.getX() + r.getI()*x;
			x *= r.getX();
		}
		simplify();
		return *this;
	}

/* compound assignment operator, uses rational subtraction and then calls simplify */
	Rational& Rational::operator-=(const Rational& r) {

		if(x == r.x) i-=r.getI();
		else{
			i = i*r.getX() - r.getI()*x;
			x *= r.getX();
		}
		simplify();
		return *this;
	}

/* compound assignment operator, uses rational multiplaction then calls simplify */
	Rational& Rational::operator*=(const Rational& r) {
		i*=r.getI();
		x*=r.getX();
		simplify();
		return *this;
	}

/* compound assignment operator, uses rational division then calls simplify */
	Rational& Rational::operator/=(const Rational& r) {
		Rational q = Rational(r.x,r.i);
		*this*=q;
		simplify();
		return *this;
	}

/** simplifies the rational */
	void Rational::simplify(){
		Integer res = Integer();
		if(x.getY() == "0"){
			i = Integer("1");

		} else {
			res = gcd(+x, +i);
			i /= res;
			x /= res;
		}

	}

	/* returns the sign */
	bool Rational::getSign() const {
		return (i.sign() && x.sign() || (!i.sign() && !x.sign()));
	}

	Rational operator+(const Rational& lhs, const Rational& rhs) {
		Rational r = Rational(lhs);
		return r+=rhs;
	}

	Rational operator-(const Rational& lhs, const Rational& rhs) {
		Rational r = Rational(lhs);
		return r-=rhs;
	}

	Rational operator*(const Rational& lhs, const Rational& rhs) {
		Rational r = Rational(lhs);
		return r*=rhs;
	}

	Rational operator/(const Rational& lhs, const Rational& rhs) {
		Rational r = Rational(lhs);
		return r/=rhs;
	}

	std::ostream& operator<<(std::ostream& os, const Rational& i) {

		using namespace std;
		Rational r = i;
		r.simplify();
		Integer tempI = r.getI();
		Integer tempX = r.getX();
		string str = "";



		if(tempI ==Integer("0")){
			os << "0";
			return os;
		}
		if(!i.getSign()){
			str.append("-");
		}

		if(tempX == Integer("1")){
			str.append(tempI.getY());
		} else if (+tempI < +tempX){
			str.append(tempI.getY());
			str.append("/");
			str.append(tempX.getY());
		} else{
			Integer w = Integer(tempI % tempX);
			w = (+tempI - +w)/+tempX;
			Integer t = Integer(+tempI-((+w*+tempX)));
			if(t == Integer("0")){
				str.append(w.getY());
			} else{
				str.append(w.getY());
				str.append(".");
				str.append(t.getY());
				str.append("/");
				str.append(tempX.getY());
			}

		}
		os << str;
		return os;
	}
	std::istream& operator>>(std::istream& is, Rational& i) {
		using namespace std;

		string str;
		is >> str;
		i = Rational(str);
		return is;
	}

	bool operator<(const Rational& lhs, const Rational& rhs) {
		if(lhs.getSign() == false && rhs.getSign()==true)
			return true;
		if(lhs.getSign() == true && rhs.getSign() == false)
			return false;
		if(lhs.getSign() == false && rhs.getSign()==false)
			return +lhs.getI()*+rhs.getX() > +lhs.getX()*+rhs.getI();
		
		return lhs.getI()*rhs.getX() > lhs.getX()*rhs.getI();

	}

	bool operator> (const Rational& lhs, const Rational& rhs) {
		if(lhs.getSign() == false && rhs.getSign()==true)
			return false;
		if(lhs.getSign() == true && rhs.getSign() == false)
			return true;
		if(lhs.getSign() == false && rhs.getSign()==false)
			return +lhs.getI()*+rhs.getX() < +lhs.getX()*+rhs.getI();
		
		return lhs.getI()*rhs.getX() > lhs.getX()*rhs.getI();
	}

	bool operator<=(const Rational& lhs, const Rational& rhs) {
		return !(lhs > rhs);
	}

	bool operator>=(const Rational& lhs, const Rational& rhs) {
		return !(lhs < rhs);
	}

	bool operator==(const Rational& lhs, const Rational& rhs) {
		return (lhs.getI()*rhs.getX() == lhs.getX()*rhs.getI()) && (lhs.getSign() == rhs.getSign());
	}

	bool operator!=(const Rational& lhs, const Rational& rhs) {
		return !(lhs==rhs);
	}

}
