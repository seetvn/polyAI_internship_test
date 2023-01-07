
def bfs(x,y,dimension,res):
  """
  """
  x-=1
  y-=1
  ans_display=[["0" for i in range(dimension)]for i in range(dimension)]
  queue=[(x,y)]
  visited=[(x,y)]
  while queue:
    r,c=queue.pop(0)
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    for x_dir,y_dir in directions:
      new_r,new_c=r + x_dir,c + y_dir
      x_mag=abs(new_r-x)
      y_mag=abs(new_c-y)
      if new_r in range(dimension) and new_c in range(dimension) and (new_r,new_c) not in visited and x_mag + y_mag <= res:
      
        queue.append((new_r,new_c))
        visited.append((new_r,new_c))
        ans_display[new_r][new_c]="X"
  
  ans_display[x][y]="T"
  return ans_display

ans=bfs(1,1,4,2)
for x in range(len(ans)):
  print(ans[x])
  print("")
  
  
  