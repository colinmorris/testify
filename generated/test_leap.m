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

- (void)testNonLeapEvenYear {
  XCTAssert(![[[Year alloc] initWithCalendarYear:@1998] isLeapYear]);
}

- (void)testCentury {
  XCTAssert(![[[Year alloc] initWithCalendarYear:@1900] isLeapYear]);
}

- (void)testExceptionalCentury {
  XCTAssert([[[Year alloc] initWithCalendarYear:@2400] isLeapYear]);
}

@end

