#######################################################################
# Function: is_valid_num
# Description: To prevent the user input a wrong float number or non integer number.  
# Parameters: num
# Return values: True, False
# Pre-Conditions: User input num.
# Post-Conditions: Correct float number
#######################################################################
def is_valid_num(num):
   count = 0;
   for x in range(len(num)):
      if(num[x] < '0' or num[x] > '9'):
         if(num[x] != '.'):
            print("You idiot!!!");
            return False;

   for x in range(len(num)):
      if(num[x] == '.'):
         count = count + 1;
         if(count > 1):
            print("You idiot!!!");
            return False;
   return True;

#######################################################################
# Function: get_gravitational_force
# Description: get the user input
# Parameters: None
# Return values: float mass1, mass2, dist.
# Pre-Conditions: None
# Post-Conditions: Correct floating number
#######################################################################
def get_gravitational_force():
   mass1 = input("Enter mass 1: ");
   while(not is_valid_num(mass1)):
      mass1 = input("Enter mass 1: ");
   mass2 = input("Enter mass 2: ");
   while(not is_valid_num(mass2)):
      mass2 = input("Enter mass 2: ");
   dist = input("Enter dist: ");
   while(not is_valid_num(dist)):
      dist = input("Enter dist: ");
   return float(mass1), float(mass2), float(dist); 

#######################################################################
# Function: main
# Description: get the mass1, mass2, dist and calculate the F
# Parameters: None
# Return values: None
# Pre-Conditions: correct mass1, mass2, dist
# Post-Conditions: result
#######################################################################
def main():
   condition = 1;
   while condition:
      mass1, mass2, dist = get_gravitational_force();
      G = 6.673*(10**(-8));
      F = (G*mass1*mass2)/(dist**2);
      print(F);
      condition = int(input("Do you want to play again? (1- y, 0 - n): "));
main();
