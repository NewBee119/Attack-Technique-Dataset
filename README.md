# Attack-Technique-Dataset
A dataset containing APT group related articles and MITRE ATT&amp;CK technique descriptions
## MitreEnterprise.json
* A summary of attack techniques, collected from https://attack.mitre.org/techniques/enterprise/
* Each techniques has a description and a full description.
## APTgroupMitre.json
* A summary of APT group with its used attack techniques and relted articles (references), colleted form https://attack.mitre.org/groups/
## tech_refer.json
* A summary of threat-related artilces. Each url (artilces) can be found in APTgroupMitre.json and related to several techniques that can be found in MitreEnterprise.json
## _id.txt
* Get each url in tech_refer an id.
## references
* This fold contains artilces(urls) described in _id.txt, and each the file name exactly means the id described in _id.txt.The file in references containing html file and Users can use the script deal_raw_file.py to make a classification.
## references_processed
* Some preprocessed file are listed for users.
