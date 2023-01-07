n, m = map(int, input().split())
# n is for grid
#m is for number of cases
#delivery_map = [[0 for _ in range(n)] for _ in range(n)]
dd={}
def bfs(x,y,r):
  x-=1
  y-=1
  local_ans=0
  for a in range(max(0,x-r),min(n,x+r+1)):
    for b in range(max(0,y-r),min(n,y+r+1)):
      #calculate distance
      if abs(a-x) + abs(b-y) <=r:
        #delivery_map[a][b]+=1
        dd[(a,b)]=1 + dd.get((a,b),0)
        local_ans=max(local_ans,dd[(a,b)])
  return local_ans
        
for x in range(m):
  x_co,y_co,step_size=map(int, input().split())
  ans=bfs(x_co,y_co,step_size)
#print(dd)
#print(ans)
  
            
