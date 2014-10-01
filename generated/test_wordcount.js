var word_count = require('./wordcount');


describe("word_count()", function() {
  it("counts one word", function() {
    var expected = {"word": 1};
    expect(word_count("word")).toEqual(expected);
  });

  it("counts one of each", function() {
    var expected = {"of": 1, "each": 1, "one": 1};
    expect(word_count("one of each")).toEqual(expected);
  });

  it("counts multiple occurences", function() {
    var expected = {"blue": 1, "fish": 4, "two": 1, "red": 1, "one": 1};
    expect(word_count("one fish two fish red fish blue fish")).toEqual(expected);
  });

  it("preserves punctuation", function() {
    var expected = {"java": 1, "javascript!!&@$%^&": 1, "car": 1, "as": 1, ":": 2, "carpet": 1};
    expect(word_count("car : carpet as java : javascript!!&@$%^&")).toEqual(expected);
  });

  it("includes numbers", function() {
    var expected = {"1": 1, "2": 1, "testing": 2};
    expect(word_count("testing 1 2 testing")).toEqual(expected);
  });

  it("preserves mixed case", function() {
    var expected = {"go": 1, "Go": 1, "GO": 1};
    expect(word_count("Go go GO")).toEqual(expected);
  });

  it("multiple spaces", function() {
    var expected = {"it": 1, "for": 1, "wait": 1};
    expect(word_count("wait for     it")).toEqual(expected);
  });

  it("splits on newlines", function() {
    var expected = {"ma": 1, "want": 1, "oh": 1, "ah": 3, "la": 2, "rah": 2, "romance": 1, "bad": 1, "ga": 2, "roma": 2, "your": 1};
    expect(word_count("rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your bad romance")).toEqual(expected);
  });

});

