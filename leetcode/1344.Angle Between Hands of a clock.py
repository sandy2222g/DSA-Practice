class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x=hour+minutes/60
        d=(11*x)%12
        return min(d,12-d)*30