bool rotateString(char * s, char * goal){
    if(strlen(s)!=strlen(goal))return false;
    char str[strlen(s)*2+1];
    strcpy(str,s);
    strcat(str,s);
    return strstr(str,goal)?true:false;
}
