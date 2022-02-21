#Basic program to build school administration
import csv
def file_name(information_list):
  with open("Studentss.csv" ,"a", newline='')as csv_file:
    writer = csv.writer(csv_file)
    if csv_file.tell()==0:
      writer.writerow(['Name ','Age','Contact No','Email_Id'])
    writer.writerow(information_list)
if __name__=='__main__':
        condition = True
        student_num = 1
        while condition:
          student_information = input("Enter student #{} information in the format as(Name Age Contact_No Email_Id) : ".format(student_num))
          
          information_lists = student_information.split(' ')
          
          print("\n Entered information is : \n Name : {} \n Age : {} \n Contact_No : {}\n Email_Id : {}".format( information_lists[0],information_lists[1],information_lists[2],information_lists[3] ))
          
          check = input("Is the Entered information is correct(yes/no) : ")
          if check=='yes':
            file_name(information_lists)
            condition_check = input("Enter (yes/no) if you need to enter the information for another student : ")
            if condition_check =='yes':
                condition =True
                student_num=student_num+1
            elif condition_check =='no':
              condition=False
          
          elif check =='no':
            print("Please re enter the data :  ")
          

          

