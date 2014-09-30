#import <XCTest/XCTest.h>
#import "anagram.h"


@interface test_suite : XCTestCase

@end

@implementation test_suite
- (void)testNoMatches {
  NSArray* actual = [[[Anagram alloc] initWithString:@"diaper"] match:@[@"hello", @"world", @"zombies", @"pants"];
  NSArray* expected = @[];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testDetectsSimpleAnagram {
  NSArray* actual = [[[Anagram alloc] initWithString:@"ant"] match:@[@"tan", @"stand", @"at"];
  NSArray* expected = @[@"tan"];
  XCTAssertEqualObjects(actual, expected);
}

@end

