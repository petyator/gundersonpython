from redmine import Redmine
import os
import shutil
import platform

packageNumber = 'v0000 - ' + os.environ['GIT_COMMIT']

if not os.path.isdir('/projects/kulso_projektek/TEKINVEST_1501_LINUXECR/CI/dev-releases/' + packageNumber):
	os.mkdir(packageNumber)
	os.chdir(packageNumber)
	
	redmine = Redmine('https://redmine.frontendart.com', key='31b26e01d916059c8de798f7e62d1965b3e82593')
	project = redmine.project.get('tekinvest_1502_penztargep')
	
	os.mkdir('ProjectManagement')
	os.chdir('ProjectManagement')
	
	trackers = ['Bug','Feature','Task','Refactoring', 'Support']
	statuses = ['New','Assigned','In Progress','Feedback','Rejected','Closed']
	
	for tracker in trackers:
		os.mkdir(tracker)
		os.chdir(tracker)
		for status in statuses:
			for i in project.issues:
				if str(i.tracker) == tracker and str(i.status) == status:
					f = open(status, 'a+')
					f.write('-------------------------------------------------------------------\n')
					f.write('#')
					f.write(str(i.id).encode('UTF-8'))
					f.write(' - ')
					f.write(i.subject.encode('UTF-8'))
					f.write('\n\n')
					f.write(i.description.encode('UTF-8'))
					f.write('\n\n')
					f.close()
		os.chdir('..')
		if not os.listdir(tracker):
			os.removedirs(tracker)
	
	os.chdir('..')
	
	shutil.copytree(os.environ['WORKSPACE'] + '/TEKINVEST_1501_LINUXECR/doc','Doc')
	
	os.mkdir('Doc/wiki')
	os.chdir('Doc/wiki')
	
	for i in project.wiki_pages:
		f = open(i.title, 'w')
		f.write(i.text.encode('UTF-8'))
		f.close()
	
	os.chdir('../..')
	os.mkdir('Src')
	shutil.copy(os.environ['WORKSPACE'] + '/TEKINVEST_1501_LINUXECR/src.zip',os.environ['WORKSPACE'] + '/' + packageNumber + '/Src/src.zip')
	
	shutil.copytree(os.environ['WORKSPACE'] + '/ConfigurationManagement','ConfigurationManagement')
	os.chdir(os.environ['WORKSPACE'] + '/' + packageNumber + '/ConfigurationManagement')
	
	
	f = open('Product_version', 'w')
	f.write("v0000")
	f.write("\n")
	f.write(os.environ['GIT_COMMIT'])
	f.close()
	
	shutil.copytree(os.environ['WORKSPACE'] + '/' + 'tekinvest_bin/Release/x86_64/',os.environ['WORKSPACE'] + '/' + packageNumber + '/' + 'Product')
	os.mkdir(os.environ['WORKSPACE'] + '/' + packageNumber + '/' + 'QA')
	if os.path.isfile(os.environ['WORKSPACE'] + '/TEKINVEST_1501_LINUXECR/test/regTest/style/result.html'):
	    shutil.copy(os.environ['WORKSPACE'] + '/TEKINVEST_1501_LINUXECR/test/regTest/style/result.html',os.environ['WORKSPACE'] + '/' + packageNumber + '/QA/result.html')
	shutil.copytree(os.environ['WORKSPACE'] + '/' + packageNumber + '/','/projects/kulso_projektek/TEKINVEST_1501_LINUXECR/CI/dev-releases/' + packageNumber)