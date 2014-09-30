#import <XCTest/XCTest.h>
#import "hamming.h"


@interface test_suite : XCTestCase

@end

@implementation test_suite
- (void)testEmptyStrings {
  NSUInteger actual = [Hamming compute:@"" against:@""];
  NSUInteger expected = @0;
  XCTAssertEqual(actual, expected);
}

- (void)testOneNucleotideSame {
  NSUInteger actual = [Hamming compute:@"A" against:@"A"];
  NSUInteger expected = @0;
  XCTAssertEqual(actual, expected);
}

- (void)testOneNucleotideDifferent {
  NSUInteger actual = [Hamming compute:@"A" against:@"G"];
  NSUInteger expected = @1;
  XCTAssertEqual(actual, expected);
}

- (void)testShortNonequal {
  NSUInteger actual = [Hamming compute:@"AT" against:@"CT"];
  NSUInteger expected = @1;
  XCTAssertEqual(actual, expected);
}

- (void)testShortNoMatches {
  NSUInteger actual = [Hamming compute:@"AG" against:@"CT"];
  NSUInteger expected = @2;
  XCTAssertEqual(actual, expected);
}

- (void)testLongNonequal {
  NSUInteger actual = [Hamming compute:@"GGACGA" against:@"GGTCGA"];
  NSUInteger expected = @4;
  XCTAssertEqual(actual, expected);
}

@end

