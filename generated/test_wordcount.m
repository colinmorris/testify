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
  NSDictionary* actual = [[[WordCount alloc] initWithString:@"word"] count];
  NSDictionary* expected = @{ @"word" : @1};
  XCTAssertEqualObjects(actual, expected);
}

@end

