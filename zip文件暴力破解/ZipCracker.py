import zipfile
import threading

#z_file=zipfile.ZipFile("test.zip","r")
#z_file.extractall(pwd = "sly520".encode())


class ZipCracker(threading.Thread):
     '''zip file brute force mechine'''

     thread_list=[]

     @staticmethod
     def CrackZip(dic_list,target_file):

         thread_index =0
         ret=[]
         for dic_lib in dic_list:

              thread_index+=1
              temp_thread=ZipCracker(target_file,dic_lib,thread_index)
              temp_thread.start()
              ZipCracker.thread_list.append(temp_thread)
              print("cracker thread:",thread_index,"has started")

     def __init__(self,target_file,pwd_dictionary,index):

          threading.Thread.__init__(self)
          self.z_file=zipfile.ZipFile(target_file,"r")
          self.pwd_number=0
          self.pwd_dictionary=pwd_dictionary
          self.index=index
          self.stop=False

     def __shutdown(self):

         for cracker in ZipCracker.thread_list:

             cracker.Stop()
         print("all thread has shutdown")

     def Stop(self):

          print("thread:",self.index,"has shut down...")
          self.stop=True

     def __test_pwd(self,pwd):
          '''test the pwd if right'''

          self.pwd_number+=1

          if self.pwd_number%10000==0:

               print("thread:",self.index,"----",self.pwd_number," pwd has tested...")
          try:
               self.z_file.extractall(pwd=pwd.encode())
               print("password has founded!!!","target zipfile password is:----",pwd)
               print("ready to shut down all threads...")
               self.__shutdown()
               return True
          except:
               return False


     def run(self):
          '''start to test all password'''

          '''pwd_lib=open(self.pwd_dictionary,"r")
          for line in pwd_lib.readlines():
               #read all password and test

               password=line.strip("\n")
               if self.__test_pwd(password):

                    print("try password number:",self.pwd_number)'''
          pwd_index=0
          pwd_lib=open(self.pwd_dictionary,"r")
          dic_lib=pwd_lib.readlines()
          
          
          while not self.stop:

               try:
                    
                    password=dic_lib[pwd_index].strip("\n")
                    pwd_index+=1
                    if self.__test_pwd(password):

                         print("try password number:",self.pwd_number)
                    

               except Exception as e:

                    self.Stop()
                    

          

#"(101W-200W).TXT","2016passworddic.txt",
dic=["2016passworddic.txt"]
ZipCracker.CrackZip(dic,"Flask.zip")

