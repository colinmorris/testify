var isLeapYear = require('./leap');


describe("isLeapYear()", function() {
  it("a known leap year", function() {
    var expected = true;
    expect(isLeapYear(1996)).toEqual(expected);
  });

  it("any old year", function() {
    var expected = false;
    expect(isLeapYear(1997)).toEqual(expected);
  });

  it("non leap even year", function() {
    var expected = false;
    expect(isLeapYear(1998)).toEqual(expected);
  });

  it("century", function() {
    var expected = false;
    expect(isLeapYear(1900)).toEqual(expected);
  });

  it("exceptional century", function() {
    var expected = true;
    expect(isLeapYear(2400)).toEqual(expected);
  });

});

