#文字の類似度
import functools

class LevenshteinSimilarity:
    """Levenshtein距離による文字列の類似度を計算する"""

    @functools.lru_cache(maxsize=None)
    def levenshtein_distance(self, a: str, b: str) -> int:
        """文字列間のLevenshtein距離を計算する"""
        if not a:
            return len(b)
        if not b:
            return len(a)
        return min(self.levenshtein_distance(a[1:], b[1:]) + (a[0] != b[0]), self.levenshtein_distance(a[1:], b) + 1,
                   self.levenshtein_distance(a, b[1:]) + 1)

    def __call__(self, a: str, b: str) -> float:
        """文字列の類似度を計算する。類似度は0から1の間で1に近いほど類似度が高い。"""
        distance = self.levenshtein_distance(a, b)
        try:
            return 1 / (distance + 1)
        except ZeroDivisionError:
            return 1
        