


with open('log.txt', 'r') as rf:
    with open ('log_new.txt', 'w') as wf:

        x = rf.readlines()[1][28:]
        wf.writelines(x)

with open('log.txt', 'r') as rf1:
    with open('log_new.txt', 'a') as wf1:
        contents = rf1.read()
        count = contents.count("launched")
        wf1.write("The application has started "+str(count)+" times\n")

with open('log.txt', 'r') as rf3:
    with open('log_new.txt', 'a') as wf3:
        warnings = rf3.read().lower().count("warning")

        if (warnings > 0):
            wf3.write("There are "+ str(warnings)+" warnings,")
        else:
            wf3.write("There is no warning in this file.")

with open('log.txt', 'r') as rf4:
    with open('log_new.txt', 'a') as wf4:
        errors = rf4.read().lower().count("error")
        if (errors > 0):
            wf4.write(" and "+str(errors)+" errors.\n")
        else:
            wf4.write("There is no error in this file.\n")

with open('log.txt', 'r') as rf5:
    with open('log_new.txt', 'a') as wf5:
        number = 0
        for line in rf5:
            for part in line.split():
                if "Error" in part:

                    number += 1
                    wf5.write(str(number)+". Crash occured at " + str(line[11:19]+ "\n"))



