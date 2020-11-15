#Ask user for input
def ask_user():
		UserInput = input('Please enter centimetres/metres to convert in the format "x unit1 in unit2": ')
		return UserInput

class Converter():
	#Set acceptable measurement inputs
	cm_inputs = ('cm','centimetres')
	m_inputs = ('m', 'metres')

	#Set input sucess to False until user inputs in acceptable format
	input_success = False

	def __init__(self, UserInput):
		self.UserInput = UserInput

	#Convert user input string into list of strings
	def input_to_list(self):
		InputList =  (str(self.UserInput)).split()
		return InputList


	def output(self):
		#Import list from function above
		InputList = self.input_to_list()
		#Define input variables
		unit1 = (str(InputList[1])).lower()
		unit2 = (str(InputList[3])).lower()
		x = int(InputList[0])
		#Convert cm's into m's, set input success to true if correct format
		if unit1 in self.cm_inputs and unit2 in self.m_inputs:
			self.input_success = True
			answer = str(x/100) + " m"
			print (answer)
		#Convert m's into cm's, set input success to true if correct format
		if unit1 in self.m_inputs and unit2 in self.cm_inputs:
			self.input_success = True
			answer = str(int(InputList[0])*100) + " cm"
			print (answer)
		#if input success remains false, print error message
		if not self.input_success:
			print ('Input Error: Please input in the format "x cm in m".')

		
def main():
	return Converter(ask_user()).output()
#Run converter class with user input
main()