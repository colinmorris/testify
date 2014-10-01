import json
import sys


# Decorator for methods in TestGen subclasses. Allows a method to yield a series of 
# strings (or (str, int) tuples), which will be appended as standalone lines to 
# the object's internal accumulator which is building up the text of the full unit test suite.
def glommer(method_or_default_indentation):
  # Hackish implementation of decorator with optional argument (http://stackoverflow.com/questions/3888158/python-making-decorators-with-optional-arguments)
  arg = isinstance(method_or_default_indentation, int)
  default_indentation = method_or_default_indentation if arg else 0
  
  def glommer_(fun):
    def inner(self, *args):
      for line_obj in fun(self, *args):
        if line_obj is None:
          # An empty yield in a glommer is like an empty print
          self.add_spacer()
        elif isinstance(line_obj, tuple):
          # If an indentation is specified, it should override the number passed to the decorator
          (line, indentation) = line_obj
          self.add_line(line, indentation)
        else:
          assert isinstance(line_obj, basestring)
          self.add_line(line_obj, default_indentation)
    return inner
  if arg:
    return glommer_
  else:
    return glommer_(method_or_default_indentation)

# TODO: Maybe have a separate class for test cases?


def namify(name, naming_style):
  """Given a name consisting of one or more lowercase tokens separated by spaces, 
  return a corresponding variable name in the given style (e.g. "camel", "pothole").
  """
  tokens = name.split()
  
  if naming_style == 'pothole':
    return '_'.join(tokens)
    
  elif naming_style == 'camel':
    return ''.join(token.capitalize() for token in tokens)
    
  else:
    raise NotImplementedError("No handling for naming style " + str(naming_style))


class TestGen(object):
  """This is an abstract class defining a framework for generating a unit test suite 
  given a language-independent description of a problem and some inputs and expected outputs.
  
  Subclasses are responsible for defining language-specific logic for writing unit tests,
  converting between types, etc.  
  """
  
  LANG = "null"
  # Naming style for functions
  FUN_NAMING = "pothole"
  # Naming style for classes
  CLASS_NAMING = "camel"
  
  # The unit of indentation
  IND = '  '
  
  def __init__(self, problem):
    self.problem = problem
    self.name = problem['name']
    self.fun = namify(problem['function'], self.FUN_NAMING)
    self.module = problem['module']
    # A string that acumulates the whole text of the unit test suite
    self._acc = ''
    self.add_import()
    self.add_spacer(2)
    self.add_pretests()
    for case in problem['testcases']:
      self.add_case(case)
      self.add_spacer()
    self.add_posttests()
    
  @glommer
  def add_spacer(self, width=1):
    """Add some vertical whitespace."""
    yield '\n' * (width-1)
    
  def add_line(self, line, indentation_level=0):
    self._acc += self.IND * indentation_level + line + '\n'
    
  def __iadd__(self, line):
    self.add_line(line)
    return self
    
  def get_formatstring(self, key):
    """Get a language-specific format string from the 'languageFormatters' section of
    the problem's json representation.
    """
    f = self.problem['languageFormatters']
    default = f['default']
    specific = f.get(self.LANG, {})
    if key in specific:
      return specific[key]
    return default[key]
    
  def add_case(self, case):
    raise NotImplementedError("child class must implement add_case")
    
  def input(self, case):
    """Return an array of the inputs for the given case, formatted according to our language."""
    if not isinstance(case['input'], list):
      ins = [case['input']]
    else:
      ins = case['input']
    return [self.repr(input) for input in ins]
    
  def actual(self, case):
    """Return a string representation of the 'actual' value for the given test case (as opposed to expected)."""
    actual = self.get_formatstring("actual")
    return actual.format(input=self.input(case), args=self.args(case), function=self.fun)
  
  def add_import(self):
    raise NotImplementedError("child class must implement add_import")
    
  def add_pretests(self):
    raise NotImplementedError("child class must implement add_pretests")
    
  def add_posttests(self):
    # This one is optional
    pass
        
  def module_string(self):
    """A big string representation of our whole unit test suite."""
    return self._acc
    
  def repr(self, obj):
    """Language-appropriate representation of the given Python object"""
    raise NotImplementedError("child class must implement repr")
    
  def args(self, case):
    """String representation of the argument list for the given case"""
    if not isinstance(case['input'], list):
      args = [case['input']]
    else:
      args = case['input']
    
    return ', '.join(self.repr(arg) for arg in args)
    
  def expected(self, case):
    return self.repr(case['expected'])
    
  def output_type(self, case):
    return self.typestring(case['expected'])
    
  def input_type(self, case):
    return self.typestring(case['input'])
    
  def typestring(self, obj):
    """Return the language-specific type corresponding to the type of the given Python object, as a string."""
    raise NotImplementedError("child class must implement typestring")
  
class PythonTestGen(TestGen):
  
  LANG = "python"
  
  @glommer
  def add_import(self):
    yield "import unittest"
    yield "from {} import {}".format(self.module, self.fun)

  @glommer
  def add_pretests(self):
    yield "class {}Tests(unittest.TestCase):".format(namify(self.name, self.CLASS_NAMING))
      
  @glommer
  def add_case(self, case):
    yield 'def test_{}(self):'.format(namify(case['description'], self.FUN_NAMING)), 1
    if isinstance(case['expected'], bool):
      self.add_boolean_assertion(case)
    else:
      self.add_equality_assertion(case)

  @glommer
  def add_equality_assertion(self, case):
    yield 'self.assertEqual(', 2
    yield self.expected(case) + ',', 3
    yield self.actual(case), 3
    yield ')', 2
    
  @glommer
  def add_boolean_assertion(self, case):    
    yield 'self.assert{truthiness}({actual})'.format(truthiness=str(case['expected']), actual=self.actual(case)), 2
    
  def repr(self, obj):
    return repr(obj)
    
    
class JavascriptTestGen(TestGen):
  
  LANG = "javascript"
  
  @glommer
  def add_import(self):
    yield "var {} = require('./{}');".format(self.fun, self.module)
    
  @glommer
  def add_pretests(self):
    yield 'describe("{}()", function() {{'.format(self.fun)
    
  @glommer
  def add_posttests(self):
    yield '});'
    
  @glommer(1)
  def add_case(self, case):
    yield 'it("{}", function() {{'.format(case['description'])
    
    yield 'var expected = {};'.format(self.expected(case)), 2
    yield 'expect({}({})).toEqual(expected);'.format(self.fun, self.args(case)), 2
    
    yield '});'
    
  def repr(self, obj):
    return json.dumps(obj)

class ObjCTestGen(TestGen):
  
  LANG = "objc"
  
  @glommer
  def add_import(self):
    yield "#import <XCTest/XCTest.h>"
    yield '#import "{}.h"'.format(self.module)
    
  @glommer
  def add_pretests(self):
    yield "@interface test_suite : XCTestCase"
    yield
    yield "@end"
    yield
    yield "@implementation test_suite"
      
  @glommer
  def add_posttests(self):
    yield "@end"
    
  @glommer
  def add_case(self, case):
    testName = 'test' + namify(case['description'], 'camel')
    yield "- (void){} {{".format(testName)
    
    if isinstance(case['expected'], bool):
      self.add_boolean_assertion(case)
    else:
      self.add_equality_assertion(case)
    
    yield '}'
    
  @glommer(1)
  def add_equality_assertion(self, case):
    yield "{} actual = {};".format(self.output_type(case), self.actual(case)), 1
    yield "{} expected = {};".format(self.output_type(case), self.repr(case['expected'])), 1
    if self.primitive_type(case['expected']):
      yield "XCTAssertEqual(actual, expected);", 1
    else:
      yield "XCTAssertEqualObjects(actual, expected);", 1
      
  def primitive_type(self, obj):
    return isinstance(obj, int) or isinstance(obj, bool)
    
  @glommer(1)
  def add_boolean_assertion(self, case):
    mod = '' if case['expected'] else '!'
    yield "XCTAssert({mod}{actual});".format(mod=mod, actual=self.actual(case))
    
  def typestring(self, obj):
    if isinstance(obj, basestring):
      return "NSString*"
    elif isinstance(obj, list):
      return "NSArray*"
    elif isinstance(obj, dict):
      return "NSDictionary*"
    elif isinstance(obj, int):
      return "NSUInteger"
    else:
      raise NotImplementedError(obj)
    
  def string_escape(self, s):
    # Why is this repr business necessary? Because we need to preserve literals like \n or \t
    rep = repr(s)
    if rep.startswith('u'):
      rep = rep[1:]
    assert rep[0] in "'\"" and rep[-1] in "'\""
    rep = rep[1:-1]
    return '@"{}"'.format(rep)
      
  def repr(self, obj):
    if isinstance(obj, basestring):
      return self.string_escape(obj)
    elif isinstance(obj, list):
      return '@[{}]'.format(', '.join(self.repr(ele) for ele in obj))
    elif isinstance(obj, dict):
      return '@{ ' +\
        ', '.join('{k} : {v}'.format(k=self.repr(key), v=self.repr(value)) for (key, value) in obj.iteritems()) +\
        '}'
    elif isinstance(obj, int):
      return '@' + str(obj)
    else:
      raise NotImplementedError()
      

if __name__ == '__main__':
  # Usage: e.g. unittests.py wordcount.json js
  fname = sys.argv[1]
  lang = sys.argv[2]
  f = open(fname)
  problem = json.loads(f.read())
  lang_to_gen = {'py': PythonTestGen, 'js': JavascriptTestGen, 'objc': ObjCTestGen}
  generator = lang_to_gen[lang]
  print generator(problem).module_string()