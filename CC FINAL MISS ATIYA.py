import re
tokenization=[]
class Token:
    def __init__(self, token_type, lexeme,check,line):
        self.token_type = token_type
        self.value_part = lexeme
        self.check=check
        self.line=line
        

class KeywordToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class ObjectCallToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("OBJECT CALL", lexeme,True,line)
class IdentifierToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("IDENTIFIER", lexeme,True,line)
class LexicalToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("LEXICAL ERROR", lexeme,False,line)        
class IntConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("INT CONSTANT", lexeme,True,line) 
class FloatConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("FLOAT CONSTANT", lexeme,True,line) 
class StringConstantToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("STRING CONSTANT", lexeme,True,line) 
class BooleanToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("BOOLEAN CONSTANT", lexeme,True,line) 
'''class PunctureToken(Token):
    def __init__(self, token_type,lexeme):
        super().__init__(token_type, lexeme,True) '''
class PunctureToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class OperatorToken(Token):
    def __init__(self, token_type,lexeme,line):
        super().__init__(token_type, lexeme,True,line)
class DataTypeToken(Token):
    def __init__(self, lexeme,line):
        super().__init__("DATA TYPE", lexeme,True,line)                 


class checker:
    def __init__(self):
        pass
    def isDataType(self,word,line):
        DT=['int','float','string','bool'] 
        if word in DT:
            return(DataTypeToken(word,line))
        else:
            return(LexicalToken(word,line))
    def isOB_CALL(self, word,line):
        match = re.match(r'[_A-Za-z]+[_0-9A-Za-z]*(\.[_A-Za-z]+[_0-9A-Za-z]*)*$', word)
        if match:
            iden=match.group()
            return(ObjectCallToken(iden,line))
        else:
            return(LexicalToken(word,line))       
    def isID(self, word,line):
        match = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word)
        if match:
            iden=match.group()
            return(IdentifierToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isINT(self,word,line):
        match=re.match(r'^[+|-]?[0-9]+$',word)
        if match:
            iden=match.group()
            return(IntConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isFLOAT(self,word,line):
        match=re.match(r'^[+|-]?([0-9]+\.([0-9]*)?|(\.[0-9]+))$',word)
        if match:
            iden=match.group()
            return(FloatConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))   
    def isSTRING(self,word,line):
        match=re.match(r"^(['\"])(.*?)(?<!\\)\1$",word)
        if match:
            iden=match.group()
            return(StringConstantToken(iden,line))
        else:
            return(LexicalToken(word,line))
    def isBOOLEAN(self,word,line):
        match=re.match(r"^(True|False)$" ,word)
        if match:
            iden=match.group()
            return(BooleanToken(iden,line))
        else:
            return(LexicalToken(word,line))  
    def isKEYWORD(self,word,line):
        key=['self','staticmethod','virtual','override','new','and','or','class','len','def','if','elif','else','break','continue','pass','for','not','return','is','in','while','import','from','try','exception','as','range','except','finally','print','__init__'] 
        if word in key:
            return(KeywordToken(word.upper(),word,line))
        else:
            return(LexicalToken(word,line))   
    def isPUNCT(self,word,line):
        punct=['(',')','{','}','[',']',',',';',':','.'] 
        if word in punct:
            return(PunctureToken(word,word,line))
        else:
            return(LexicalToken(word,line))
    def isOPER(self,word,line):
        oper=['++','--','&','|','**','*','/','+','-','<','>','<=','>=','!=','==','=','+=','-=','*=','/=']
        if word in oper:
            if (word=='++') or (word=='--'):
                return(OperatorToken(word,word,line))
            if(word=='+=') or (word=='-=') or (word=='*=') or (word=='/='):
                return(OperatorToken(word,word,line))
            if(word=='&') or (word=='|') :
                return(OperatorToken(word,word,line))
            if (word=='**'):
                return(OperatorToken(word,word,line)) 
            if (word=='='):
                return(OperatorToken(word,word,line))
            if (word=='*') or (word=='/'):
                return(OperatorToken(word,word,line))
            if (word=='+') or (word=='-'):
                return(OperatorToken(word,word,line)) 
            if (word=='<') or (word=='>') or (word=='<=') or (word=='>=') or (word=='!=') or (word=='=='):
                return(OperatorToken(word,word,line))
        else:
            return(LexicalToken(word,line))      

'''c=checker()
res=c.isID('2xyz')
res1=c.isINT('-788')
res2=c.isFLOAT('-.5')
res3=c.isSTRING('"ehfwfwfwhf/.wfe/\wfef''%32737$"')
res4=c.isBOOLEAN('True')
res5=c.isKEYWORD('for')
res6=c.isPUNCT('}')
res7=c.isOPER('>=')
print(res.token_type,res.value_part,res1.token_type,res1.value_part,res2.token_type,res2.value_part,res3.token_type,res3.value_part,res4.token_type,res4.value_part,res5.token_type,res5.value_part,res6.token_type,res6.value_part,res7.token_type,res7.value_part)'''
class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.position = 0
        self.tokens = []
        self.temp=''
        self.quote=[]
        self.punct=['(',')','{','}','[',']',',',';',':']
        self.line_number = 1  # Initialize line number
        self.line_check=False
        self.comments=[]

    def scan(self):
        self.line_check=False
        while self.position < len(self.input_text):
            self.line_check=False
            if (self.input_text[self.position] !='"') and len(self.quote)<=0:
                if (self.input_text[self.position] != ' ') and (self.input_text[self.position] != '\n'):
                    if(self.input_text[self.position] in self.punct):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                            #print('pun',self.line_number,self.input_text[self.position])
                            if (self.position+1==len(self.input_text)):
                                break
                            #if (self.input_text[self.position+1] == '\n'):
                                #print('pun',self.line_number,self.input_text[self.position-1])
                             #   self.line_number=self.line_number+1
                              #  self.line_check=True
                            
                    if(self.input_text[self.position] =='='):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='+'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='-'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = '' 
                    if(self.input_text[self.position] =='*'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='/'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''        
                    if(self.input_text[self.position] =='<'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='>'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='!'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    if(self.input_text[self.position] =='&'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = '' 
                    if(self.input_text[self.position] =='|'):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''                                
                    match2=re.fullmatch(r'\.',self.temp)
                    if match2:
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                    
                    self.temp = self.temp + self.input_text[self.position]
                    #print(self.temp,self.input_text[self.position])
                    self.position = self.position + 1
                    
                    if(self.position==len(self.input_text)):
                        break
                    if(self.input_text[self.position]=='.'):
                        #print(self.temp,'.')
                        match=re.fullmatch(r'[0-9]*',self.temp)
                        match1=re.fullmatch(r'[a-zA-Z]*',self.temp)
                        if match1:
                            #print(self.temp,'m1')
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                        if match:
                            #print(self.temp,'m2')
                            self.temp=self.temp+self.input_text[self.position]
                            self.position=self.position+1
                            while(re.match(r'[0-9]',self.input_text[self.position])):
                                #print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                self.temp=self.temp+self.input_text[self.position]
                                self.position=self.position+1
                                if (self.position==len(self.input_text)):
                                    break
                            else:
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = '' 
                        else:
                            if self.temp=='':
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = ''
                                self.temp=self.temp+self.input_text[self.position]
                                self.position=self.position+1
                                while(re.match(r'[0-9]',self.input_text[self.position])):
                                    #print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                    self.temp=self.temp+self.input_text[self.position]
                                    self.position=self.position+1
                                    if (self.position==len(self.input_text)):
                                        break              
                    '''if(self.input_text[self.position]=='.'):
                        match=re.match(r'[_A-Za-z]+[_0-9A-Za-z]*(\.[_A-Za-z]+[_0-9A-Za-z]*)$',self.temp)
                        print(self.input_text[self.position],self.temp)
                        if match is not None:
                            self.temp=self.temp+self.input_text[self.position]
                            self.position=self.position+1
                            #print(self.input_text[self.position])
                            while(re.match(r'[_A-Za-z0-9]',self.input_text[self.position])):
                                print('while self position',self.position,self.input_text[self.position],len(self.input_text))
                                if(self.input_text[self.position-1]=='.'):
                                    if(re.match(r'[0-9]',self.input_text[self.position])):
                                        if self.temp:  # Check if temp is not empty before appending
                                            self.tokens.append(self.temp)
                                            self.tokens.append(self.line_number)
                                            self.temp = ''
                                    else:
                                        print(self.temp[-1],' .')
                                        self.temp=self.temp+self.input_text[self.position]
                                        self.position=self.position+1
                                        if (self.position==len(self.input_text)):
                                            break       
                                else:
                                    print(self.temp[-1])
                                    self.temp=self.temp+self.input_text[self.position]
                                    self.position=self.position+1
                                    if (self.position==len(self.input_text)):
                                        break  
                            else:
                                if self.temp:  # Check if temp is not empty before appending
                                    self.tokens.append(self.temp)
                                    self.tokens.append(self.line_number)
                                    self.temp = '''
                    if(self.temp in self.punct):
                        if self.temp:  # Check if temp is not empty before appending
                            self.tokens.append(self.temp)
                            #print('down punc',self.line_number,self.input_text[self.position])    
                            self.temp = ''
                            '''if (self.input_text[self.position+1] == '\n'):
                                #print('down punc 1',self.line_number,self.input_text[self.position+1])
                                self.line_number=self.line_number+1
                                self.line_check=True
                                #print('temp',self.temp)'''
                            if (self.input_text[self.position] == '\n'):
                                #print('down punc 1',self.line_number,self.input_text[self.position+1])
                                self.line_number=self.line_number+1
                                self.line_check=True
                                #print('temp',self.temp)    
                            #self.tokens.append(self.line_number-1)    
                            if self.line_check:
                                self.tokens.append(self.line_number-1)
                            else:
                                self.tokens.append(self.line_number)   
                            
                    if(self.temp=='='):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='/'):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1            
                    if(self.temp=='+'):
                        if(self.input_text[self.position] =='+') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1 
        
                    if(self.temp=='-'):
                        if(self.input_text[self.position] =='-') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending``
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='*'):
                        if(self.input_text[self.position] =='*') or (self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1  
                    if(self.temp=='<'):
                        if(self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='>'):
                        if(self.input_text[self.position]=='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                        else:
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1  
                    if(self.temp=='!'):
                        if(self.input_text[self.position] =='='):
                            self.temp = self.temp + self.input_text[self.position]
                            self.position = self.position + 1
                            if self.temp:  # Check if temp is not empty before appending
                                self.tokens.append(self.temp)
                                self.tokens.append(self.line_number)
                                self.temp = ''
                                if (self.input_text[self.position] == '\n'):
                                    self.line_number =self.line_number+ 1
                    if(self.temp=='&'):
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp=''
                            if (self.input_text[self.position] == '\n'):
                                self.line_number =self.line_number+ 1
                    if(self.temp=='|'):
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp=''
                            if (self.input_text[self.position] == '\n'):
                                self.line_number =self.line_number+ 1                                                                  
                                                                      
                else:
                    if self.temp:  # Check if temp is not empty before appending
                        self.tokens.append(self.temp)
                        self.tokens.append(self.line_number)
                        self.temp = ''
                        if (self.input_text[self.position] == '\n'):
                            #print(self.line_number,self.input_text[self.position-1])
                            self.line_number =self.line_number+ 1
                            
                    self.position = self.position + 1        
                # print(self.position,self.input_text[self.position])
            else:
                #  print('else ',self.position)
                if (self.input_text[self.position] !='"'):
                    if(self.input_text[self.position] == "\\"):
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                    else:    
                        self.temp = self.temp + self.input_text[self.position]
                        self.position = self.position + 1
                else:                                
                    self.temp = self.temp + self.input_text[self.position]
                
                    if(len(self.quote)>0):
                        self.quote.pop()
                        if self.temp:
                            self.tokens.append(self.temp)
                            self.tokens.append(self.line_number)
                            self.temp = ''
                        if (self.input_text[self.position+1] == '\n'):
                            #print(self.line_number,self.input_text[self.position-1])
                            self.line_number =self.line_number+ 1
                    else:
                        self.quote.append(self.input_text[self.position])
                    self.position=self.position+1
             
            
                 

        # Append the last word after the loop
        if self.temp:
            self.tokens.append(self.temp)
            self.tokens.append(self.line_number)
            self.temp = ''

        #print(self.tokens, self.position, self.input_text)

        return self.tokens

def switch_case(case,line):
    check=checker()
    toke=[]
    if (re.match(r'_|[a-zA-Z]',case[0])) :
        dt=check.isDataType(case,line)
        id=check.isID(case,line)
        ky=check.isKEYWORD(case,line)
        ob=check.isOB_CALL(case,line)
        if(id.check==True)and(ky.check==True):
            toke.append(ky.token_type)
            toke.append(ky.value_part)
            toke.append(ky.line)
            return toke
        
        elif(id.check==True)and(dt.check==True):
            toke.append(dt.token_type)
            toke.append(dt.value_part)
            toke.append(dt.line)
            return toke
        
        else:
            bol=check.isBOOLEAN(case,line)
            if(bol.check==True):
                toke.append(bol.token_type)
                toke.append(bol.value_part)
                toke.append(bol.line)
                return toke
            elif(id.check==True):
                toke.append(id.token_type)
                toke.append(id.value_part)
                toke.append(id.line)
                return toke
            else:
                toke.append(ob.token_type)
                toke.append(ob.value_part)
                toke.append(ob.line)
                return toke
            
    elif case[0]=='"' or case[0]=="'":
        string=check.isSTRING(case,line)
        toke.append(string.token_type)
        toke.append(string.value_part)
        toke.append(string.line)
        return toke
    elif (case[0] == '+') or (case[0]=='-') or (case[0]=='&') or (case[0]=='|') or (case[0]=='*') or (case[0]=='/') or (case[0]=='<') or (case[0]=='>') or (case[0]=='!') or (case[0]=='='):
        oper=check.isOPER(case,line)
        toke.append(oper.token_type)
        toke.append(oper.value_part)
        toke.append(oper.line)
        return toke
    elif (case[0] == '(') or (case[0]==')') or (case[0]=='{') or (case[0]=='}') or (case[0]=='[') or (case[0]==']') or (case[0]==':') or (case[0]==';') or (case[0]==',') or(case[0]=='.') :
        punct=check.isPUNCT(case,line)
        toke.append(punct.token_type)
        toke.append(punct.value_part)
        toke.append(punct.line)
        return toke
    elif (re.match(r'.|[0-9]',case[0])):
        integ=check.isINT(case,line)
        flt=check.isFLOAT(case,line)
        if(integ.check==True) or (flt.check==True):
            if(integ.check==True):
                toke.append(integ.token_type)
                toke.append(integ.value_part)
                toke.append(integ.line)
                return toke
            else:
                toke.append(flt.token_type)
                toke.append(flt.value_part)
                toke.append(flt.line)
                return toke
        else:
            toke.append(integ.token_type)
            toke.append(integ.value_part)
            toke.append(integ.line)
            return toke
     
    else:
        return (LexicalToken(case,line))



input_code = open(r"C:\Users\hpint\Downloads\practice.py",'r')
lexer = Lexer(input_code.read())
tokens = lexer.scan()
#print(tokens)
for i in range(0,len(tokens),2): 
    #print(tokens[i+1],tokens[i],len(tokens))
    val=switch_case(tokens[i],tokens[i+1])
    #val[1]=val[1]+"#"
    #print(val)
    tokenization.append(val)
    
print(tokenization,type (tokenization))   
with open("list.txt", "w") as my_file:
    for item in tokenization:
        line = " ".join(map(str, item)) + "\n"
        my_file.write(line)

count=0
def DEC(types):
    global count
    if(val[count][0]=='IDENTIFIER'):
        name=val[count][1]
        if(ccr=='global'):
            scope.scope_insert(name,types,stack.top())
        else:
            member.mem_insert(name,types)
        #print(val[count][1])
        count+=1
        if(INIT(types)):
            return True
        
    return False

def INIT(types):
    global count
    if(val[count][0]==';'):
        return True
    elif(val[count][0]=='='):
        count+=1
        #print("checking")
        if(F_3(types)):
            #print("hello")
            return True

    return False

def F_3(types):
    global count
    
    if(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        right_type=val[count][0].split()[0].lower()
        #print("checking",val[count][0],right_type,types)
        if(types!=right_type):
            #print(val[count][0],right_type,types)
            raise Exception(f"Type mismatch in assignment for variable '{val[count-2][1]}' at line '{val[count-2][2]}'") 
        count+=1
        if(IDTR(types)):
            #print(val[count][0],right_type,types)
            return True
    elif(val[count][0]=='IDENTIFIER'):
        if (val[count+1][1]==';'):
            name=val[count][1]
            if(ccr=='global'):
                right_type=scope.scope_lookup(name)
            else:
                member.mem_lookup(name)  
            
        else:
            name=val[count][1]
            if(ccr=='global'):
                scope.scope_insert(name,types,stack.top())
            else:
                member.mem_insert(name,types)
        count+=1
        if(INIT(types)):
            return True

    return False

def IDTR(types):
    global count
   
    if(val[count][0]==';'):
        return True
    elif(val[count][0]==','):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            name=val[count][1]
            if(ccr=='global'):
                scope.scope_insert(name,types,stack.top())
            else:
                member.mem_insert(name,types)
            count+=1
            if(INIT(types)):
                return True
    
    return False    

def LIST():
    global count
    if(val[count][0]=='['):
        count+=1
        if(VALUES()):
            if(val[count][0]==']'):
                #print('dic mul',val[count][0])
                return True

    return False

def VALUES():
    global count
    #print(val[count][0])
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='!')  or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT') :#null remove
        #print(val[count][0])
        if(expression()):
            #print(val[count][0],',')
            if(MUL_VAL()):
                return True
    elif(val[count][0]=='{') :        
        if(DICTIONARY()):
            count+=1
            if(MUL_VAL()):
                #print('dic mul',val[count][0])
                return True
    elif(val[count][0]=='['):          
        if(LIST()):
            count+=1
            if(MUL_VAL()):
                return True
    elif(val[count][0]==']'):
        #print('nll check')
        return True

    return False 

def MUL_VAL():
    global count
    if(val[count][0]==','):
        count+=1
        if(F_2()):
            return True 
    elif(val[count][0]==']'):
        return True
    
    return False

def F_2():
    global count
    #print('f2',val[count][0])
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='!') or(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT')  :
        if(expression()):
            #print(val[count][0],'f_2')
            if(MUL_VAL()):
                return True
    if(val[count][0]=='{'):
        #print(val[count][0],'f_2 dic')        
        if(DICTIONARY()):
            count+=1
            #print(val[count][0],'f_2 dic')
            if(MUL_VAL()):
                return True
    if(val[count][0]=='['):        
        if(LIST()):
            count+=1
            #print(val[count][0],'f_2 list')
            if(MUL_VAL()):
                return True

    return False

def DICTIONARY():
    global count
    #print(val[count][0],'dic')
    if(val[count][0]=='{'):
        count+=1
        if(KVP()):
            if(val[count][0]=='}'):
                return True
            
    return False        

def KVP():
    global count
    if(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        if(KEYS()):
            count+=1
            if(val[count][0]==':'):
                count+=1
                if(KVALUES()):
                    count+=1
                    if(MD()):
                        return True
    elif(val[count][0]=='}'):
        return True

    return False

def MD():
    global count
    if(val[count][0]==','):
        count+=1
        if(KEYS()):
            count+=1
            if(val[count][0]==':'):
                count+=1
                if(KVALUES()):
                    count+=1
                    if(MD()):
                        return True
    elif(val[count][0]=='}'):
        return True 

    return False

def KEYS():
    global count
    if(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        return True

    return False

def KVALUES():
    global count
    if(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT') :
        return True
    if (val[count][0]=='['):
        if(LIST()):
            return True 
        
    return False    
            
def INC_DEC(name):
    global count
    l_ty=scope.scope_lookup(name)
    if(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/='):
        operator=INDE()
        if(operator!=False):
            #print(l_ty,operator)
            count+=1
            if((val[count][0]=='INT CONSTANT') or (val[count][0]=='FLOAT CONSTANT')):
                
                r_ty=val[count][0].split()[0].lower()
                re_ty=compatibility.binary_comp(l_ty,r_ty,operator)
                #print(l_ty,r_ty,operator,re_ty)
                count+=1
                return re_ty

    return False

'''def AD():
    global count
    if(val[count][0]=='.'):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            return True
    elif(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/='):
        return True  '''

def INDE():
    global count
    if(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/='):
       return val[count][0]
    
    return False
        
def FUNC_DEF(types):
    global count
    global li_n
    global li_t
    #print(val[count][0])
    if(val[count][0]=='DEF'):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            name=val[count][1]
            count+=1
            #print(val[count][0],'hiiiiii')
            if(val[count][0]=='('):
                count+=1
                #print(val[count][0],'hiiiiii')
                if(PARAM()):
                    #print(val[count][0],'hiiiiii')
                    if(val[count][0]==')'):
                        para_li=li_t
                        para_li.append(types)
                        #print(val[count][0],'hiiiiii',para_li,ccr)
                        if (ccr=='global'):
                            #print(val[count][0],'hiiiiii',para_li,ccr,stack.top())
                            scope.scope_insert(name,para_li,stack.top())
                        else:
                            member.mem_insert(name,para_li)    
                        count+=1
                        if(BODY()):
                            return True

    return False                    

def PARAM():
    global count
    global li_n
    global li_t
    li_t=[]
    li_n=[]
    if(val[count][0]=='DATA TYPE'):
        li_t.append(val[count][1])
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            li_n.append(val[count][1])
            count+=1
            if(F_1()):
                return True
            #return True
    elif(val[count][0]==')'):
        return True
    return False

def F_1():
    global count
    global li_n
    global li_t
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='DATA TYPE'):
            li_t.append(val[count][1])
            count+=1
            if(val[count][0]=='IDENTIFIER'):
                li_n.append(val[count][1])
                count+=1
                if(F_1()):
                    return True
                return True
    elif(val[count][0]==')'):
        return True

    return False

def FUNC_CALL(name): 
    global count
    #print(val[count][0])
    #print(val[count][0])
    if(val[count][0]=='('):
        count+=1
                #print(val[count][0])
        ty=expression()        
        if(ty!=False):
                    #p#rint(val[count][0],';')
            if(val[count][0]==')'):
                re_t=scope.Fun_scope_lookup(name,ty)
                count+=1
                        #print(val[count][0])
                if(val[count][0]==';'):
                    return re_t

    return False

def AE():
    global count
    if val[count][0] == '.':
        count += 1
        if val[count][0] == 'IDENTIFIER':
            count += 1
            if AE():
               return True
            return True
    # elif val[count][0] == '(':
    #     if(FUNC_CALL()):
    #         return True
    # elif val[count][0] == '=':
    #     if(Assignment()):
    #         return True
    return False                                   

def EXCEPTIION_HANDLING():
    global count
    if(val[count][0]=='TRY'):
        count+=1
        if(BODY()):
            count+=1
            if(EXCEPT()):
                return True

    return False

def EXCEPT():
    global count
    if(val[count][0]=='FINALLY') :
        count+=1 
        if(BODY()):
            return True
    elif(val[count][0]=='EXCEPT'):
        count+=1
        if(A_NAME()):
            if(BODY()):
                count+=1
                if(F_12()):
                    return True

    return False

def F_12():
    global count
    if(val[count][0]=='FINALLY'):
        count+=1
        if(BODY()):
            return True
    return False

def A_NAME():
    global count
    if(val[count][0]=='EXCEPTION'):#null
        count+=1
        if (val[count][0]=='AS'):
            count+=1
            if (val[count][0]=='IDENTIFIER'):
                count+=1
                return True
    elif val[count][0] in ['{',';','DATA TYPE','IDENTIFIER','FOR','TRY',]:
        return True
        
    return False

def FOR_LOOP():
    global count
    if(val[count][0]=='FOR'):
        #print(val[count][0],'in')
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            count+=1
            if(val[count][0]=='IN') :
                count+=1
                if(RANGE()):
                    #print('for true',val[count][0])
                    if(BODY()):
                        #print('for true')
                        return True

    return False                

def RANGE():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        if(expression()):
            #print(val[count][0],'is')
            return True
    elif(val[count][0]=='RANGE'):
        count+=1   
        if(val[count][0]=='('):
            count+=1
            if(ITERABLE()):
                if(val[count][0]==')'):
                    count+=1
                    #print(val[count][0],'is2')
                    return True
                
    return False

def ITERABLE():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        if(expression()):
           # print(val[count][0],'iter')
            return True
    elif(val[count][0]=='LEN'):
        count+=1
        if(val[count][0]=='('):
            count+=1
            if(val[count][0]=='INT CONSTANT') or (val[count][0]=='IDENTIFIER') :
                count+=1
                if(val[count][0]==')'):
                    count+=1
                    return True

    return False            

def CONSTANT():
    global count
    if(val[count][0]=='INT CONSTANT'):
        count+=1
        if(CONST()):
            return True 
    elif(val[count][0]=='STRING CONSTANT'):
        count+=1
        if(CONST()):
            return True 
    elif(val[count][0]=='FLOAT CONSTANT'):
        count+=1
        if(CONST()):
            return True  
    elif(val[count][0]=='BOOLEAN CONSTANT'):
        count+=1
        if(CONST()):
            return True

    return False

def CONST():
    global count
    if(val[count][0]==','):
        count+=1
        if(CONST()):
            return True
    elif():#null

     return False                    


def if_else():
    global count 
    if(val[count][0]=='IF'):
        #print('in if')
        count+=1
        if (val[count][0]=='('):
            count+=1
            #print(val[count][0])
            if (expression()):
                #print(val[count][0],'f')
                if(val[count][0]==')'):
                    count+=1
                    #print(val[count][0])
                    if(BODY()):
                        try:
                            if val[count+1][0] in ['ELSE','ELIF']:
                                count+=1
                        except IndexError:
                            return True
                        #print('true if elif before')
                        if(elif_()):
                            #print('true if elif')
                            return True 
                    return True
    return False                        

def elif_():    
    global count 
    #print(val[count][0])
    if(val[count][0]=='ELSE'):
        count+=1
        #print(val[count][0])
        if(BODY()):
            return True
    elif(val[count][0]=='ELIF'):
        count+=1
        if (val[count][0]=='('):
            count+=1
            if (expression()):
                if(val[count][0]==')'):
                    count+=1
                    if(BODY()):
                        try:
                            if val[count+1][0] in ['ELSE','ELIF']:
                                count+=1
                        except IndexError:
                            return True 
                        if(elif_()):
                            return True
    elif val[count][0] in ['}','FINALLY','EXCEPT','ELSE','ELIF']:#follow det to remove  null   
        return True
    
           
    return False
   
def expression():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'): 
        #print('check for A')
        le_t=A()
        if(le_t!=False):
            #print('a')
            operator=E1(le_t)
            if(operator!=False):
                return operator
    elif val[count][0] in [',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:
        return True#operator        
          
    return False

def E1(types):
    global count
    if(val[count][0]=='|'):
        operator=val[count][1]
        count+=1
        le_t=A()
        if(le_t!=False):
            re_type=compatibility.binary_comp(types,le_t,operator)
            operators=E1(re_type)
            if(operators!=False):
                return operators
    elif val[count][0] in [',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:
        return types

    return False

def A():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):#or()null:
        #print('check B')
        lf_ty=B()
        #print(lf_ty,'e14')
        if(lf_ty!=False):
            operator=A1(lf_ty)
            if(operator!=False):
                #print('yesq')
                #print(operator,'e14')
                return operator
            
    return False

def A1(types):
    global count
    if(val[count][0]=='&'):
        operator=val[count][1]
        count+=1
        le_t=B()
        if(le_t!=False):
            re_ty=compatibility.binary_comp(types,le_t,operator)
            operators=A1(re_ty)
            if(operators!=False):
                return operators
    elif val[count][0] in ['|',',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:
        return types

    return False

def B():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        #print('check c')
        le_ty=C()
        #print(le_ty,'e3')
        if(le_ty!=False):
            operator=B1(le_ty)
            if(operator!=False):
                return operator

    return False    

def B1(types):
    global count
    if(val[count][0]=='<') or (val[count][0]=='>') or (val[count][0]=='<=') or (val[count][0]=='>=') or (val[count][0]=='!=') or (val[count][0]=='%=') or (val[count][0]=='=='):
        #print(val[count][0])
        operator=RO()
        if(operator!=False):
            le_t=C()
            if(le_t!=False):
                re_ty=compatibility.binary_comp(types,le_t,operator)
                operators=B1(re_ty)
                if(operators!=False):
                    return operators
    elif val[count][0] in ['&','|',',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:               
        return types
    
    return False

def RO():
    global count
    if(val[count][0]=='<') or (val[count][0]=='>') or (val[count][0]=='<=') or (val[count][0]=='>=') or (val[count][0]=='!=') or (val[count][0]=='%=')or (val[count][0]=='=='):
        operator=val[count][1]
        count+=1
        return operator
    
    return False

def C():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        #print('check D')
        le_ty=D()
        #print(le_ty,'e2')
        if(le_ty!=False):
            operator=C1(le_ty)
            #print(operator,'e1')
            if(operator!=False):
                return operator
    
    return False

def C1(types):
    global count
    if(val[count][0]=='+') or (val[count][0]=='-'):
        #print('c1 +')
        operator=PM()
        if(operator!=False):
            le_t=D()
            if(le_t!=False):
                re_ty=compatibility.binary_comp(types,le_t,operator)
                operators=C1(re_ty)
                if(operators!=False):
                    return operators
    elif val[count][0] in ['==','<','>','<=','>=','!=','%=','&','|',',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']: 
        return types

    return False

def PM():
    global count
    if(val[count][0]=='+') or (val[count][0]=='-'):
        operator=val[count][1]
        count+=1
        return operator
    
    return False

def D():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        #print('check e')
        le_ty=E()
        #print(le_ty,'e1')
        if(le_ty!=False):
            operator=D1(le_ty)
            #print(operator,'e1')
            if(operator!=False):
                #print('yes')
                return operator
            
    return False

def D1(types):
    global count
    if(val[count][0]=='*') or (val[count][0]=='/') or (val[count][0]== '%'):
        operator=MDM()
        if(operator!=False):
            le_t=E()
            if(le_t!=False):
                re_ty=compatibility.binary_comp(types,le_t,operator)
                operators=D1(re_ty)
                if(operators!=False):
                    return True
    elif val[count][0] in ['+','-','==','<','>','<=','>=','!=','%=','&','|',',',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:             
        return types
    
    return False

def MDM():
    global count
    if(val[count][0]=='*') or (val[count][0]=='/') or (val[count][0]== '%'):
        operator=val[count][1]
        count+=1
        return operator
    
    return False

def E():
    global count
    if(val[count][0]=='IDENTIFIER'):
        name=val[count][1]
        count+=1
        e_types=F_9(name)
        #print(e_types,'e')
        if(e_types!=False):
            return e_types
    elif(val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        #print('check int')
        e_types=val[count][0].split()[0].lower()
        count+=1
        return e_types

    return False 

'''def F_9():
    global count
    if(val[count][0]=='('):
        if(FUNC_CALL()):
            return True  
    elif(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/=') :
        if(INC_DEC()):
            return True 
    elif val[count][0] in ['*','/','%','+','-','==','<','>','<=',',','>=','!=','%=','&','|',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:           
        #print('true',val[count][0])
        return True 

    return False '''
def F_9(name):
    global count
    if(val[count][0]=='('):
        e_types=FUNC_CALL(name)
        if(e_types!=False):
            return e_types 
    elif(val[count][0]=='.'):
        if(AE()):
            if(FUNC_CALL()):
                return True  
    elif(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/=') :
        e_types=INC_DEC(name)
        #print(e_types,'inc re')
        if(e_types!=False):
            return e_types
    elif val[count][0] in ['*','/','%','+','-','==','<','>','<=',',','>=','!=','%=','&','|',']',')','{',';','FOR','IF','TRY','DATA TYPE','IDENTIFIER']:  
        e_types=scope.scope_lookup(name)
        #print('true',val[count][0])
        return e_types

    return False     

def BODY():
    global count
    global ccr
    global li_n
    global li_t
    global stack_add
    #print(val[count][0],'body')
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER'):
        if(SST()):
            #print('for true')
            return True
    elif(val[count][0]=='{'):
        #print("MST")
        if(ccr!='global'):
            ccr_list.append(ccr)
            ccr='global'
        stack.push(stack_add)
        stack_add+=1
        
        if (len(li_n)!=0):
            #print(stack.size(),stack.top())
            for i in range(len(li_n)):
                scope.scope_insert(li_n[i],li_t[i],stack.top())
                #counter-=1
            
        li_t=[]
        li_n=[]   
        #print(val[count][0])
        #print(count)
        count+=1
        #print(val[count][0])
        #print(val[count][0],'body',count)
        if(MST()):
            #print("MST",val[count][0])
            if(val[count][0]=='}'):
                if(ccr=='global') and (len(ccr_list)>1):
                    ccr=ccr_list.pop()
                stack.pop()
                return True
    elif(val[count][0]==';'):
        return True
    
    return False

def SST():
    global count
    #print('for sst',val[count][0])
    if(val[count][0]=='FOR'):
        if(FOR_LOOP()):
            return True
    elif(val[count][0]=='IF'):
        if(if_else()):
            return True  
    elif(val[count][0]=='TRY'):
        if(EXCEPTIION_HANDLING()):
            return True 
    elif(val[count][0]=='DATA TYPE'):
        types=val[count][1]
        count+=1
        if(F_10(types)):
            return True
    elif(val[count][0]=='IDENTIFIER'):
        name=val[count][1]
        #print('for true','sst')
        count+=1 
        types=F_11(name) 
        if(types!=False):
            #print("print")
            return types
    return False

def F_10(types):
    global count
    if(val[count][0]=='IDENTIFIER'):
        if(DEC(types)):
            return True
    elif(val[count][0]=='DEF'):   
        if(FUNC_DEF(types)):
            return True

    return False

def F_11(name):
    global count
    if(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=')  or (val[count][0]=='/=') :
        #print('for true','f-11')
        ret_t=INC_DEC(name)
        if(ret_t!=False):
            #print('for true be  ',val[count][0])
            count+=1
            #print('for true',val[count][0])
            if(count<len(val)):
                if (val[count][0]==';'):
                    #print('for true',val[count][0])
                    return ret_t
    elif(val[count][0]=='='):
        count+=1
        #lel_t=scope.scope_lookup(name)
        #print(val[count][1])
        reg_t=F_13()
        #print(reg_t)
        lel_t=reg_t
        scope.scope_insert(name,lel_t,stack.top())
        #print(lel_t,reg_t,val[count][1])
        if(reg_t!=False):
            if (lel_t!=reg_t):
                raise Exception(f"Type mismatch in assignment for variable '{val[count-2][1]}' at line '{val[count-2][2]}'") 
            return True
    elif (val[count][0]=='('):
        ret_t=FUNC_CALL(name)
        if(ret_t!=False):
            return reg_t  

    return False    

def F_13():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            if (val[count][0]==';'):
                return True
    elif(val[count][0]=='{'):
        if(DICTIONARY()):
            count+=1
            if (val[count][0]==';'):
                return True
    if(val[count][0]=='NEW'):
        types_b=OBJECT_CREATE()
        if(types_b!=False):
            count+=1
            if (val[count][0]==';'):
                #print(types_b,'ob')
                return types_b

    return False

def MST():
    global count
    
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER'):
        if(SST()):
            #print('for true','mst')
            count+=1
            if(MST()):
                return True
    elif(val[count][0]=='}'):
        return True

    return False            

def OBJECT_CREATE():
    global count
    arg=[]
    if(val[count][0]=='NEW'):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            name=val[count][1]
            count+=1
            #print('inj')
            if(val[count][0]=='('):
                count+=1
                argu=ARGUMENTS(arg)
                if(argu!=False):
                    if(val[count][0]==')'):
                        #print(val[count][0])
                        #print(name,'f')
                        ccr=name
                        #print(para_check,ccr,member.member_list[ccr])
                        if(len(member.member_list[ccr])==0):
                            raise Exception(f"Symbol '{name}' not declared  so no constructor for class")    
                        else:
                            on=False
                            for item in member.member_list[ccr]:
                                #print(item,ccr)
                                if isinstance(item[1],list):
                                    if (item[0]=='__init__') and (argu==item[1]):
                                        #counter+=1
                                        #print(item[3],'d')
                                        on=True
                                        #print(on)
                                        break
                            #print(on)        
                            if not on:
                                #counter+=1
                                raise Exception(f"Symbol '{name}' not declared  so no constructor for class")        
                        ccr='global'  
                        return name

    return False


def ARGUMENTS(arg):
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        if(val[count][0]=='IDENTIFIER'):
            rp_t=scope.scope_lookup(val[count][1])
            arg.append(rp_t)
        if (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
            rp_t=val[count][0].split()[0].lower()
            arg.append(rp_t)
        count+=1
        if(PLZADDMORE(arg)):
            return arg
    elif(val[count][0]==')'):
        return arg
     
    return False   

def PLZADDMORE(arg):
    global count
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
            if(val[count][0]=='IDENTIFIER'):
                rp_t=member.mem_lookup(val[count][1])
                arg.append(rp_t)
            if (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
                rp_t=val[count][0].split()[0].lower()
                arg.append(rp_t)
            count+=1
            if(PLZADDMORE(arg)):
                return arg
    elif(val[count][0]==')'):
        return arg       
    return False


def CLASS():
    global count
    if(val[count][0]=='CLASS'):
        types=val[count][1]
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            name=val[count][1]
            count+=1
            #print('yes')
            if(F_4(types,name)):
            
                return True 

    return False

def F_4(types,name):
    global count
    parent=[]
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER') or (val[count][0]=='DEF') or (val[count][0]=='SELF') or (val[count][0]=='STATICMETHOD') or (val[count][0]=='VIRTUAL') or (val[count][0]=='OVERRIDE') or (val[count][0]==';') or (val[count][0]=='{'):
        if(CLASS_BODY(types,name,parent)):
            return True
    elif(val[count][0]=='('):
        count+=1
        parent=BASE_CLASSES(parent)
        if(parent!=False):
            if(val[count][0]==')'):
                count+=1
                #print('d')
                if(CLASS_BODY(types,name,parent)):
                    return True
    return False                       

def BASE_CLASSES(parent):
    global count
    if(val[count][0]=='IDENTIFIER'):
        per=val[count][1]
        definition.define_lookup(per)#abdul
        parent.append(per)
        count+=1
        parent=F_5(parent)
        if(parent!=False):
            return parent
    
    return False 

def F_5(parent):
    global count
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='IDENTIFIER'):
            per=val[count][1]
            definition.define_lookup(per)
            parent.append(per)
            count+=1
            parent=F_5(parent)
            if(parent!=False):
                return parent
    elif(val[count][0]==')'):#null remove
        return parent

    return False 

# def CLASS_DEF():
#     global count
#     if(val[count][0]=='{'):
#         count+=1
#         if (CLASS_BODY()):
#             count+=1
#             if(val[count][0]=='}'):
#                 return True

#     return False

def CLASS_FUN(types):
    global count
    global li_n
    global li_t
    li_n=[]
    li_t=[]
    #print(val[count][0],'con_body',val[count+1][0])
    if (val[count][0]=='DEF'):
        count+=1
        if (val[count][0]=='IDENTIFIER'):
            name=val[count][1]
            count+=1
            if(val[count][0]=='('):
                count+=1
                if(val[count][0]=='SELF'):
                    count+=1
                    #print(val[count][0],'self')
                    li_n,li_t =PARA(li_n,li_t)
                    if (li_n!=False):
                        if(val[count][0]==')'):
                            pra_li=li_t
                            pra_li.append(types)
                            member.mem_insert(name,pra_li)
                            count+=1
                            #print(val[count][0],'self')
                            if(BODY()):
                                return True
    #elif(val[count][0]=='@'):
        #count+=1
    # elif(val[count][0]=='STATICMETHOD'):
    #     count+=1
    #     if(FUNC_DEF()):
    #         return True
    return False

def PARA(li_n,li_t):
    global count
    if(val[count][0]==','):
        count+=1
        if(val[count][0]=='DATA TYPE'):
            li_t.append(val[count][1])
            count+=1
            if(val[count][0]=='IDENTIFIER'):
                li_n.append(val[count][1])
                count+=1
                #print(val[count][0],'self1',val[count-1][1])
                li_n,li_t=PARA(li_n,li_t)
                if (li_n!=False):
                    #print(val[count][0],'self1',val[count-1][1])
                    return  li_n,li_t                         
            
    elif(val[count][0]==')'):#remove null 
        return li_n,li_t  

    return False                                

def CONSTRUCTOR(): 
    global count
    global li_n
    global li_t
    li_t=[]
    li_n=[]
    if (val[count][0]=='DEF'):
        count+=1
        if(val[count][0]=='__INIT__'):
            name=val[count][1]
            count+=1
            if(val[count][0]=='('):
                count+=1
                if(val[count][0]=='SELF'):
                    count+=1
                    #print('para true',val[count][0])
                    li_n,li_t =PARA(li_n,li_t)
                    if (li_n!=False):
                        if(val[count][0]==')'):
                            member.mem_insert(name,li_t)
                            count+=1
                            #if(val[count][0]=='{'):
                                #count+=1
                            if(BODY()):
                                    #if(val[count][0]=='}'):
                                return True
                                    
    return False  


'''def CONSTRUCTOR_BODY():
    global count
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER') :
        count+=1
        if(CLASS_BODY()):
            return True
        
    elif(val[count][0]=='self') :#or(val[count][0]==''): null
        if(CONS_BD):
            return True

    return False'''

def CONS_BD():
    global count
    if(val[count][0]=='SELF'):
        count+=1
        if(val[count][0]=='.'):
            count+=1
            if(val[count][0]=='IDENTIFIER'):
                count+=1
                if(val[count][0]=='='):
                    count+=1
                    if (val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
                        count+=1
                        if(count<len(val)):
                            if(val[count][0]==';'):
                                count+=1
                                #print(val[count][0])
                                if(C_B()):
                                    return True
                
                    
                
    return False

def C_B():
    global count
    if(val[count][0]=='SELF'):
        if(CONS_BD()):
            return True 
    elif(val[count][0]=='}'): #null remove 
        return True
    return False           

def STRUCTURE_LESS():
    global count
    if(val[count][0]=='FOR'):
        if(FOR_LOOP()):
            return True
    elif(val[count][0]=='IF'):
        if(if_else()):
            return True    
    elif(val[count][0]=='TRY'):
        if(EXCEPTIION_HANDLING()):
            return True
    elif(val[count][0]=='IDENTIFIER'):
        name=val[count][1]
        count+=1
        #print(val[count][0],'inc')
        typess=F_23(name)
        if(typess!=False):
            return typess
    elif(val[count][0]=='DATA TYPE'):
        types=val[count][1]
        count+=1
        if(F_24(types)):
            return True  
    elif(val[count][0]=='CLASS'):
        if(CLASS()):
            #print(val[count][0],'f2',val[count-1][0],val[count-2][0],count)
            return True 


    try:
        print("error ",val[count][0],' at line ',val[count][2],count) 
    except IndexError:
        print("error after ",val[count-1][0],' at line ',val[count-1][2],count) 
         
    return False    
    

def F_23(name):
    global count
    if(val[count][0]=='+=') or (val[count][0]=='-=') or (val[count][0]=='*=') or (val[count][0]=='/='):
        re_t=INC_DEC(name)
        if(re_t!=False):
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):
                    return re_t
    elif(val[count][0]=='('):
        #print('func')
        re_t=FUNC_CALL(name)
        if(re_t!=False):
            return re_t
        
    elif(val[count][0]=='.'):
        #print('func')
        if(AE()):
            #print(val[count][0],'23')
            if(F_Z(name)):
                return True
        
    elif(val[count][0]=='='):
        on=False
        #print(name,val[count][1])
        count+=1
        if val[count][0] in ['[','{','NEW']:
            on=True            
        re_t=F_25()
        #print(val[count][0],re_t,'y')
        if on:
            le_t=re_t
            scope.scope_insert(name,le_t,stack.top())
        else:    
            le_t=scope.scope_lookup(name)
        #print(re_t,'red')
        if(re_t!=False):
            on=False

            if (le_t!=re_t):
                raise Exception(f"Type mismatch in assignment for variable '{val[count-2][1]}' at line '{val[count-2][2]}'") 
            return True
    return False
def F_Z(name):
    global count
    if(val[count][0]=='('):
        if(FUNC_CALL()):
            return True
    elif(val[count][0]=='='):
        le_t=scope.scope_lookup(name)
        #operator=val[count][1]
        count+=1
        re_ty=Assignment()
        #print(re_ty,'F_Z','e')
        if(re_ty!=False):
            if(le_t!=re_ty):
                raise Exception(f"Type mismatch in assignment for variable '{val[count-2][1]}' at line '{val[count-2][2]}'") 
            return True
     
    return False
def Assignment():
    global count
    if(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
       
       re_t=expression()
       #print(re_t,'express re')
       if(re_t!=False):
            # count+=1
            # if(count<len(val)):    
            #     if(val[count][0]==';'):
            #print(re_t,'e145')
            return re_t
    
    return False    


def F_25():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            #print(val[count][0],';')
            if(count<len(val)):
                if (val[count][0]==";"):
                    return True       
    elif(val[count][0]=='{'):
        if(DICTIONARY()):
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):  
                    return True            
    elif(val[count][0]=='IDENTIFIER') or (val[count][0]=='INT CONSTANT') or (val[count][0]=='STRING CONSTANT') or (val[count][0]=='FLOAT CONSTANT') or (val[count][0]=='BOOLEAN CONSTANT'):
        #le_t=scope.scope_lookup(name)
        re_ty=Assignment()
        #print(re_ty,'F_Z','e')
        if(re_ty!=False):
            #if(le_t!=re_t):
               # raise Exception(f"Type mismatch in assignment for variable '{val[count-2][1]}' at line '{val[count-2][2]}'") 
            return re_ty
    
    elif(val[count][0]=='NEW'):
        typessss=OBJECT_CREATE()
        if(typessss!=False):#obj abd
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):
                    #print(typessss,'yyyyy')
                    return typessss

    return False

def F_24(types):
    global count
    if(val[count][0]=='IDENTIFIER'):
        if(DEC(types)):
            return True
    elif(val[count][0]=='DEF'):
        if(FUNC_DEF(types)):
            return True

    return False        

def CLASS_BODY(types,name,parent):
    global count#abdul
    global ccr
    global ccr_list
    ccr_list.append(ccr)
    #print(name,types,parent)
    ccr=definition.define_insert(name,types,parent)
    member.member_list[ccr]=[]
    if(val[count][0]=='{'):
        count+=1
        if(CLASS_MST()):
            #print(val[count][0])
            if(val[count][0]=='}'):
                ccr=ccr_list.pop()
                return True
    
    return False


def CLASS_SST():
    global count
    #print(val[count][0])
    if(val[count][0]=='FOR'):
        if(FOR_LOOP()):
            return True
    elif(val[count][0]=='IF'):
        if(if_else()):
            return True    
    elif(val[count][0]=='TRY'):
        if(EXCEPTIION_HANDLING()):
            return True
    elif(val[count][0]=='IDENTIFIER'):
        name=val[count][1]
        count+=1
        types=F_7(name)
        if(types!=False):
            return types
    elif(val[count][0]=='DATA TYPE'):
        types=val[count][1]
        count+=1
        if(F_6(types)):
            #print(val[count][0],'con_body',val[count+1][1])
            return True  
    elif(val[count][0]=='DEF'):
        if(CONSTRUCTOR()):
            #print(val[count][0],'con_body',val[count+1][0])
            return True
    elif(val[count][0]=='SELF'):
        #print('self')
        if(CONS_BD()):
            count-=1
            #print(val[count][0],'con')
            return True          
    elif(val[count][0]=='STATICMETHOD') or (val[count][0]=='VIRTUAL') or (val[count][0]=='OVERRIDE'):
        if(EX_FUNC()):
            return True 
 
    return False


def CLASS_MST():
    global count
    if(val[count][0]=='FOR') or (val[count][0]=='IF') or (val[count][0]=='TRY') or (val[count][0]=='DATA TYPE') or (val[count][0]=='IDENTIFIER') or (val[count][0]=='DEF') or (val[count][0]=='SELF') or (val[count][0]=='STATICMETHOD') or (val[count][0]=='VIRTUAL') or (val[count][0]=='OVERRIDE'):
        if(CLASS_SST()):
            count+=1
            if(CLASS_MST()):
                return True
    elif(val[count][0]=='}'):
        return True

    return False        


def EX_FUNC():
    global count
    global t_m
    t_m='-'
    #print(val[count][0])
    if(val[count][0]=='STATICMETHOD'):
        t_m=val[count][1]
        count+=1
        if(val[count][0]=='DATA TYPE'):
            types=val[count][1]
            count+=1
            #print(val[count][0])
            if(FUNC_DEF(types)):
                return True
    elif(val[count][0]=='VIRTUAL'):
        t_m=val[count][1]
        count+=1
        if(val[count][0]=='DATA TYPE'):
            types=val[count][1]
            count+=1
            if(FUNC_DEF(types)):
                return True
    elif(val[count][0]=='OVERRIDE'):
        t_m=val[count][1]
        count+=1
        if(val[count][0]=='DATA TYPE'):
            types=val[count][1]
            count+=1
            if(FUNC_DEF(types)):
                return True

    return False

def F_6(types):
    global count
    #print(val[count][0])
    if(val[count][0]=='IDENTIFIER'):
        if(DEC(types)):
            #print('c')
            return True
    elif(val[count][0]=='DEF'):
        #print(val[count][0])    
        if(CLASS_FUN(types)):
            #print(val[count][0])
            return True

    return False

def F_7(name):
    global count
    if val[count][0] in ['+=','-=','*=','/=']:
        re_t=INC_DEC(name)
        if(re_t!=False):
            return re_t
    elif (val[count][0]=='='):
        count+=1
        re_t=F_8()
        le_t=re_t
        member.mem_insert(name,le_t)
        #print(val[count][0],'con')
        if(re_t!=False):
            scope.scope_insert(name,re_t,stack.top())
            return True  

    return False

def F_8():
    global count
    if(val[count][0]=='['):
        if(LIST()):
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):
                    return True
    elif(val[count][0]=='{'): 
        if(DICTIONARY()):
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):
                    return True
    elif(val[count][0]=='NEW'):
        types_c=OBJECT_CREATE()
        if(types_c!=False):
            count+=1
            if(count<len(val)):
                if(val[count][0]==';'):
                    return types_c
    return False        


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    def top(self):
        return self.items[-1]


class scope: 
    def __init__(self):
        self.scope_list=[]
    
    def scope_insert(self,value,typ,scope):
        global counter
        #print("innn")
        if isinstance(typ,list):
            if (len(self.scope_list)!=0):
                #print("innn")
                for item in self.scope_list:
                    if isinstance(item[1],list):
                        exit_li=item[1][:-1]
                        new_li=typ[:-1]
                        if not ((item[0]==value) and (exit_li==new_li) and(item[2]==stack.top())):
                            pass
                        else:
                            
                            raise Exception(f"Symbol '{value}' already declared in this scope at line '{val[count-1][2]}'")
                add_val=[]
                add_val.append(value)
                add_val.append(typ)
                add_val.append(scope)
                self.scope_list.append(add_val)
                return True
                return()
            else: 
                #print("i2n")  
                add_val=[]
                add_val.append(value)
                add_val.append(typ)
                add_val.append(scope)
                self.scope_list.append(add_val) 
                return True
                #print("self",self.scope_list)

        if (len(self.scope_list)!=0):
            for item in self.scope_list:
                #print(item[0],item[2],stack.top())
                if not ((item[0]==value) and (item[2]==stack.top())):
                    pass
                else:
                    #print(counter,len(tokenization))
                    raise Exception(f"Symbol '{value}' already declared in this scope at line '{val[count-1][2]}'")  
            add_val=[]
            add_val.append(value)
            add_val.append(typ)
            add_val.append(scope)
            self.scope_list.append(add_val)
            #print(self.scope_list,tokenization[counter][1],'d')
            return True
            return()    
              
        else:   
            add_val=[]
            add_val.append(value)
            add_val.append(typ)
            add_val.append(scope)
            self.scope_list.append(add_val)
            return True  
    

    def scope_lookup(self,value):
        
        #print(val,self.scope_list)
        if (len(self.scope_list)==0):
            raise Exception(f"Symbol '{value}' not declared ")    
        else:
            #cur_sp=stack.top()
            i=0
            #print(tokenization[counter],stack.top())
            #print(value)
            while(i<stack.size()-1):
                for item in self.scope_list:
                    if((item[0]==value) and (item[2]==stack.items[stack.size()-i-1])):     
                        #print(self.scope_list,stack.items)  
                        return item[1]
                i+=1    
            raise Exception(f"Symbol '{value}' not declared") 

    def Fun_scope_lookup(self,value,para_li):
        global counter
        if(len(self.scope_list)==0):
            raise Exception(f"Symbol '{value}' not declared g")    
        else:
            i=0
            while(i<stack.size()-1):
                for item in self.scope_list:
                    if isinstance(item[1],list):
                        if((item[0]==value) and (para_li==item[1][:-1]) and(item[2]==stack.items[stack.size()-i-1])):

                            #print(self.scope_list,stack.items)  
                            return item[1][-1]
                i+=1
            
            raise Exception(f"Symbol '{value}' not declared") 

class member():
    def __init__(self):
        self.member_list={}

    def mem_insert(self,name,typ):
        global t_m
        global ccr
        if (t_m=='override'):
            add_val=[]
            add_val.append(name)
            add_val.append(typ)
            add_val.append(t_m)
            #print(add_val)
            #print(add_val,ccr,'check')
            on_over=False
            t_m='-'
            for item in definition.define_list:
                if(item[0]==ccr):
                    #print(item)
                    if (len(item[2])!=0):
                        over_check=item[2]
                        #print(over_check)
                        for cl in over_check:
                            if(len(member.member_list[cl])!=0):
                                for ite in member.member_list[cl]:
                                    #print(ite,member.member_list[cl])
                                    if isinstance(ite[1],list):
                                        if((ite[0]==add_val[0]) and(ite[1]==add_val[1]) and (ite[2]=='virtual')):
                                            on_over=True
                                            pass
                            else:
                                
                                raise(f"this class {ccr} its parent class donot have function")            
                    else:
                        
                        raise(f"this class {ccr} this not have parent class")    
            if(on_over==False):
                raise(f"CAN'T OVERRIDE IT ")
            self.member_list[ccr].append(add_val)  
            return()
    
        if isinstance(typ,list):
            if (len(self.member_list[ccr])!=0):
                for item in self.member_list[ccr]:
                    if isinstance(item[1],list):
                        exit_li=item[1][:-1]
                        new_li=typ[:-1]
                        if not ((item[0]==name) and (exit_li==new_li)):
                            pass
                        else:
                            
                            raise Exception(f"Symbol '{name}' already declared in this scope at line '{val[count-1][2]}'")
                add_val=[]
                add_val.append(name)
                add_val.append(typ)
                add_val.append(t_m)
                #print(add_val)
                self.member_list[ccr].append(add_val)
                t_m='-'
                
                return()
            else:   
                add_val=[]
                add_val.append(name)
                add_val.append(typ)
                add_val.append(t_m)
                self.member_list[ccr].append(add_val) 
                t_m='-' 
                return()
                
                            

        if (len(self.member_list[ccr])!=0):
            for item in self.member_list[ccr]:
                #print(item[0],item[2],stack.top())
                if not (item[0]==name):
                    pass
                else:
                    #counter+=1
                    #print(counter,len(tokenization))
                    raise Exception(f"Symbol '{name}' already declared in this class at line '{val[count-1][2]}'")  
            add_val=[]
            add_val.append(name)
            add_val.append(typ)
            add_val.append(t_m)
            self.member_list[ccr].append(add_val)
            t_m='-'
            #counter+=1
            #print(self.scope_list,tokenization[counter][1],'d')
            return()    
              
        else:   
            add_val=[]
            add_val.append(name)
            add_val.append(typ)
            add_val.append(t_m)
            self.member_list[ccr].append(add_val)  
            t_m='-'
            #counter+=1

    def mem_lookup(self,name):
        global ccr
        #global counter
        if (len(self.member_list[ccr])==0):
            raise Exception(f"Symbol '{name}' not declared ")    
        else:
            for item in self.member_list[ccr]:
                if (item[0]==name):
                    #counter+=1
                    #print(item[3])
                    return(item[1]) 

            i=0
            #print(tokenization[counter],stack.top())
            while(i<stack.size()-1):
                for item in scope.scope_list:
                    if((item[0]==name) and (item[2]==stack.items[stack.size()-i-1])):    
                        #counter+=1  
                        #print(self.scope_list,stack.items)  
                        return item[1]    
                i+=1
            #counter+=1    
            raise Exception(f"Symbol '{name}' not declared")
        
    def Fun_mem_lookup(self,name,para_li):
        #global counter
        #print(name,para_li,ccr,stack.size(),stack.top())
        if(len(self.member_list[ccr])==0):
            raise Exception(f"Symbol '{name}' not declared g")    
        else:
            for item in self.member_list[ccr]:
                if isinstance(item[1],list):
                    if (item[0]==name) and (para_li==item[1][:-1]):
                        #counter+=1
                        #print(item[3])
                        return(item[1][-1],item[2])
                
            i=0
            while(i<stack.size()-1):
                for item in scope.scope_list:
                    if isinstance(item[1],list):
                        if((item[0]== name) and (para_li==item[1][:-1]) and(item[2]==stack.items[stack.size()-i-1])):
                            #counter+=1  
                            #print(self.scope_list,stack.items)  
                            return (item[1][-1],'-')
                i+=1
            #counter+=1
            raise Exception(f"Symbol '{name}' not declared") 

class definition():
    def __init__(self):
        self.define_list=[]

    def define_insert(self,name,typ,parent):
        #print(name,typ,parent)
        global counter
        if (len(self.define_list)!=0):
            for item in self.define_list:
                #print(item[0],item[2],stack.top())
                if not ((item[0]==name) and (item[1]=='class')):
                    pass
                else:
                    #print(counter,len(tokenization))
                    raise Exception(f"class '{name}' already declared in this scope at line '{val[count-1][2]}'") 
            add_val=[]
            add_val.append(name)
            add_val.append(typ)
            add_val.append(parent)
            add_val.append(name)
            self.define_list.append(add_val)
            #counter+=1
            #print(self.scope_list,tokenization[counter][1],'d')
            return(name.lower())
        else:   
            add_val=[]
            add_val.append(name)
            add_val.append(typ)
            add_val.append(parent)
            add_val.append(name)
            self.define_list.append(add_val)  
            #counter+=1 
            return(name.lower())

    def define_lookup(self,name):
        global counter
        if (len(self.define_list)==0):
            raise Exception(f"Symbol '{name}' class not declared g")
        else:
            for item in self.define_list:
                if (item[0]==name):
                    #counter+=1
                    #print(item[3])
                    return(item[3])
            #counter+=1
            raise Exception(f"Symbol '{name}' class not declared") 
        
class compatibility():
    def __init__(self):
        self.binary_list=[['int','int','+=','int'],['int','int','-=','int'],['int','int','/=','int'],['int','int','*=','int'],['int','int','+','int'],['int','int','-','int'],['int','int','*','int'],['int','int','/','int'],['int','int','!=','bool'],['int','int','%','int'],['int','int','//','int'],['int','int','**','int'],['int','int','==','bool'],['int','int','<','bool'],['int','int','<=','bool'],['int','int','>','bool'],['int','int','>=','bool'],['float','int','+=','float'],['float','int','-=','float'],['float','int','%=','float'],['float','int','*=','float'],['float','int','+','float'],['int','float','+=','float'],['int','float','-=','float'],['int','float','*=','float'],['int','float','/=','float'],['int','float','+','float'],['float','int','-','float'],['int','float','-','float'],['float','int','*','float'],['int','float','*','float'],['float','int','/','float'],['int','float','/','float'],['float','int','%','float'],['int','float','%','float'],['float','int','//','int'],['int','float','//','int'],['float','int','==','bool'],['int','float','==','bool'],['float','int','!=','bool'],['int','float','!=','bool'],['float','int','<','bool'],['int','float','<','bool'],['float','int','>','bool'],['int','float','>','bool'],['float','int','<=','bool'],['int','float','<=','bool'],['float','int','>=','bool'],['int','float','>=','bool'],['float','float','+','float'],['float','float','-','float'],['float','float','*','float'],['float','float','+=','float'],['float','float','-=','float'],['float','float','*=','float'],['float','float','/=','float'],['float','float','%','float'],['float','float','//','int'],['float','float','**','float'],['float','float','==','bool'],['float','float','!=','bool'],['float','float','<','bool'],['float','float','>','bool'],['float','float','<=','bool'],['float','float','>=','bool'],['string','string','+','string'],['string','string','+','string'],['string','int','*','string'],['int','string','*','string'],['string','string','==','bool'],['string','string','!=','bool'],['string','string','>','bool'],['string','string','<','bool'],['string','string','<=','bool'],['string','string','>=','bool'],['bool','bool','AND','bool'],['bool','bool','OR','bool'],['bool','bool','&','bool'],['bool','bool','|','bool']]
        self.uni_list=[]

    def binary_comp(self,le_ty,rg_ty,oper): 
        comp_check=[]
        comp_check.append(le_ty)
        comp_check.append(rg_ty)   
        comp_check.append(oper)
        #print(comp_check,'d')
        for comp_item in self.binary_list:
            if comp_item[:-1]==comp_check:
                #counter+=1
                return(comp_item[-1])
        #counter+=1
        raise Exception(f"This {oper} Does not support this Data Type {le_ty} and this {rg_ty}")    

stack = Stack()
stack.push(-1)
stack.push(0)
stack_add=1
scope=scope()
definition=definition()
member=member()
compatibility=compatibility()
a=True
val=tokenization
ccr_list=[]
li_t=[]
li_n=[]
ccr='global'
t_m='-'
while(count<len(val)-1) and (a==True):   
    a=STRUCTURE_LESS()
    try:
        print(a,val[count][2])
    except IndexError:
        print()
    count+=1

#print(stack.items,scope.scope_list)

print("SCOPE")
print('======================================================================================================================================')    
print(ccr)    
print("SCOPE TABLE")
print('======================================================================================================================================')
print(scope.scope_list,len(scope.scope_list),stack.top())
print("DEFINITION TABLE")
print('======================================================================================================================================')
print(definition.define_list)
print("MEMBER TABLE")
print('======================================================================================================================================')
print(member.member_list)
