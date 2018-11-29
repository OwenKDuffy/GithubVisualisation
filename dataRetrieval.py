from github import Github
import json
output = "/data.json"
g = Github("b9cd6f594a4d01c8e6e1cf6a14f42c0d6c165559")

repo = g.get_repo("PyGithub/PyGithub")

j = repo.get_stats_participation()
l = j.all
with open("docs/data.json", 'w') as outfile:
    json.dump(l , outfile)

# print(j.all)
