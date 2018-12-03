from github import Github
import json


output = "/data.json"
g = Github("b9cd6f594a4d01c8e6e1cf6a14f42c0d6c165559")

repo = g.get_repo("PyGithub/PyGithub")

# j = repo.get_stats_participation()
j = repo.get_commits()
lengthJ = j.totalCount

linesOfCode = 0
authorContributions = {}
locCount = []
#
for x in range(lengthJ):
    com = j[x]
    # print(j[x].author.login)
    if com is not None:
        if com.author is not None:
            commitAuthor = com.author.login

            # print(commitAuthor)
            if (commitAuthor in authorContributions):
                contributions = authorContributions[commitAuthor]
                authorContributions[commitAuthor] = contributions + 1
            else:
                authorContributions[commitAuthor] = 1

        linesOfCode += com.stats.additions - com.stats.deletions
        locCount.append(linesOfCode)
#
#
#
print(linesOfCode)
# # # l = j.all
# json_str = json.dumps(authorContributions)
# with open("authors.json", 'w') as outfile:
#     json.dump(json_str , outfile)

# print(j.all)
