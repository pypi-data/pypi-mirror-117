[![codecov](https://codecov.io/gh/Amourspirit/python-kwargshelper/branch/master/graph/badge.svg?token=mJ2HdGwSGy)](https://codecov.io/gh/Amourspirit/python-kwargshelper) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/Amourspirit/python-kwargshelper/CodeCov) ![GitHub](https://img.shields.io/github/license/Amourspirit/python-kwargshelper) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kwargshelper) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/kwargshelper)

# kwargshelper

A python package for working with **kwargs**

## Installation

You can install the Version Class from [PyPI](https://pypi.org/project/kwargshelper/):

```python
pip install kwargshelper
```

## KwargsHelper Class

Helper class for working with python `**kwargs` in a class constructor

Assigns values of `**kwargs` to an exising class with type checking and rules

Parse kwargs with suport for rules that can be extended that validate any arg of kwargs.
Type checking of any type.

Callback function for before update that includes a Cancel Option.

Many other options avaliable for more complex usage.

## KwArg Class

Helper class for working with python `**kwargs` in a method/function
Wrapper for `KwargsHelper` Class.

Assigns values of `**kwargs` to itself with validation

Parse kwargs with suport for rules that can be extended that validate any arg of kwargs.
Type checking of any type.

Callback function for before update that includes a Cancel Option.

Many other options avaliable for more complex usage.

## Rules

New rules can be created by inheriting from `IRule` interface/class

**Example Rule:**

```python
from kwhelp.rules import IRule
class RuleIntRangeZeroNine(IRule):
    '''
    Rule to ensure a integer from 0 to 9.
    '''
    def validate(self) -> bool:
        if not isinstance(self.field_value, int):
            return False
        if self.field_value < 0 or self.field_value > 9:
            if self.raise_errors:
                raise ValueError(
                    f"Arg error: '{self.key}' must be a num from 0 to 9")
            return False
        return True
```

### Included Rules

* RuleAttrNotExist
* RuleAttrExist
* RuleBool
* RuleNotNone
* RuleNumber
* RuleInt
* RuleIntPositive
* RuleIntNegative
* RuleFloat
* RuleFloatPositive
* RuleFloatNegative
* RuleStr
* RuleStrNotNullOrEmpty

## Usage KwArg Class

```python
from kwhelp import KwArg
import kwhelp.rules as rules

def my_method(**kwargs) -> str:
    kw = KwArg(**kwargs)
    kw.assign(key='first', require=True, types=[int])
    kw.assign(key='second', require=True, types=[int])
    kw.assign(key='msg', types=[str], default='Result:',
        rules=[rules.RuleStrNotNullOrEmpty])
    kw.assign(key='end', types=[str])
    first:int = kw.first
    second:int = kw.second
    msg: str = kw.msg
    _result = first + second
    if kw.is_attribute_exist('end'):
        return_msg = f'{msg} {_result}{kw.end}'
    else:
        return_msg = f'{msg} {_result}'
    return return_msg
```

## Usage KwargsHelper Class

Simple usage

```python
from kwhelp import KwargsHelper
import kwhelp.rules as rules

class MyClass:
    def __init__(self, **kwargs):
        self._loop_count = -1
        kw = KwargsHelper(self, {**kwargs}, field_prefix='')
        kw.assign(key='exporter', types=[str], default='None')
        kw.assign(key='name', types=[str], default='unknown')
        kw.assign(key='file_name', rules=[
                  rules.RuleStr, rules.RuleStrNotNullOrEmpty])
        kw.assign(key='loop_count', rules=[
                  rules.RuleInt, rules.RuleIntPositive],
                  default=self._loop_count)


my_class = MyClass(exporter='json', file_name='data.json', loop_count=3)
print(my_class.exporter)  # json
print(my_class.file_name)  # data.json
print(my_class.name)  # None
print(my_class.loop_count)  # 3
try:
    # will raise an error because loop_count is default  is -1 and
    # RuleIntPositive is added to rules
    my_class = MyClass(exporter='html', file_name='data.html',
                       name='Best Doc')
except Exception as e:
    print(e)  # Arg error: 'loop_count' must be a positive int value

my_class = MyClass(file_name='data.html', name='Best Doc', loop_count=1)
print(my_class.exporter)  # None
print(my_class.file_name)  # data.html
print(my_class.name)  # Best Doc
print(my_class.loop_count)  # 1
```

Using rules with Callback:

```python
from kwhelp import KwargsHelper, AfterAssignEventArgs, BeforeAssignEventArgs, AssignBuilder
import kwhelp.rules as rules

class MyClass:
    def __init__(self, **kwargs):
        self._loop_count = -1
        kw = KwargsHelper(self, {**kwargs})
        ab = AssignBuilder()
        kw.add_handler_before_assign(self._arg_before_cb)
        kw.add_handler_after_assign(self._arg_after_cb)
        ab.append(key='exporter', rules=[rules.RuleStr])
        ab.append(key='name', require=True, rules=[rules.RuleStr],
                  default='unknown')
        ab.append(key='file_name', require=True, rules=[
            rules.RuleStr, rules.RuleStrNotNullOrEmpty])
        ab.append(key='loop_count', require=True, rules=[
                  rules.RuleInt, rules.RuleIntPositive],
                  default=self._loop_count)
        result = True
        # by default assign will raise errors if conditions are not met.
        for arg in ab:
            result = kw.assign_helper(arg)
            if result == False:
                break
        if result == False:
            raise ValueError("Error parsing kwargs")

    def _arg_before_cb(self, helper: KwargsHelper,
                       args: BeforeAssignEventArgs) -> None:
        if args.key == 'name' and args.field_value == 'unknown':
            args.field_value = 'None'

    def _arg_after_cb(self, helper: KwargsHelper,
                      args: AfterAssignEventArgs) -> None:
        # callback function after value assigned to attribute
        if args.key == 'name' and args.field_value == 'unknown':
            raise ValueError(
                f"{args.key} This should never happen. value was suppose to be reassigned")

    @property
    def exporter(self) -> str:
        return self._exporter

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def loop_count(self) -> int:
        return self._loop_count

my_class = MyClass(exporter='json', file_name='data.json', loop_count=3)
print(my_class.exporter)  # json
print(my_class.file_name)  # data.json
print(my_class.name)  # None
print(my_class.loop_count)  # 3
```

Using callback example:

```python
from kwhelp import KwargsHelper, AfterAssignEventArgs, BeforeAssignEventArgs, AssignBuilder

class MyClass:
    def __init__(self, **kwargs):
        self._loop_count = -1
        kw = KwargsHelper(originator=self, obj_kwargs={**kwargs})
        ab = AssignBuilder()
        kw.add_handler_before_assign(self._arg_before_cb)
        kw.add_handler_after_assign(self._arg_after_cb)
        ab.append(key='exporter', require=True, types=[str])
        ab.append(key='name', require=True, types=[str],
                  default='unknown')
        ab.append(key='file_name', require=True, types=[str])
        ab.append(key='loop_count', types=[int],
                  default=self._loop_count)
        result = True
        # by default assign will raise errors if conditions are not met.
        for arg in ab:
            result = kw.assign_helper(arg)
            if result == False:
                break
        if result == False:
            raise ValueError("Error parsing kwargs")

    def _arg_before_cb(self, helper: KwargsHelper,
                       args: BeforeAssignEventArgs) -> None:
        # callback function before value assigned to attribute
        if args.key == 'loop_count' and args.field_value < 0:
            # cancel will raise CancelEventError unless KwargsHelper constructor has cancel_error=False
            args.cancel = True
        if args.key == 'name' and args.field_value == 'unknown':
            args.field_value = 'None'

    def _arg_after_cb(self, helper: KwargsHelper,
                      args: AfterAssignEventArgs) -> None:
        # callback function after value assigned to attribute
        if args.key == 'name' and args.field_value == 'unknown':
            raise ValueError(
                f"{args.key} This should never happen. value was suppose to be reassigned")

    @property
    def exporter(self) -> str:
        return self._exporter

    @property
    def file_name(self) -> str:
        return self._file_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def loop_count(self) -> int:
        return self._loop_count


my_class = MyClass(exporter='json', file_name='data.json', loop_count=3)
print(my_class.exporter)  # json
print(my_class.file_name)  # data.json
print(my_class.name)  # None
print(my_class.loop_count)  # 3
```
