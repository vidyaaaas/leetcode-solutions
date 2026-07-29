class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for s_character, t_character in zip(s, t):
            if (
                s_character in s_to_t
                and s_to_t[s_character] != t_character
            ):
                return False

            if (
                t_character in t_to_s
                and t_to_s[t_character] != s_character
            ):
                return False

            s_to_t[s_character] = t_character
            t_to_s[t_character] = s_character

        return True
