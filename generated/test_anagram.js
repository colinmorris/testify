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

  it("does not confuse different duplicates", function() {
    var expected = [];
    expect(detect_anagrams("galea", ["eagle"])).toEqual(expected);
  });

  it("eliminates anagram subsets", function() {
    var expected = [];
    expect(detect_anagrams("good", ["dog", "goody"])).toEqual(expected);
  });

  it("detects multiple anagrams", function() {
    var expected = ["gallery", "regally", "largely"];
    expect(detect_anagrams("allergy", ["gallery", "ballerina", "regally", "clergy", "largely", "leading"])).toEqual(expected);
  });

  it("same word isnt anagram", function() {
    var expected = [];
    expect(detect_anagrams("banana", ["banana"])).toEqual(expected);
  });

  it("is case insensitive", function() {
    var expected = ["Orchestra"];
    expect(detect_anagrams("Orchestra", ["cashregister", "Carthorse", "radishes"])).toEqual(expected);
  });

});

