from typing import List

# 733 Flood Fill

# depth first search
class Solution:
    def floodFill(self, image: List[List[int]], x: int, y: int, newColor: int) -> List[List[int]]:
        if image[x][y] != newColor:
            old, image[x][y], m, n = image[x][y], newColor, len(image), len(image[0])
            for i, j in zip((x, x + 1, x, x - 1), (y + 1, y, y - 1, y)):
                if 0 <= i < m and 0 <= j < n and image[i][j] == old:
                    self.floodFill(image, i, j, newColor)
        return image


