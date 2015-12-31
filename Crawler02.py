import re, urllib

textfile = file('depth_2.txt','wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'

#myurl = input("@> ")

myurl = "http://www.gobiernotransparentechile.cl/directorio/servicios"

j=1

for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print "Level 0 " + i  
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
			print "Level 1 " + ee
			for ff in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(ee).read(), re.I):
				print "%i %s" %(j,ff)
				textfile.write(ff+'\n')
				j=j+1
				
textfile.close()