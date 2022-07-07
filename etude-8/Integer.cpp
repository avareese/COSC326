#include <iostream> 
#include <string> 
#include <vector>
#include "Integer.h"
#include <regex>

/** Authors 
 * Ava Reese and Katherine Butt
 * Integer.cpp
 */

namespace cosc326 {

	/* default constructor */
	Integer::Integer() {
		y = "0";
		pos = true;
	}
	/* changes the sign from positive to negative */
	void Integer::swapSign() {
		pos = !(pos);
	}

	std::string Integer::getY() const{
		return y;
	}

	/* returns what the sign of the integer is*/
	bool Integer::sign() const{
		return pos;
	}
	/* copy of constructor*/
	Integer::Integer(const Integer& i) : y(i.getY()), pos(i.pos){}
		
/* this method ensures there are no errors and if there is print an error message */
	Integer::Integer(const std::string& s) {

		bool checkSign = true;
		size_t i = 0;
		std::string string = s;

		if(string.empty()){
			new (this) Integer();
		}

		if(string[0] == '-'){
			pos = false;
			string.erase(0,1);
		} else
			pos = true;

		while(checkSign && !(i==string.size())){
			if(!isdigit(string[i])){
				checkSign = false;
			}
			i++;
		}

		if(!checkSign){
			std::cout << "Could not convert input to an integer\n";
			std::cout << "The integer will be zero\n";
			y = "0";
		} else {
			y = string;
		}
	
	}


	Integer::~Integer() {
	
	}

/* assignment operator */
	Integer& Integer::operator=(const Integer& i) {
		y = i.getY();
		pos = i.sign();
		return *this;
	}
/* unary operator which swaps the sign*/
	Integer Integer::operator-() const {
		Integer result = Integer(*this);
		result.swapSign();
		return result;
	}
/* unary operator which makes sure the sign is + */
	Integer Integer::operator+() const {
		Integer result = Integer(*this);

		if(!result.sign())
			result = -result;
		return result;
	}

/** compound operator which conists of binary opartor and assignment operator this makes
 * sure we use addition operator*/

	Integer& Integer::operator+=(const Integer& i) {
		if((*this > i) && (!pos && i.sign()) || (pos && !i.sign()))
			y = findDiff(y, i.getY());
		else if ((*this < i) && (!pos && i.sign()) || (pos && !i.sign())){
			y = findDiff(i.getY(), y);
			swapSign();
		} else {
			y = findSum(y, i.getY());
		}
		y = getRidOfZeros(y);
		return *this;
	}

/** compound operator which consist of binary operator and assignment operator this makes
 * sure we call right subtraction operator */
	Integer& Integer::operator-=(const Integer& i) {

		if((!pos && i.pos) || (pos && !i.pos))
			y = findSum(y, i.getY());
		else if(*this > i){
			y = findDiff(y, i.getY());
		} else if (*this < i){
			y = findDiff(i.getY(), y);
			swapSign();
		} else {
			y = "0";
			pos = true;
		}
		y = getRidOfZeros(y);
		return *this;
	}

/* compound operator, makes sure we call the right operation for multiplacation */
	Integer& Integer::operator*=(const Integer& i) {

		if((pos && !i.pos) || (!pos && !i.pos)){
			swapSign();
		}
		y = multiply(y, i.getY());
		y = getRidOfZeros(y);
		return *this;
	}

/* compound operator, makes sure we call the right operation for division */
	Integer& Integer::operator/=(const Integer& i) {
		bool boolean = true;
		if((!pos && i.pos) || (pos && !i.pos)){
			boolean = false;
		}
		*this = division(+*this, +i);
		pos = boolean;
		return *this;
	}

/* compound operator, make sure we use the right operator for remainder (similar to division)*/
	Integer& Integer::operator%=(const Integer& i) {
		pos = true;
		*this = remainder(+*this, +i); 
		return *this;
	}

/* binary artithmetic operator, making sure we + */
	Integer operator+(const Integer& lhs, const Integer& rhs) {
		Integer result = Integer(lhs);
		return result+=rhs;
	}

/* binary arthimetic operator, makes sure we subtract */
	Integer operator-(const Integer& lhs, const Integer& rhs) {
		Integer result = Integer(lhs);
		return result-=rhs;
	}
/* binary arthimetic operator, makes sure we mulitply*/
	Integer operator*(const Integer& lhs, const Integer& rhs) {
		Integer result = Integer(lhs);
		return result *=rhs;
	}
/* binary arthmetic operator, makes sures we divide */
	Integer operator/(const Integer& lhs, const Integer& rhs) {
		Integer result = Integer(lhs);
		return result/= rhs;
	}
/* binary arthimetic operator, makes sure we return the remainder */
	Integer operator%(const Integer& lhs, const Integer& rhs) {
		Integer result = Integer(lhs);
		return result%= rhs;
	}

/* output stream for insertion */
	std::ostream& operator<<(std::ostream& os, const Integer& i) {
		if(!i.sign())
			os << '-';
		os << i.getY();
		return os;
	}
/* input stream for extraction */
	std::istream& operator>>(std::istream& is, Integer& i) {
		using namespace std;
		string in;
		cin >> in;
		Integer j = Integer(in);
		i = j;
		return is;
	}
/* if numbers are negative call opposite function for positive numbers */
	bool operator<(const Integer& lhs, const Integer& rhs) {
		int x = lhs.getY().size(), x1 = rhs.getY().size();

		if((lhs.sign() == false) && (rhs.sign() == false))
			return +lhs > +rhs;
		else if ((lhs.sign() == false) && rhs.sign())
			return true;
		else if (lhs.sign() && (rhs.sign() == false))
			return false;
		
		if(x < x1)
			return true;
		if (x1 < x)
			return false;

		for(int i =0; i<x;i++)
			if(lhs.getY()[i]< rhs.getY()[i])
				return true;
			else if (lhs.getY()[i] > rhs.getY()[i])
				return false;

		return false;
		
	}

/* if numbers are negative call opposite function for positive numbers */
	bool operator> (const Integer& lhs, const Integer& rhs) {

		int x = lhs.getY().size(), x1 = rhs.getY().size();

		if((lhs.sign() == false) && (rhs.sign() == false))
			return +lhs < +rhs;
		else if ((lhs.sign() == false) && rhs.sign())
			return false;
		else if (lhs.sign() && !rhs.sign())
			return true;

		if(x > x1)
			return true;
		if(x1 > x)
			return false;

		for(int i =0; i< x;i++)
			if(lhs.getY()[i] > rhs.getY()[i])
				return true;
			else if (lhs.getY()[i] < rhs.getY()[i])
				return false;

		return false;

	}

	bool operator<=(const Integer& lhs, const Integer& rhs) { 
		return !(lhs > rhs);
	}

	bool operator>=(const Integer& lhs, const Integer& rhs) {
		return !(lhs < rhs);	
	}

	bool operator==(const Integer& lhs, const Integer& rhs) { 
		return (lhs.getY() == rhs.getY()) && (lhs.sign() == rhs.sign());
	}

	bool operator!=(const Integer& lhs, const Integer& rhs) { 
		return !(lhs == rhs);
	}

	/**The idea is based on school mathematics. We traverse both strings from end, one by one add digits and keep track of carry. 
	 * To simplify the process, we do following: 
	1) Reverse both strings. 
	2) Keep adding digits one by one from 0’th index (in reversed strings) to end of smaller string,
	append the sum % 10 to end of result and keep track of carry as sum/10. 
	3) Finally reverse the result. 
	* please note: found of geeksforgeeks
	*/
	std::string findSum(std::string str1, std::string str2){
	
		using namespace std; 

    	// Before proceeding further, make sure length
    	// of str2 is larger.

    	if (str1.length() > str2.length())
        	swap(str1, str2);
 
    	// Take an empty string for storing result
    	string str = "";
 
    	// Calculate length of both string
    	int n1 = str1.length(), n2 = str2.length();
 
    	// Reverse both of strings
    	reverse(str1.begin(), str1.end());
    	reverse(str2.begin(), str2.end());
 
    	int carry = 0;
    	for (int i=0; i<n1; i++)
    	{
        	// Do school mathematics, compute sum of
        	// current digits and carry
        	int sum = ((str1[i]-'0')+(str2[i]-'0')+carry);
        	str.push_back(sum%10 + '0');
 
        	// Calculate carry for next step
        	carry = sum/10;
    	}
 
    	// Add remaining digits of larger number
    	for (int i=n1; i<n2; i++)
    	{
        	int sum = ((str2[i]-'0')+carry);
        	str.push_back(sum%10 + '0');
        	carry = sum/10;
    	}
 
    	// Add remaining carry
    	if (carry)
        	str.push_back(carry+'0');
 
    	// reverse resultant string
    	reverse(str.begin(), str.end());
 
    	return str;
	}
/**We traverse both strings from the end, one by one subtract digits. 
* 1.Reverse both strings.
* 2.Keep subtracting digits one by one from 0’th index (in reversed strings) to the end of a smaller string, append the diff if it’s positive to end of the result. If difference(diff) is negative then add 10 and keep track of carry as 1 if it’s positive then carry is 0.
* 3. Finally, reverse the result.
 *  please note: found on geeksforgeeks
 */

	std::string findDiff(std::string str1, std::string str2){

		using namespace std;

		string minus = ""; 

    	if (Integer(str1) < Integer(str2)) {
        	swap(str1, str2);
			minus = "-";
		}
    	// Take an empty string for storing result
    	string str = "";
 
    	// Calculate length of both string
    	int n1 = str1.length(), n2 = str2.length();
 
    	// Reverse both of strings
    	reverse(str1.begin(), str1.end());
    	reverse(str2.begin(), str2.end());
 
    	int carry = 0;

		// Run loop till small string length
    	// and subtract digit of str1 to str2
    	for (int i = 0; i < n2; i++) {
        	// Do school mathematics, compute difference of
        	// current digits
 
        	int sub = ((str1[i] - '0') - (str2[i] - '0') - carry);
 
        	// If subtraction is less then zero
        	// we add then we add 10 into sub and
        	// take carry as 1 for calculating next step
        	if (sub < 0) {
            	sub = sub + 10;
            	carry = 1;
       	 	}
        	else
            	carry = 0;
 
        	str.push_back(sub + '0');
    	}

		// subtract remaining digits of larger number
    	for (int i = n2; i < n1; i++) {
        	int sub = ((str1[i] - '0') - carry);
 
        	// if the sub value is -ve, then make it positive
        	if (sub < 0) {
            	sub = sub + 10;
            	carry = 1;
        	}
        	else
            	carry = 0;
 
        	str.push_back(sub + '0');
    	}
 
    	// reverse resultant string
    	reverse(str.begin(), str.end());
 
    	return minus + str;
	}
 /* We start from last digit of second number multiply it with first number. 
  *Then we multiply second digit of second number with first number, and so on. 
  * We add all these multiplications. While adding, we put i-th multiplication shifted.
  * please note: found on geeksforgeeks
  */
	std::string multiply(std::string num1, std::string num2)
	{
		using namespace std;

		int len1 = num1.size();
    	int len2 = num2.size();
    	if (len1 == 0 || len2 == 0)
    		return "0";
 
    	// will keep the result number in vector
    	// in reverse order
    	vector<int> result(len1 + len2, 0);
 
    	// Below two indexes are used to find positions
    	// in result.
    	int i_n1 = 0;
    	int i_n2 = 0;

		// Go from right to left in num1
    	for (int i=len1-1; i>=0; i--)
    	{
        	int carry = 0;
        	int n1 = num1[i] - '0';

        	i_n2 = 0;
         
        	for (int j=len2-1; j>=0; j--)
        	{
            
            	int n2 = num2[j] - '0';
            	int sum = n1*n2 + result[i_n1 + i_n2] + carry;
 
            	
            	carry = sum/10;
 
            
            	result[i_n1 + i_n2] = sum % 10;
 
            	i_n2++;
        	}
		
        if (carry > 0)
            result[i_n1 + i_n2] += carry;
 
        i_n1++;
   		}	
 
    	// ignore '0's from the right
    	int i = result.size() - 1;
    	while (i>=0 && result[i] == 0)
    	i--;
 
    	// If all were '0's - means either both or
    	// one of num1 or num2 were '0'
    	if (i == -1)
    		return "0";
 
    	// generate the result string
    	string s = "";
     
    	while (i >= 0)
        s += std::to_string(result[i--]);
 
    	return s;
	}
/* greatest common demoniator method which finds the gcd */
	Integer gcd(const Integer& a, const Integer& b) {

		if(a == b)
			return a;
		if(b == Integer("0"))
			return a;

		if(a==b)
			return a;

		if(a>b)
			return gcd(a-b,b);

		return gcd(a, b-a);
	}
 
/** removes the zeros that are padded onto the number*/
	std::string getRidOfZeros(std:: string s){

		const std::regex pattern("^0+(?!$)");

		s = regex_replace(s, pattern, "");
		return s;
	}

		
	/* division method which minuses mulitples of the divisor*/
	Integer division (Integer divided, Integer divisor){

		Integer ten = Integer("10");
		Integer one = Integer("1");
		Integer r = Integer("0");
		Integer currentDivisor;
		size_t length = (divided.getY().size() - divisor.getY().size() +1);
		
		if(divided == divisor)
			return Integer("1");
		if(divisor > divided)
			return divided;

		for(size_t i =0; i<length;i++){
			currentDivisor = divisor;
			int count =0;

			do {
				currentDivisor *=ten;
				count++;
			} while(divided > currentDivisor);
				currentDivisor = Integer(currentDivisor.getY().substr(0, currentDivisor.getY().size()-1));
				count--;
				Integer c = Integer("0");

			while(divided >= currentDivisor){
				c+=one;
				divided-=currentDivisor;
			}

			for(int y =0; y<count;y++)
				c*=ten;

			r+=c;	

		}
		return r;
	}

	/* remainder method which returns the divided to get the remainder*/
	Integer remainder (Integer divided, Integer divisor){

		Integer ten = Integer("10");
		Integer one = Integer("1");
		Integer r = Integer("0");
		Integer currentDivisor;
		size_t length = (divided.getY().size() - divisor.getY().size() +1);
		
		if(divided == divisor)
			return Integer("1");
		if(divisor > divided)
			return divided;

		for(size_t i =0; i<length;i++){
			currentDivisor = divisor;
			int count =0;

			do {
				currentDivisor *=ten;
				count++;
			}while(divided > currentDivisor);
				currentDivisor = Integer(currentDivisor.getY().substr(0, currentDivisor.getY().size()-1));
				count--;
				Integer c = Integer("0");

			while(divided >= currentDivisor){
				c+=one;
				divided-=currentDivisor;
			}

			for(int y =0; y<count;y++)
				c*=ten;

			r+=c;	

		}
		return divided;
	}


}
