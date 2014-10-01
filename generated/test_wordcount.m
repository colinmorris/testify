#import <XCTest/XCTest.h>
#import "wordcount.h"


@interface test_suite : XCTestCase

@end

@implementation test_suite
- (void)testCountsOneWord {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"word"] count];
  NSDictionary* expected = @{ @"word" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testCountsOneOfEach {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"one of each"] count];
  NSDictionary* expected = @{ @"of" : @1, @"each" : @1, @"one" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testCountsMultipleOccurences {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"one fish two fish red fish blue fish"] count];
  NSDictionary* expected = @{ @"blue" : @1, @"fish" : @4, @"two" : @1, @"red" : @1, @"one" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testPreservesPunctuation {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"car : carpet as java : javascript!!&@$%^&"] count];
  NSDictionary* expected = @{ @"java" : @1, @"javascript!!&@$%^&" : @1, @"car" : @1, @"as" : @1, @":" : @2, @"carpet" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testIncludesNumbers {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"testing 1 2 testing"] count];
  NSDictionary* expected = @{ @"1" : @1, @"2" : @1, @"testing" : @2};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testPreservesMixedCase {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"Go go GO"] count];
  NSDictionary* expected = @{ @"go" : @1, @"Go" : @1, @"GO" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testMultipleSpaces {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"wait for     it"] count];
  NSDictionary* expected = @{ @"it" : @1, @"for" : @1, @"wait" : @1};
  XCTAssertEqualObjects(actual, expected);
}

- (void)testSplitsOnNewlines {
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"rah rah ah ah ah\nroma roma ma\nga ga oh la la\nwant your bad romance"] count];
  NSDictionary* expected = @{ @"ma" : @1, @"want" : @1, @"oh" : @1, @"ah" : @3, @"la" : @2, @"rah" : @2, @"romance" : @1, @"bad" : @1, @"ga" : @2, @"roma" : @2, @"your" : @1};
  XCTAssertEqualObjects(actual, expected);
}

@end

