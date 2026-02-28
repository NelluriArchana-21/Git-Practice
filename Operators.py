#Arithmetic Operators -> (+,_,*,/,//,%,**) -> Used for Arithematic Calculations
a,b=20,10
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b, sep='\n')

#Relational Operators -> (==,!=,>,<,>=,<=) -> Used for comparing values -> o/p: Boolean
a,b=10,10
print(a==b,a!=b,a>b,a<b,a>=b,a<=b,sep='\n')

#Assignment Operators -> (=,+=,-+,*=,/=,//=,%=,**=) -> Used to assign after performing action 

#Logical Operators -> (and,or,not) -> used with boolean values -> o/p:boolean
print(True and True, False or False, not True,sep='\n')

#Identity Operators -> (is, not is) -> Compare obj reference
a,b='Hellooo',"Hi"
print(a is b, a is not b,sep='\n')

#Membership operators -> (in,not in) -> used to check the presence of an object
a='ArchanaNelluri'
print('A' in a, 'X' not in a, sep='\n')

#Bitwise Operators -> (&,|,^,~,>>,<<) -> Used on binary numbers
a,b=2,8
print(a&b,a|b,a^b,~a,a>>b,a<<b,sep='\n')