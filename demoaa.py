text='welcome to file handling'
a=open('demoaa.txt','w')
a.write(text)
a.close()



with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)