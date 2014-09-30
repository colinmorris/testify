#import <XCTest/XCTest.h>
#import "leap.h"


@interface test_suite : XCTestCase

@end

@implementation test_suite
- (void)testAKnownLeapYear {
  XCTAssert([[[Year alloc] initWithCalendarYear:@1996] isLeapYear]);
}

- (void)testAnyOldYear {
  XCTAssert(![[[Year alloc] initWithCalendarYear:@1997] isLeapYear]);
}

@end

