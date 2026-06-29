class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1:
            return -1
        
        queue = deque()
        visit = set()
        queue.append((0,0))
        visit.add((0,0))

        length = 1

        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == n-1 and c == n - 1:
                    return length
                
                neighbours = [[0,1], [1,1], [1,0], [1, -1], [0, -1], [-1,-1], [-1, 0], [-1,1]]
                for neighbour in neighbours:
                    dr, dc = neighbour
                    new_r = r + dr
                    new_c = c + dc

                    if new_r < 0 or new_c < 0 or new_r == n or new_c == n or (new_r, new_c) in visit or grid[new_r][new_c] == 1:
                        continue
                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))

            length += 1
        return -1
            