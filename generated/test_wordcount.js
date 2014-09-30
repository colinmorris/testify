var word_count = require('./wordcount');


describe("word_count()", function() {
  it("counts one word", function() {
    var expected = {"word": 1};
    expect(word_count("word")).toEqual(expected);
  });

  it("counts one of each", function() {
    var expected = {"word": 1};
    expect(word_count("word")).toEqual(expected);
  });

});

