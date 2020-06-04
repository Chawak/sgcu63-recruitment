import json
path_list=[]
def dfs(current,previous,fileToSearch,path,count):
  if current==fileToSearch and previous=="_files": #check if current is file to search 
    path_list.append([count,path+"/"+current])
  elif isinstance(current,dict):
    for key,value in current.items():
      if key=="_files":
        dfs(value,key,fileToSearch,path,count+1)
      else:
        dfs(value,key,fileToSearch,path+"/"+key,count+1)
  elif isinstance(current,list):
    for i in current:
      dfs(i,previous,fileToSearch,path,count)

def fileSearch(fileToSearch, filesObj): 
  json_path=json.loads(filesObj)
  for key,value in json_path.items():
    dfs(value,key,fileToSearch,"/"+key,1)
  ans=[path for count,path in sorted(path_list)]
  return ans
S=""" {"FolderA": {"_files": [ "file1", "file2" ] ,"SubfolderC": {"_files": [ "file1" ]} ,"SubfolderB": {"_files" : [ "file1" ]}}}"""
print(fileSearch("file1",S)) 