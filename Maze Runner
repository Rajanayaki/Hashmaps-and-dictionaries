def numberofpaths(rows,col):
  looprange=rows+col-2

  path=1
  for i in range(1,looprange+1):
    path*=i
  rowcount=1
  for i in range(1,rows):
    rowcount*=i
  colcount=1
  for i in range(1,col):
    colcount*=i
  
  totalpath=path//(rowcount*colcount)
  return totalpath


rows,col=map(int,input().split())
pathcount=numberofpaths(rows,col)
pathcount=list(str(pathcount))
pathcount=pathcount[-8:]
pathcount=int("".join(pathcount))
print(pathcount)
