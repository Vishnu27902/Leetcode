import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack=new Stack<>();
        for(char i:s.toCharArray())
        {
            if(i=='{'||i=='['||i=='(')
            stack.push(i);
            else if(stack.isEmpty())
            return false;
            else if(i=='}' && stack.peek()=='{') stack.pop();
            else if(i==']' && stack.peek()=='[') stack.pop();
            else if(i==')' && stack.peek()=='(') stack.pop();
            else return false;
        }
        return stack.isEmpty();
    }
}
