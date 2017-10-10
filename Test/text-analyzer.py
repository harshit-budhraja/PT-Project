log = input('Enter the file name to decrypt (from this directory): ')
data = ""

with open(log) as f:
    for line in f:
    	line = line.replace('\r','').replace('\n','')
    	if(line=="space"):
    		line = " "
    	if(line=="Shift_L"):
    		line = ""
    	if(line=="Shift_R"):
    		line = ""
    	if(line=="period"):
    		line = "."
    	if(line=="exclam"):
    		line = "!"
    	if(line=="dollar"):
    		line = "$"
    	if(line=="apostrophe"):
    		line = "'"
    	if(line=="plus"):
    		line = "+"
    	if(line=="minus"):
    		line = "-"
    	if(line=="at"):
    		line = "@"
    	if(line=="numbersign"):
    		line = "#"
    	if(line=="percent"):
    		line = "%"
    	if(line=="asciicircum"):
    		line = "^"
    	if(line=="ampersand"):
    		line = "&"
    	if(line=="asterisk"):
    		line = "*"
    	if(line=="parenleft"):
    		line = "("
    	if(line=="parenright"):
    		line = ")"
    	if(line=="underscore"):
    		line = "_"
    	if(line=="equal"):
    		line = "="
    	if(line=="asciitilde"):
    		line = "~"
    	if(line=="comma"):
    		line = ","
    	if(line=="Return"):
    		line = "\n"
    	if(line=="colon"):
    		line = ":"
    	
    	# Exception for break of the keylogger
    	if(line=="grave"):
    		line = "\n-------------------------------------------------------------------------\n"
    	
    	
    	data = data + str(line)

print(data)
