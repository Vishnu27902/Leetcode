#include<stack>
#include<cstring>
class Solution {
public:
    bool isValid(string str) {
        if(str.length()%2!=0) return false;
        stack<char> s;
        for(auto i:str)
        {
            if(i=='{'||i=='('||i=='[') s.push(i);
            else if(s.empty()) return false;
            else if(i=='}' && s.top()=='{' ) s.pop();
            else if(i==')' && s.top()=='(' ) s.pop();
            else if(i==']' && s.top()=='[' ) s.pop();
            else return false;
        }
        return s.empty();
    }
};
