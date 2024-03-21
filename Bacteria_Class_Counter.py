#!/usr/bin/env python
import re
# This is a program to extract data from a FAPROTAX file in which the starting metadata lines are removed. It will output a tab seperated .txt document that holds a list of funtional tags and the numbers of each tax level that have them. Currently it will only do one tax level at a time, specified by chaning the parenthesis in the re.find line.

functionfile = "./silva_allgroups_taxtable_1-27-24-filt-norm_report.txt"
header = "functionality\tfunction_total\tdomain\tphylum\tclass\torder\tfamily\tgenus\tspecies\tcount\torder_total\n"
#FunctionDict = {} #holds function as key and number of bacteria with that function as value
currfunction = "" #holds current function
currfunction_total = 000 #holds total number of bacteria mapped to that function, used for metadata and data validation checks
taxDict = {} #holds taxonomy as tab seperated string as key and number seen as value

odict = {} #used for order relative abundance calculations
with open(functionfile, "r") as file:
    for line in file:
        if line.strip(): #skips blank lines
            if line[0] != "#": #if a taxonomy line, grab tax levels individually
                o = str(re.findall(r'o__([A-Za-z]+);', line))
                o=o[2: len(o) - 2]
                if not o in odict.keys():
                    odict[o]=1
                else:
                    odict[o] = (int(odict[o]) + 1)


with open(functionfile, "r") as file, open("Funtional_Taxonomy_Report.txt", "w") as output:
    #puts header in out file
    output.write(header)
    #grabs the first record
    line=file.readline()
    currfunction = str(re.findall(r'# ([A-Za-z_]+) \(\d+ records\):', line))
    currfunction_total = str(re.findall(r'# [A-Za-z_]+ \((\d+) records\):', line))
    currfunction=currfunction[2: len(currfunction) - 2] #removes surounding [''] from re return
    currfunction_total=currfunction_total[2: len(currfunction_total) - 2]
    #iterate through file
    curr=0
    for line in file:
        if line.strip(): #skips blank lines
            if line[0] != "#": #if a taxonomy line, grab tax levels individually
                d = str(re.findall(r'd__([A-Za-z]+);', line))
                d=d[2: len(d) - 2] #removes surounding [''] from re return
                p = str(re.findall(r'p__([A-Za-z]+);', line))
                p=p[2: len(p) - 2]
                c = str(re.findall(r'c__([A-Za-z]+);', line))
                c=c[2: len(c) - 2]
                o = str(re.findall(r'o__([A-Za-z]+);', line))
                o=o[2: len(o) - 2]
                f = str(re.findall(r'f__([A-Za-z]+);', line))
                f=f[2: len(f) - 2]
                g = str(re.findall(r'g__([A-Za-z]+);', line))
                g=g[2: len(g) - 2]
                s = str(re.findall(r's__([A-Za-z]+);', line))
                s=s[2: len(s) - 2]
                tax = ("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (d, p, c, o, f, g, s))
                if not tax in taxDict.keys():
                    taxDict[tax] = 1
                else:
                    taxDict[tax] = (int(taxDict[tax]) + 1)
            else: #if the functionality line, denoted by a #
                total=0
                if currfunction_total:
                    curr=int(currfunction_total)
                for value in taxDict.values():
                    total = total+value
                if not(total == curr):
                    print ("Wrong total for",currfunction," total: ",total," expected: ",currfunction_total,"*ignore if empty, test is working as intended")
                if currfunction_total == 0: #skips unmapped functions
                    continue
                for tax, value in taxDict.items():
                    order = str(re.findall(r'[A-Za-z]+\t[A-Za-z]+\t[A-Za-z]+\t([A-Za-z]+)', tax))
                    order=order[2: len(order) - 2]
                    ototal = odict[order]
                    outline = ("%s\t%s\t%s\t%s\t%s\n" % (currfunction, currfunction_total, tax, value, ototal))
                    output.write(outline)
                taxDict.clear()
                currfunction = str(re.findall(r'# ([A-Za-z_]+) \(\d+ records\):', line))
                currfunction_total = str(re.findall(r'# [A-Za-z_]+ \((\d+) records\):', line))
                currfunction=currfunction[2: len(currfunction) - 2] #removes surounding [''] from re return
                currfunction_total=currfunction_total[2: len(currfunction_total) - 2]
                #outputs final record (wihtout # trigger)
    for tax, value in taxDict.items():
        order = str(re.findall(r'[A-Za-z]+\t[A-Za-z]+\t[A-Za-z]+\t([A-Za-z]+)', tax))
        order=order[2: len(order) - 2]
        ototal = odict[order]
        outline = ("%s\t%s\t%s\t%s\t%s\n" % (currfunction, currfunction_total, tax, value, ototal))
        output.write(outline)
