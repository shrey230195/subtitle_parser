#program to parse an srt file and store  it in a database which 
#i) takes time as input and returns the subtitle 
# ii) Takes a text as input and returns the time

from split_srt import srt_store_to_database 
from split_srt import start_time
from split_srt import end_time
from split_srt import dialogue 
pos=0
#open the srt file
with open('ironman.srt',"r") as f:
	srtText=f.read()
	srt_store_to_database(srtText)

#function to print the lists(start_time,end_time,dialogue)
	def print_detail(list):
		for i in range(0,len(list)):
			print "\n\t"
			print list[i]

#binary search to find the position of inputted time in the file

	def binary_search(time):
		first=0
		last=len(start_time)-1
		found=False
		while(first<=last and not found):
			midpoint=(first+last)/2
			if(time>=start_time[midpoint] and time<=end_time[midpoint]):
				global pos
				pos=midpoint
				found=True
				
			else:
				if(time<start_time[midpoint]):
					last=midpoint-1
					
				else:
					first=midpoint
							
	#function to search the start time an dend time of inputted dialogue               
	def search_text():
		found = False
		#print "list of dialogues::\n"
		#print_detail(dialogue)
		string = raw_input("enter the dialogue to be searched\n")
		       
		for i in range(0,len(dialogue)):
		    if string==dialogue[i]:
			    print "\n start time :: \t"
			    print start_time[i]
			    print "\n end time ::\t"
			    print end_time[i]
			    found= True
		if(found==False):				#simple else statement wasn't working(i dont know why)
			print "not found"	

	# menu for operations
	def menu():
		print """ MENU ::::
			  SUBTILE FILE                                   :: 1
			  STARTING TIME                                  :: 2
			  ENDING TIME                                    :: 3
			  DIALOGUE 	                                 :: 4
			  CORRESPONDING DIALOGUE WITH SOME TIME AS INPUT :: 5
			  CORRESPONDING TIME WITH SOME TEXT AS INPUT     :: 6
			  exit                                           :: 0"""
	
	ans = 'y'
	while(ans=='y'):
		menu()
		ch=raw_input()
		if(ch=='0'):
			exit()
		elif(ch=='2'):
			print_detail(start_time)
		elif(ch=='3'):
			print_detail(end_time)
		elif(ch=='4'):
			print_detail(dialogue)
		elif(ch=='5'):
			time=float(raw_input("enter the time for which dialogue is to be seached"))
			binary_search(time)
			print "\n DIALOGUE::\n\t"
			print dialogue[pos]		
					
		elif(ch=='6'):
			search_text()
				    

		else:
			print "\ninvalid choice"	
		ans=raw_input("\ntry again? (y/n)")	
				
			


			    			