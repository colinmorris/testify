var hamming = require('./hamming');


describe("hamming()", function() {
  it("empty strings", function() {
    var expected = 0;
    expect(hamming("", "")).toEqual(expected);
  });

  it("one nucleotide same", function() {
    var expected = 0;
    expect(hamming("A", "A")).toEqual(expected);
  });

  it("one nucleotide different", function() {
    var expected = 1;
    expect(hamming("A", "G")).toEqual(expected);
  });

  it("short nonequal", function() {
    var expected = 1;
    expect(hamming("AT", "CT")).toEqual(expected);
  });

  it("short no matches", function() {
    var expected = 2;
    expect(hamming("AG", "CT")).toEqual(expected);
  });

  it("long nonequal", function() {
    var expected = 4;
    expect(hamming("GGACGA", "GGTCGA")).toEqual(expected);
  });

});

