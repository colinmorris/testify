#import <XCTest/XCTest.h>
#import "anagram.h"


@interface test_suite : XCTestCase

@end

@implementation test_suite
- (void)testNoMatches {
  NSArray* actual = [[[Anagram alloc] initWithString:@"diaper"] match:@[@"hello", @"world", @"zombies", @"pants"]];
  NSArray* expected = @[];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testDetectsSimpleAnagram {
  NSArray* actual = [[[Anagram alloc] initWithString:@"ant"] match:@[@"tan", @"stand", @"at"]];
  NSArray* expected = @[@"tan"];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testDoesNotConfuseDifferentDuplicates {
  NSArray* actual = [[[Anagram alloc] initWithString:@"galea"] match:@[@"eagle"]];
  NSArray* expected = @[];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testEliminatesAnagramSubsets {
  NSArray* actual = [[[Anagram alloc] initWithString:@"good"] match:@[@"dog", @"goody"]];
  NSArray* expected = @[];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testDetectsMultipleAnagrams {
  NSArray* actual = [[[Anagram alloc] initWithString:@"allergy"] match:@[@"gallery", @"ballerina", @"regally", @"clergy", @"largely", @"leading"]];
  NSArray* expected = @[@"gallery", @"regally", @"largely"];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testSameWordIsntAnagram {
  NSArray* actual = [[[Anagram alloc] initWithString:@"banana"] match:@[@"banana"]];
  NSArray* expected = @[];
  XCTAssertEqualObjects(actual, expected);
}

- (void)testIsCaseInsensitive {
  NSArray* actual = [[[Anagram alloc] initWithString:@"Orchestra"] match:@[@"cashregister", @"Carthorse", @"radishes"]];
  NSArray* expected = @[@"Orchestra"];
  XCTAssertEqualObjects(actual, expected);
}

@end

