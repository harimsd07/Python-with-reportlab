
"""
Version : v2.0
     v2 - 08/09/2017 - get_employee_count() Employee count calculated with helping verb
     v2.0 - 12/09/2017 - secondary_filteration() has been added for some more special handling to get employee count

Pending : Nill
"""

import re
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

class EmployeeCount:
    def __init__(self, developer_mode = True):
        self.developer_mode = developer_mode
        self.employee_keywords = ['employees','people','staff','staff,','people.','employees.','employees,','people,','staff.','associates','assistants.','individuals.','individuals','professionals','employee','associates,','workforce','employers']
        self.templist = []
        self.commas = [',',' ,',', ']
        self.helping_verb = ['passionate','full-time','experienced','committed','loyal','enthusiastic','Charlotte','Dedicated','global','fewer','corporate','exceptional','co-op','qualified','wonderful','valued','new','technical','part-time','skilled','care','conscientious','hardworking','permanent','service','outstanding','dedicated','full-service','time','k','directly-employed','total','plus','local','caring','service-oriented','Rosaprima','Full-time','tight-knit','talented']
        self.helping_verb_sec_fil = ['employs','employ','employing','employees','employees:','employed','employee','employees','employment']
        self.f1 = ''

    def get_employee_count(self,description,company_name):#primary_filteration
        try:
            is_matched = False
            description_split = description.split()
            #print description
            for word in self.employee_keywords:
                if word in description_split :
                    if self.developer_mode:
                        print (description_split.index(word)-1,'word',word,'description',description_split)
                    index1 = description_split.index(word)-1
                    if self.developer_mode:
                        print (description_split[index1])
                    # if word == 'employees:':
                        # index1 = description_split[description_split.index(word):description_split.index(word)+3]
                        # for ele in index1:
                            # regexp = re.findall("\$?([0-9,]+)[.%]?",ele)
                            # if ele.isdigit()or regexp:
                                # print 'pass'
                                # file_objc.final_list(company_name,ele)
                                # print 'done'
                    regexp = re.findall("\$?([0-9,]+)[.%]?",description_split[index1])
                    if description_split[index1].isdigit()or regexp:#checks for immediate count before selected keywords
                        #print 'pass',employee_count
                        is_matched = True
                        acc = company_name
                        if acc not in self.templist:
                            self.templist.append(acc)
                            file_objc.final_list(company_name,description,description_split[index1])
                    else:
                        for i in self.helping_verb:
                            if i == description_split[index1]:
                                try:
                                    index2 = description_split[description_split.index(word)-6:description_split.index(word)]
                                except Exception:
                                    index2 = description_split[description_split.index(word)-2:description_split.index(word)]
                                if self.developer_mode:
                                    print ('new',index2)
                                for ele in index2:
                                    #print ele
                                    regexp = re.findall("\$?([0-9,]+)[.%]?",ele)
                                    if ele.isdigit()or regexp:
                                        if self.developer_mode:
                                            print ('pass',ele)
                                        is_matched = True
                                        acc = company_name
                                        if self.helping_verb == 'k':
                                            ele = ele+'k'
                                        if acc not in self.templist:
                                            self.templist.append(acc)
                                            file_objc.final_list(company_name,description,ele)
            if not is_matched: # is not match code
                acc = str(company_name)+'\t'+str(description)
                self.secondary_filteration(company_name,description)
        except Exception as e:
            print (e)

    def secondary_filteration(self,company_name,description):
        if self.developer_mode:
            print ('entered secondary_filteration')
        is_matched = False
        description_split = description.split()
        if self.developer_mode:
            print (description_split)
        for word in self.helping_verb_sec_fil:
            if word in description_split :
                if self.developer_mode:
                    print (description_split.index(word)-1,'word',word,'description',description_split)
                try:
                    index2 = description_split[description_split.index(word):description_split.index(word)+7]
                except Exception:
                    index2 = description_split[description_split.index(word):description_split.index(word)+3]
                for ele in index2:
                    regexp = re.findall("\$?([0-9,]+)[.%]?",ele)
                    if ele.isdigit()or regexp:#checks for  count for cretain indexes from selected keywords
                        #print 'pass',ele
                        is_matched = True
                        acc = company_name
                        if acc not in self.templist:
                            self.templist.append(acc)
                            file_objc.final_list(company_name,description,ele)
        if not is_matched: # is not match code
            acc = str(company_name)+'\t'+str(description)+'\n'
            #print 'acc',acc
            with open('a',errors='ignore') as f1:
            #self.f1.write('company_name\tdescription\n')
                f1.write(acc)
            file_objc.null_final_list(company_name,description)
class Files:
    def __init__(self,developer_mode= False):
        self.developer_mode=developer_mode
        self.write_filename=''
        self.final_result=''

    def get_input_from_file(self):
        if len(sys.argv) >1:
             filename = sys.argv[1]
             temp_filename=filename.split('.')[0]
             self.write_filename=str(temp_filename)+('_output.txt')
             if self.developer_mode:
                 print (self.write_filename)
             self.f = open(self.write_filename,'w')
             self.f.write('company_name\temp_count\n')
        else:
            if self.developer_mode:
                print ("Please Enter the Filename")
            exit()
        self.developer_mode = False
        with open(filename,'r',errors='ignore') as fopen:
            company_list = fopen.read().split("\n")
        for index, company_data in enumerate(company_list):
            company_name, description = company_data.split('\t')
            if self.developer_mode:
                print ("\n\n",index, company_name,description)
            objec.get_employee_count(description,company_name)

    def null_final_list(self,company_name,description):#final list of matched correct numbers
        redundancy_list = []
        self.final_result = str(company_name)+ '\t' +str(description)+ '\t'+ '\n'
        if company_name not in redundancy_list:
            redundancy_list.append(company_name)
            self.file_write(self.final_result)

    def final_list(self,company_name,description,emp_count):#final list of matched correct numbers
         redundancy_list = []
         #print 'emp_count',emp_count
         if ',' in emp_count:
             values=emp_count.split(',')
             for i in values:
                 if i.isdigit():
                     print ('Type Int ')
                     if company_name not in redundancy_list:
                         redundancy_list.append(company_name)
                         self.final_result = str(company_name) + '\t' +str(description)+ '\t' + str(emp_count) + '\n'
                         self.file_write(self.final_result)
                 else:
                     if company_name not in redundancy_list:
                         redundancy_list.append(company_name)
                         self.null_final_list(company_name)
                     # if emp_count.split(',')[0].isdigit() and emp_count.split(',')[1].isdigit():
            
         else:
             self.final_result = str(company_name) + '\t' +str(description)+ '\t' + str(emp_count) + '\n'
             if company_name not in redundancy_list:
                 redundancy_list.append(company_name)
                 self.file_write(self.final_result)

    def file_write(self,final_result):#file write for matched numbers (correct numbers without ISD code)
        self.f.write(self.final_result)

if __name__ == '__main__':
    objec = EmployeeCount()
    file_objc = Files()
    file_objc.get_input_from_file()
