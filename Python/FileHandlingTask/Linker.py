import os

path=r"E:\Work\Maang-Work\BootCamp\Python\FileHandlingTask"
target="Vaibhav"

for f in os.listdir(path):
    if f.endswith(".txt"):

        filename=os.path.join(path,f)
        print("File:"+filename)

        cnt=0

        with open(filename) as file:
            for line in file:
                cnt+=line.count(target)

        print("Count of 'Vaibhav':"+str(cnt))
        print("----------------------------------")

