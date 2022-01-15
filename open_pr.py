#This program will get open PRs
from atlassian import Bitbucket
import datetime

bitbucket = Bitbucket( 
	url = '',  ## Enter the bitbucket url 
	username='', ## Enter the userid 
	password='' )## Enter the password 

project key= ''
repos = bitbucket.repo_list(project_key) 

for repo in repos:
  for repokey, repovalue in repo.items()
    if repokey == "name" : 
	  open_pull_requests = bitbucket.get_pull_requests(project_key, repovalue.lower(), state='OPEN', order='newest', limit=100, start=0)
	  print("Repo ", repovalue) 
	  for pull_req in open_pullrequests :
	    print("pull req details", pull_req['title']) 
		date time_stamp = pull_req["createdDate"] 
		your_dt = datetime.datetime.fromtimestamp(int(date_time_stamp)/1000) #using the local timezone and converting from 10 digit timestamp
		print (your_dt.strftime("%Y-%m-%d %H:%M:%S")) 
