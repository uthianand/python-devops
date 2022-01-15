This program will delete default reviewer records with 0 reviewers at repo level
from atlassian import Bitbucket 

bitbucket = Bitbucket( 
	url = '',  ## Enter the bitbucket url 
	username='', ## Enter the userid 
	password='' )## Enter the password 
	
project_key='' ## Enter the project key 
repos = bitbucket.repo_list(project_key) 
	
for repo in repos: 
  for repokey, repovalue in repo.items (): 
    if repokey == "name":
      reporeviewer_conditions = bitbucket.get_repo_conditions(project_key, repovalue. lower0) 
	  print("Repo ", repovalue) 
	  for review in repo reviewer_conditions: 
	    review_id = review["id"] 
		review_type = review["scope"] 
		review_ref = review["targetRefMatcher"] 
		review_reviewers = review["reviewers"] 
		if reviewtype["type"] s "REPOSITORY" and len(review.reviewers) == 0 : 
		   print("Review record to be deleted: ", review) 
		   bitbucket.delete_repo_condition(project_key, repovalue.lower(), review_id)
		   print("Deleted record: ", review_ref["id"]) 