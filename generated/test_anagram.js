var detect_anagrams = require('./anagram');


describe("detect_anagrams()", function() {
  it("no matches", function() {
    var expected = [];
    expect(detect_anagrams("diaper", ["hello", "world", "zombies", "pants"])).toEqual(expected);
  });

  it("detects simple anagram", function() {
    var expected = ["tan"];
    expect(detect_anagrams("ant", ["tan", "stand", "at"])).toEqual(expected);
  });

});

