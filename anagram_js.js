var isAnagram = function (s, t) {
    return Array.from(s).sort().join("") === Array.from(t).sort().join("");
};

console.log(isAnagram("anagram", "anagram"));
console.log(isAnagram("rat", "cat"));
