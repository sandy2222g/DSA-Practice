class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n=len(rooms)
        v={0}
        q=rooms[0]
        while q:
            c=q.pop()
            if c not in v:
                q.extend(rooms[c])
                v.add(c)
        return len(v)==n
obj=Solution()
print(obj.canVisitAllRooms([[1],[2],[3],[]]))