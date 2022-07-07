
""""
@Author Ava Reese
WhereInTheWorld etude 7
"""
import re
import json

class whereintheworld:
    
    def __init__(self, inputString):
        
        sf = "^((\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))|"\
        "(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))(\s)?(N|S|NORTH|SOUTH))(\,\s|\s)"\
        "(((\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?)))|((?:180(?:(?:\.0{1,6})?)"\
        "|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))(\s)?(E|W|EAST|WEST)))$"

        sfReverseCheck = "^((((\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?)))"\
        "|((?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))(\s)?(E|W|EAST|WEST)))(\,\s|\s)(((\+|-)?"\
        "(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?)))|((?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))"\
        "(\s)?(N|S|NORTH|SOUTH))))$"    
        
        dmsRegex = "^((((\+|-)?(?:90|(?:[0-9]|[0-8][0-9])))(\u00B0|\s|:|)(\s)?(?:60|(?:[0-9]|[0-5][0-9]))(\'|\′|\s|:|)(\s)?(?:60(?:(?:\.0{1,6})?)"\
        "|(?:[0-9]|[0-5][0-9])(?:(?:\.[0-9]{1,6})?))(\"|\″|\s|:|)(\s)?)|(((?:90|(?:[0-9]|[0-8][0-9])))(\u00B0|\s|:|)(\s)?"\
        "(?:60|(?:[0-9]|[0-5][0-9]))(\'|\′|\s|:|)(\s)?(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[0-5][0-9])(?:(?:\.[0-9]{1,6})?))"\
        "(\"|\″|\s|:|)(\s)?(N|NORTH|S|SOUTH)))(\,\s|(\s)+)?((((\+|-)?(?:180|(?:[0-9]|[0-9][0-9]|1[0-7][0-9])))(\u00B0|\s|:|)(\s)?"\
        "(?:60|(?:[0-9]|[0-5][0-9]))(\'|\′|\s|:|)(\s)?(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[0-5][0-9])(?:(?:\.[0-9]{1,6})?))"\
        "(\"|\″|\s|:|)(\s)?)|(((?:180|(?:[0-9]|[0-9][0-9]|1[0-7][0-9])))(\u00B0|\s|:|)(\s)?(?:60|(?:[0-9]|[0-5][0-9]))(\'|\′|\s|:|)(\s)?"\
        "(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[0-5][0-9])(?:(?:\.[0-9]{1,6})?))(\"|\″|\s|:|)(\s)?(E|EAST|W|WEST)))$"
        
        ddmRegex = "^((((\+|-)?(?:90|(?:[0-9]|[1-8][0-9])))(\u00B0|\s|:|)(\s)?(?:60(?:(?:\.0{1,6})?)"\
        "|(?:[0-9]|[1-5][0-9])(?:(?:\.[0-9]{1,6})?))(\'|\′|\s|:|)(\s)?)|(((?:90|(?:[0-9]|[1-8][0-9])))(\u00B0|\s|:|)(\s)?"\
        "(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[1-5][0-9])(?:(?:\.[0-9]{1,6})?))"\
        "(\'|\′|\s|:|)(\s)??(N|NORTH|S|SOUTH)))(\,\s|(\s)+)?((((\+|-)?(?:180|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])))(\u00B0|\s|:|)(\s)?"\
        "(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[1-5][0-9])(?:(?:\.[0-9]{1,6})?))"\
        "(\'|\′|\s|:|)(\s)?)|(((?:180|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])))(\u00B0|\s|:|)(\s)?"\
        "(?:60(?:(?:\.0{1,6})?)|(?:[0-9]|[1-5][0-9])(?:(?:\.[0-9]{1,6})?))(\'|\′|\s|:|)(\s)??(E|EAST|W|WEST)))$"
        
        input = inputString
        self.output = None
        
        #input = re.sub('(\s\s?)|(\s?\s)',' ',input)
        input = re.sub('(\s[dms]\s?)|(\s?[dms]\s)',' ',input)
        #print(input)
        input = input.upper().strip()
        self.name = ""
        outputList = []


        # get rid of name turn into array sep by spaces and index last value, (not isDigit) 
        # if that value isnt n s w or e then it is a name, so make that  = name
        # and remove and make it a string again
        str = ['N', 'E', 'S', 'W']
        input = input.split(" ")

        #if((input[-1].isalpha()) or ((input[-1] != 'N') or (input[-1] != 'S') or (input[-1] != 'W') or (input[-1] != 'E'))):
        if((input[-1].isalpha()) and (input[-1] not in str)):   
            self.name = input[-1]
            input = input[:-1]
            input = " ".join(input)
            input.strip()
            #print(input)
            self.name = self.name.title()
            #print(self.name)
        else:
            self.name = " "
            input = " ".join(input)
            input.strip()
            
        #input = re.sub('(\s[dms]\s?)|(\s?[dms]\s)',' ',input)
               
    # matching regex to what form and calling appropreiate method
        try:
            if(bool(re.match(sf, input))):
                outputList = self.standardForm(input, True)
            elif(bool(re.match(sfReverseCheck, input))):
                outputList = self.standardForm(input, False)
            elif(bool(re.match(ddmRegex,input))):
                outputList = self.ddm(input)
            elif(bool(re.match(dmsRegex,input))):
                outputList = self.dms(input)
            else:
                print("Unable to process: ", inputString)
        except ValueError:
            print("Unable to process: ", inputString)
            
            
        # if there is something in output list call the dictionary.
        if(outputList):
            temp = outputList[0]
            outputList[0] = outputList[1]
            outputList[1] = temp
            self.output = self.dictionary(outputList, self.name)  
        
    #checks if the number is a digit  
    def isDigitCheck(self, x):

        try: 
            x = float(x)
            return True
        except ValueError:
            return False
  
  # checks against ddm rules, if sign is S or W turn the number negative if not already      
    def ddm(self,input):
         
        for x in ["'",'"',"°"]:
            input = input.replace(x," ") 
        
        inlist = re.split(',\s|\s', input)
        outlist = [] 
        result = [0.0, 0.0]
        negLat = 1
        negLong = 1
        
        # 24 52.234 170 23.234 
        # 80 22.23 S 170 23.232
        # 80 23.23 60 22.23 W
        # 23 23.23 N 23 23.234 E
        
        # nums[0] = 23 + 23.23/60
        # nums[1] = 23 + 23.234/60
        #Positive latitudes are north of the equator, negative latitudes are south of the equator. 
        #Positive longitudes are east of the Prime Meridian; negative longitudes are west of the Prime Meridian
        
        if((len(inlist) == 4)):
            outlist = [float(s) for s in inlist if self.isDigitCheck(s)]
        elif((len(inlist) == 5) and inlist[2].isalpha()):
            neg = 1
            if(inlist[2] == 'S'):
                negLat = -1
            outlist = [float(s) for s in inlist if self.isDigitCheck(s)]
        elif((len(inlist) == 5) and inlist[4].isalpha()):
            neg =1
            if(inlist[4] == 'W'):
                negLong = -1
            outlist = [float(s) for s in inlist if self.isDigitCheck(s)]
        else:
            neg = 1
            if(inlist[2] == 'S'):
                negLat = -1
            if(inlist[5] == "W"):
                negLong = -1
            outlist = [float(s) for s in inlist if self.isDigitCheck(s)]
            
            
        result[0] = outlist[0] + (outlist[1]/60)
        result[1] = outlist[2] + (outlist[3]/60) 
        
        result[0] = round(result[0], 6)*negLat
        result[1] = round(result[1], 6)*negLong
        
        
        return result    
        
# checks against dms rules, if S  or W turn the number negative
    def dms(self,input): 
        
        for x in ["'",'"',"°"]:
            input = input.replace(x," ")
        
        # 22 23 50.234 101 30 50.23
        # 80 22 22.23 S 170 23.232 22 
        # 80 22 22.23 170 23 23.232 W
        # 80 22 22.23 S 170 22 23.232  W


        inp =  re.split(',\s|\s', input)
        out = []
        result = [0.0, 0.0]
        negLat = 1
        negLong =1
       
        if((len(inp) == 6)):
            out = [float(s) for s in inp if self.isDigitCheck(s)]
        elif((len(inp) == 7) and inp[3].isalpha()):
            if((inp[3] == 'S')):
               negLat = -1
            out = [float(s) for s in inp if self.isDigitCheck(s)]

            
        elif((len(inp) == 7) and (inp[6].isalpha())):
            neg = 1
            if(inp[4] == 'W'):
                negLong = -1
            out = [float(s) for s in inp if self.isDigitCheck(s)]
        else:
            neg = 1
            if(inp[3] == 'S'):
                negLat = -1
            if(inp[7] == 'W'):
                negLong = -1
            out = [float(s) for s in inp if self.isDigitCheck(s)]
    

        result[0] = out[0] + (out[1]/60) + (out[2]/3600)
        result[1] = out[3] + (out[4]/60) + (out[5]/3600)
            
        result[0] = round(result[0], 6)*negLat
        result[1] = round(result[1], 6)*negLong
       
        return result  
                    
   # checks against standard form rules, if S or W turn the number negative  
    def standardForm(self, input, Reversesf):
        
        for x in ["°"]:
            input = input.replace(x," ") 
        
        inputList = re.split(',\s|\s', input)
        outputList = []
        neg1 = 1
        neg2 = 1
        
        # -60.234, 50 case 1, do nothing, make an integer
        # 60.234 S, 50 case 2, get rid of s and make negative and make integer
        # -60.234, 50 E case 3, get rid of element [2] and make integer
        # 60.234 S, 50 E case 4, get rid of element [1][3] and make integer
        
        #Positive latitudes are north of the equator, negative latitudes are south of the equator. 
        #Positive longitudes are east of the Prime Meridian; negative longitudes are west of the Prime Meridian
        
        #if its S or W make the approperate number negitve if its N or E do nothing as its already postive. 
        
        #4 cases either only numbers 1 or 2. 
        # if dataArr = 2. case 1. then sort out. 
        # if dataArr = 3. then subcases. either 2 
        # element i.e dataArr[1] is not
        #an digit then case 2. else case 3. 
        
        if(len(inputList) == 2): 
            outputList = [float(s) for s in inputList if self.isDigitCheck(s)]
            
        elif((len(inputList) == 3)) and (inputList[1].isalpha()):
            
            if(inputList[1] == 'S') or (inputList[1] == 'W'):
                neg1 = -1
            outputList = [float(s) for s in inputList if self.isDigitCheck(s)]
                           
        elif((len(inputList) == 3)) and (inputList[2].isalpha()):
            
            if(inputList[2] == 'S') or (inputList[2] == 'W'):
                neg2 = -1
            outputList = [float(s) for s in inputList if self.isDigitCheck(s)]
               
        else: 

            if(inputList[1] == 'S') or (inputList[1] == 'W'):
                neg1 = -1
            if(inputList[3] == 'S') or (inputList[3] == 'W'):
                neg2 = -1     
            outputList = [float(s) for s in inputList if self.isDigitCheck(s)]
        
        
        outputList[0]*=neg1
        outputList[1]*=neg2
        
         
        if(not Reversesf):
            x = outputList[0]
            outputList[0] = outputList[1]
            outputList[1] = x   
            
            
        outputList[0] = round(outputList[0], 6)
        outputList[1] = round(outputList[1], 6)
         
        return outputList
    
    
    def dictionary(self, input, name): 
        output = {}
        output["type"] = "Feature"
        output["geometry"] = {"type" : "Point", "coordinates": input}
        output["properties"] = {"name" : name}

        return output
    
    
    def GeoJsonFile(self, path, fileName, input):
    
        output = {}
        output["type"] = "FeatureCollection"
        output["features"] = input
        
        filePathNameWExt = "./" + path + "/" + fileName 
        with open(filePathNameWExt, 'w') as outfile:
            json.dump(output,outfile)
           

def main():
    finalOutput = []
    
    while(True):
        try: 
            inputString = input("Enter a coordinate:  ")
            w = whereintheworld(inputString)
            if(w.output):
                finalOutput.append(w.output)
                #print(finalOutput)
            if(finalOutput):
                w.GeoJsonFile('./', "GeoJson.json" , finalOutput)
            
        except EOFError as e:
            # if(finalOutput):
            #     w.GeoJsonFile('./', "GeoJson.json" ,finalOutput)
            print("\n Ending program")
            quit()
    

if __name__ == "__main__":
    main()