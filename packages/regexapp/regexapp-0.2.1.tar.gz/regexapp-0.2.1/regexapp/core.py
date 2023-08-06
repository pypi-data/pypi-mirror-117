import re
import yaml
from pathlib import Path, PurePath
from datetime import datetime
from regexapp import LinePattern
from regexapp import MultilinePattern
from regexapp.exceptions import RegexBuilderError
from regexapp.exceptions import PatternReferenceError
from regexapp.collection import REF
import regexapp
from copy import deepcopy
from collections import OrderedDict
from textwrap import indent

BASELINE_REF = deepcopy(REF)


def get_template():
    """return yaml instance for template.yaml"""
    filename = str(PurePath(Path(__file__).parent, 'template.yaml'))
    with open(filename) as stream:
        obj = yaml.load(stream, Loader=yaml.SafeLoader)
        return obj


template = get_template()


def is_pro_edition():
    """return True if regexapp is Pro or Enterprise edition"""
    chk = regexapp.edition == 'Pro' or regexapp.edition == 'Enterprise'
    return chk


def enclose_string(text):
    """enclose text with either double-quote or triple double-quote

    Parameters
    ----------
    text (str): a text

    Returns
    -------
    str: a new string with enclosed double-quote or triple double-quote
    """
    text = str(text)
    fmt = '"""{}"""' if len(text.splitlines()) > 1 else '"{}"'
    enclosed_txt = fmt.format(text.replace('"', r'\"'))
    return enclosed_txt


class RegexBuilder:
    """Use for building regex pattern

    Attributes
    ----------
    user_data (str, list): a user data can be either string or list of string.
    test_data (str, list): a test data can be either string or list of string.
    is_line (bool): a flag to use LinePattern.  Default is False.
    prepended_ws (bool): prepend a whitespace at the beginning of a pattern.
            Default is False.
    appended_ws (bool): append a whitespace at the end of a pattern.
            Default is False.
    ignore_case (bool): prepend (?i) at the beginning of a pattern.
            Default is False.
    patterns (list): a list of patterns.
    test_report (str): a test report.
    test_result (bool): a test result.
    user_data_pattern_table (OrderedDict): a variable holds (user_data, pattern) pair.
    pattern_user_data_table (OrderedDict): a variable holds (pattern, user_data) pair.
    test_data_pattern_table (OrderedDict): a variable holds (test_data, pattern) pair.
    pattern_test_data_table (OrderedDict): a variable holds (pattern, test_data) pair.

    Methods
    -------
    RegexBuilder.validate_data(data, name) -> bool
    build() -> None
    test(showed=True) -> bool
    generate_unittest(test_name='', max_words=6,
                      test_cls_name='TestDynamicGenTestScript',
                      author='', email='', company='',
                      is_minimal=True, filename='', **kwargs) -> str
    generate_pytest(test_name='', max_words=6,
                    test_cls_name='TestDynamicGenTestScript',
                    author='', email='', company='',
                    is_minimal=True, filename='', **kwargs) -> str
    generate_rf_test(test_name='', max_words=6,
                     test_cls_name='TestDynamicGenTestScript',
                     author='', email='', company='',
                     is_minimal=True, filename='', **kwargs) -> str
    generate_python_test(test_name='', max_words=6,
                         test_cls_name='TestDynamicGenTestScript',
                         author='', email='', company='',
                         is_minimal=True, filename='', **kwargs) -> str

    Raises
    ------
    RegexBuilderError: if user_data or test_data is invalid format.
    """
    def __init__(self, user_data='', test_data='', is_line=False,
                 prepended_ws=False, appended_ws=False, ignore_case=False):
        self.user_data = user_data
        self.test_data = test_data
        self.is_line = is_line
        self.prepended_ws = prepended_ws
        self.appended_ws = appended_ws
        self.ignore_case = ignore_case
        self.patterns = []
        self.test_report = ''
        self.test_result = False
        self.user_data_pattern_table = OrderedDict()    # user data via pattern
        self.pattern_user_data_table = OrderedDict()    # pattern via user data
        self.test_data_pattern_table = OrderedDict()    # test data via pattern
        self.pattern_test_data_table = OrderedDict()    # pattern via test data

    @classmethod
    def validate_data(cls, **kwargs):
        """validate data

        Parameters
        ----------
        kwargs (dict): keyword argument

        Returns
        -------
        bool: True or False

        Raises
        ------
        RegexBuilderError: if failed to validate data.
        """
        if not kwargs:
            msg = 'CANT validate data without providing data.'
            raise RegexBuilderError(msg)

        is_validated = True
        for name, data in kwargs.items():
            fmt = '{} MUST be string or list of string.'
            if not isinstance(data, (list, str)):
                msg = fmt.format(name)
                raise RegexBuilderError(msg)

            if isinstance(data, list):
                for line in data:
                    if not isinstance(line, str):
                        msg = fmt.format(name)
                        raise RegexBuilderError(msg)
            is_validated &= True if data else False
        return is_validated

    def build(self):
        """Build regex pattern"""
        data = self.user_data
        self.__class__.validate_data(user_data=data)

        if not data:
            self.test_report = 'CANT build regex pattern with an empty data.'
            print(self.test_report)
            return

        if self.is_line:
            lst_of_user_data = data[:] if isinstance(data, (list, tuple)) else data.splitlines()
        else:
            if isinstance(data, str):
                lst_of_user_data = [data]
            else:
                lst_of_user_data = []
                for item in data:
                    if isinstance(item, (list, tuple)):
                        lst_of_user_data.append('\n'.join(map(str, item)))
                    else:
                        lst_of_user_data.append(str(item))

        for user_data in lst_of_user_data:
            if self.is_line:
                pattern = LinePattern(
                    user_data,
                    prepended_ws=self.prepended_ws,
                    appended_ws=self.appended_ws,
                    ignore_case=self.ignore_case
                )
            else:
                pattern = MultilinePattern(user_data, ignore_case=self.ignore_case)

            pattern not in self.patterns and self.patterns.append(pattern)
            self.user_data_pattern_table[user_data] = pattern
            self.pattern_user_data_table[pattern] = user_data

    def test(self, showed=False):
        """test regex pattern via test data.

        Parameters
        ----------
        showed (bool): show test report if set to True.  Default is False.

        Returns
        -------
        bool: True if passed a test, otherwise, False.
        """
        data = self.test_data
        self.__class__.validate_data(test_data=data)

        if not data:
            self.test_report = 'CANT run test with an empty data.'
            showed and print(self.test_report)
            return False

        if self.is_line:
            lst_of_test_data = data[:] if isinstance(data, (list, tuple)) else data.splitlines()
        else:
            if isinstance(data, str):
                lst_of_test_data = [data]
            else:
                lst_of_test_data = []
                for item in data:
                    if isinstance(item, (list, tuple)):
                        lst_of_test_data.append('\n'.join(map(str, item)))
                    else:
                        lst_of_test_data.append(str(item))

        result = ['Test Data:', '-' * 9, '\n'.join(lst_of_test_data), '']
        result += ['Matched Result:', '-' * 14]

        test_result = True
        for pat in self.patterns:
            is_matched = False
            lst = []
            for test_data in lst_of_test_data:
                match = re.search(pat, test_data)
                if match:
                    is_matched = True
                    match.groupdict() and lst.append(match.groupdict())
                    self.test_data_pattern_table[test_data] = pat
                    self.pattern_test_data_table[pat] = test_data

            test_result &= is_matched
            tr = 'NO' if not is_matched else lst if lst else 'YES'
            result.append('pattern: {}'.format(pat))
            result.append('matched: {}'.format(tr))
            result.append('-' * 10)

        self.test_result = test_result
        self.test_report = '\n'.join(result)
        showed and print(self.test_report)

        return test_result

    def generate_unittest(self, test_name='', max_words=6,
                          test_cls_name='TestDynamicGenTestScript',
                          author='', email='', company='',
                          is_minimal=True, filename='', **kwargs):
        """dynamically generate Python unittest script
        Parameters
        ----------
        test_name (str): a predefined test name.  Default is empty.
                + unittest will use either predefined test name or
                    generated test name from test data
                + pytest will use predefined test name.
                + robotframework test will depend on test workflow.  It might be
                    either used predefined test name or generated test name.
        max_words (int): total number of words for generating test name.
                Default is 6 words.
        test_cls_name (str): a test class name for test script.  This test class
                name only be applicable for unittest or pytest.
                Default is TestDynamicGenTestScript.
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: python unittest script
        """
        obj = DynamicGenTestScript(
            self, test_name=test_name, max_words=max_words,
            test_cls_name=test_cls_name, **kwargs
        )
        script = obj.generate_unittest(
            author=author, email=email, company=company,
            is_minimal=is_minimal, filename=filename, **kwargs
        )
        return script

    def generate_pytest(self, test_name='', max_words=6,
                        test_cls_name='TestDynamicGenTestScript',
                        author='', email='', company='',
                        is_minimal=True, filename='', **kwargs):
        """dynamically generate Python pytest script
        Parameters
        ----------
        test_name (str): a predefined test name.  Default is empty.
                + unittest will use either predefined test name or
                    generated test name from test data
                + pytest will use predefined test name.
                + robotframework test will depend on test workflow.  It might be
                    either used predefined test name or generated test name.
        max_words (int): total number of words for generating test name.
                Default is 6 words.
        test_cls_name (str): a test class name for test script.  This test class
                name only be applicable for unittest or pytest.
                Default is TestDynamicGenTestScript.
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: python pytest script
        """
        obj = DynamicGenTestScript(
            self, test_name=test_name, max_words=max_words,
            test_cls_name=test_cls_name, **kwargs
        )
        script = obj.generate_pytest(
            author=author, email=email, company=company,
            is_minimal=is_minimal, filename=filename, **kwargs
        )
        return script

    def generate_rf_test(self, test_name='', max_words=6,
                         test_cls_name='TestDynamicGenTestScript',
                         author='', email='', company='',
                         is_minimal=True, filename='', **kwargs):
        """dynamically generate Robotframework script
        Parameters
        ----------
        test_name (str): a predefined test name.  Default is empty.
                + unittest will use either predefined test name or
                    generated test name from test data
                + pytest will use predefined test name.
                + robotframework test will depend on test workflow.  It might be
                    either used predefined test name or generated test name.
        max_words (int): total number of words for generating test name.
                Default is 6 words.
        test_cls_name (str): a test class name for test script.  This test class
                name only be applicable for unittest or pytest.
                Default is TestDynamicGenTestScript.
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: Robotframework test script
        """
        obj = DynamicGenTestScript(
            self, test_name=test_name, max_words=max_words,
            test_cls_name=test_cls_name, **kwargs
        )
        script = obj.generate_rf_test(
            author=author, email=email, company=company,
            is_minimal=is_minimal, filename=filename, **kwargs
        )
        return script

    def generate_python_test(self, test_name='', max_words=6,
                             test_cls_name='TestDynamicGenTestScript',
                             author='', email='', company='',
                             is_minimal=True, filename='', **kwargs):
        """dynamically generate Python test script
        Parameters
        ----------
        test_name (str): a predefined test name.  Default is empty.
                + unittest will use either predefined test name or
                    generated test name from test data
                + pytest will use predefined test name.
                + robotframework test will depend on test workflow.  It might be
                    either used predefined test name or generated test name.
        max_words (int): total number of words for generating test name.
                Default is 6 words.
        test_cls_name (str): a test class name for test script.  This test class
                name only be applicable for unittest or pytest.
                Default is TestDynamicGenTestScript.
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: python pytest script
        """
        obj = DynamicGenTestScript(
            self, test_name=test_name, max_words=max_words,
            test_cls_name=test_cls_name, **kwargs
        )
        script = obj.generate_python_test(
            author=author, email=email, company=company,
            is_minimal=is_minimal, filename=filename, **kwargs
        )
        return script


def add_reference(name='', pattern='', **kwargs):
    """add keyword reference to PatternReference.  This is an inline adding
    PatternReference for quick test.

    Parameters
    ----------
    name (str): a keyword.
    pattern (str): a regex pattern.
    kwargs (dict): keyword argument which will use for special case such as datetime.

    Raises
    ------
    PatternReferenceError: if adding an existing keyword from
        system_references.yaml or user_references.yaml
    """
    if not name:
        fmt = '{} keyword can not be empty name.'
        PatternReferenceError(fmt.format(name))

    obj = dict(pattern=pattern,
               description='inline_{}_{}'.format(name, pattern))
    if name not in REF:
        REF[name] = obj
    else:
        if name == 'datetime':
            for key, value in kwargs.items():
                if re.match(r'format\d+$', key):
                    REF['datetime'][key] = value
        else:
            if name not in BASELINE_REF:
                REF[name] = obj
            else:
                fmt = ('{} already exists in system_references.yaml '
                       'or user_references.yaml')
                raise PatternReferenceError(fmt.format(name))


def remove_reference(name=''):
    """remove keyword reference from PatternReference.  This method only remove
    any inline adding keyword reference.

    Parameters
    ----------
    name (str): a keyword.

    Raises
    ------
    PatternReferenceError: if removing an existing keyword from
        system_references.yaml or user_references.yaml
    """
    if not name:
        fmt = '{} keyword can not be empty name.'
        PatternReferenceError(fmt.format(name))

    if name in REF:
        if name not in BASELINE_REF:
            REF.pop(name)
        else:
            if name == 'datetime':
                REF['datetime'] = deepcopy(BASELINE_REF['datetime'])
            else:
                fmt = ('CANT remove {!r} from system_references.yaml '
                       'or user_references.yaml')
                raise PatternReferenceError(fmt.format(name))
    else:
        fmt = 'CANT remove {!r} keyword because it does not exist.'
        raise PatternReferenceError(fmt.format(name))


class DynamicGenTestScript:
    """Dynamically generate test script

    Attributes
    ----------
    test_info (RegexBuilder, list): can be either RegexBuilder instance or
            a list of string.  If test_info is a list of string, it must follow
            this format that contain two items: user_data and test_data.
    test_name (str): a predefined test name.  Default is empty.
            + unittest will use either predefined test name or
                generated test name from test data
            + pytest will use predefined test name.
            + robotframework test will depend on test workflow.  It might be
                either used predefined test name or generated test name.
    is_line (bool): a flag to use LinePattern.  Default is False.
    max_words (int): total number of words for generating test name.
            Default is 6 words.
    kwargs (dict): an optional keyword arguments.
            Community edition will use the following keywords:
                prepended_ws, appended_ws, ignore_case
            Pro or Enterprise edition will use
                prepended_ws, appended_ws, ignore_case, other keywords
    test_cls_name (str): a test class name for test script.  This test class
            name only be applicable for unittest or pytest.
            Default is TestDynamicGenTestScript.
    template (dict): a holder for all templates or format to generate test script.
    lst_of_tests (list): a list of test.
    test_data (str): a test data
    patterns (list): a list of patterns.

    Methods
    -------
    compile_test_info() -> None
    save_file(filename, content) -> None
    generate_test_name(test_data='') -> str
    generate_custom_docstring(**kwargs) -> str
    generate_docstring(test_framework='unittest', author='', email='', company='', **kwargs) -> str
    generate_data_insertion() -> str
    generate_unittest(author='', email='', company='', is_minimal=True, filename='', **kwargs) -> str
    generate_pytest(author='', email='', company='', is_minimal=True, filename='', **kwargs) -> str
    generate_rf_test(author='', email='', company='', is_minimal=True, filename='', **kwargs) -> str
    generate_python_test(author='', email='', company='', is_minimal=True, filename='', **kwargs) -> str
    """
    def __init__(self, test_info=None, test_name='', is_line=False,
                 max_words=6, test_cls_name='TestDynamicGenTestScript',
                 **kwargs):
        self.test_info = test_info
        self.test_name = test_name
        if isinstance(test_info, RegexBuilder):
            self.is_line = test_info.is_line
        else:
            self.is_line = is_line
        self.max_words = max_words
        self.test_cls_name = str(test_cls_name)
        self.kwargs = kwargs
        self.template = template
        self.lst_of_tests = []
        self.test_data = None
        self.patterns = None
        self.compile_test_info()

    def compile_test_info(self):
        """prepare a list of test cases from test info"""

        self.lst_of_tests = []
        test_info = self.test_info
        if isinstance(test_info, RegexBuilder):
            testable = deepcopy(test_info)
            self.test_data = testable.test_data
        else:
            chk = isinstance(test_info, list) and len(test_info) == 2
            if not chk:
                raise RegexBuilderError('Invalid test_info format')

            user_data, test_data = self.test_info
            self.test_data = test_data
            prepended_ws = self.kwargs.get('prepended_ws', False)
            appended_ws = self.kwargs.get('appended_ws', False)
            ignore_case = self.kwargs.get('ignore_case', False)

            testable = RegexBuilder(
                user_data=user_data, test_data=test_data,
                is_line=self.is_line,
                prepended_ws=prepended_ws,
                appended_ws=appended_ws, ignore_case=ignore_case
            )
        testable.build()
        testable.test()

        self.patterns = testable.patterns

        user_data_pattern_table = testable.user_data_pattern_table
        pattern_user_data_table = testable.pattern_user_data_table
        test_data_pattern_table = testable.test_data_pattern_table

        if not test_data_pattern_table and not user_data_pattern_table:
            raise RegexBuilderError('No prepared_data to build test script')

        for test_data, pattern in test_data_pattern_table.items():
            test_name = self.generate_test_name(test_data=test_data)
            prepared_data = pattern_user_data_table.get(pattern)
            self.lst_of_tests.append([test_name, test_data, prepared_data, pattern])

    def save_file(self, filename, content):
        """Save data to file

        Parameters
        ----------
        filename (str): a file name
        content (str): a file content
        """
        filename = str(filename).strip()
        if filename:
            with open(filename, 'w') as stream:
                stream.write(content)

    def generate_test_name(self, test_data=''):
        """generate test name from test_data

        Parameters
        ----------
        test_data (str): a test data.  Default is empty.

        Returns
        -------
        str: a test name
        """
        pat = r'[^0-9a-zA-Z]*\s+[^0-9a-zA-Z]*'
        test_data = str(test_data).lower().strip()
        test_data = ' '.join(re.split(pat, test_data)[:self.max_words])
        test_name = self.test_name or test_data
        test_name = re.sub(r'[^0-9a-z]+', '_', test_name)
        test_name = test_name.strip('_')
        if not test_name.startswith('test_'):
            test_name = 'test_{}'.format(test_name)
        return test_name

    def generate_custom_docstring(self, **kwargs):
        """Generate custom docstring for Pro Edition or Enterprise Edition

        Parameters
        ----------
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: a custom docstring or empty string.
        """
        if kwargs:
            if is_pro_edition():
                fmt = ('Contact tuyen@geekstrident.com to use {!r} flags on '
                       'Regexapp Pro or Enterprise Edition.')
                print(fmt.format(kwargs))
            else:
                fmt = 'CANT use {!r} flags with Regexapp Community Edition.'
                print(fmt.format(kwargs))
                return ''
        else:
            return ''

    def generate_docstring(self, test_framework='unittest',
                           author='', email='', company='', **kwargs):
        """Generate module docstring for test script

        Parameters
        ----------
        test_framework (str): a test framework.  Default is unittest.
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: a module docstring
        """
        lang = '' if test_framework == 'robotframework' else 'Python '
        fmt = '{}{} script is generated by Regexapp {} Edition'
        fmt1 = 'Created by  : {}'
        fmt2 = 'Email       : {}'
        fmt3 = 'Company     : {}'
        fmt4 = 'Created date: {:%Y-%m-%d}'

        lst = list()
        author = author or company
        lst.append(fmt.format(lang, test_framework, regexapp.edition))
        lst.append('')
        author and lst.append(fmt1.format(author))
        email and lst.append(fmt2.format(email))
        company and company != author and lst.append(fmt3.format(company))
        lst.append(fmt4.format(datetime.now()))
        custom_docstr = self.generate_custom_docstring(**kwargs)
        custom_docstr and lst.append(custom_docstr)

        if test_framework == 'robotframework':
            new_lst = [l.strip() for l in indent('\n'.join(lst), '# ').splitlines()]
            comment = '\n'.join(new_lst)
            return comment
        else:
            module_docstr = '"""{}\n"""'.format('\n'.join(lst))
            return module_docstr

    def generate_data_insertion(self, is_minimal=True):
        """generate list insertion for unittest script

        Parameters
        ----------
        is_minimal (bool): flag to generate a minimal script.  Default is True.

        Returns
        -------
        str: a format of list insertion.
        """
        lst = ['arguments = list()']

        basename = 'regexapp_data_insertion'
        postfix = 'minimal_fmt' if is_minimal else 'fmt'
        fmt = self.template.get('{}_{}'.format(basename, postfix))

        fmt1 = '    # test case #{:0{}} - {}'
        spacers = len(str(len(self.lst_of_tests)))
        for index, test in enumerate(self.lst_of_tests, 1):
            test_name, test_data, prepared_data, pattern = test
            test_data = enclose_string(test_data)
            prepared_data = enclose_string(prepared_data)
            data = fmt.format(test_name=enclose_string(test_name),
                              test_data='__test_data_placeholder__',
                              prepared_data='__prepared_data_placeholder__',
                              pattern=enclose_string(pattern))
            lst.append('')
            lst.append(fmt1.format(index, spacers, test_name))
            new_data = indent(data, ' ' * 4)
            new_data = new_data.replace('__test_data_placeholder__', test_data)
            new_data = new_data.replace('__prepared_data_placeholder__', prepared_data)
            lst.append(new_data)

        result = '\n'.join(lst)
        return result

    def generate_unittest(self, author='', email='', company='',
                          is_minimal=True, filename='', **kwargs):
        """dynamically generate Python unittest script
        Parameters
        ----------
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: python unittest script
        """
        lst = []
        # part 1
        module_docstring = self.generate_docstring(
            test_framework='unittest',
            author=author, email=email, company=company, **kwargs
        )

        basename = 'unittest_regexapp'
        postfix = 'minimal_template1' if is_minimal else 'template1'
        fmt1 = self.template.get('{}_{}'.format(basename, postfix))

        data = fmt1.format(module_docstring=module_docstring,
                           test_cls_name=self.test_cls_name)
        lst.append(data)
        lst.append('')

        # part 2
        postfix = 'minimal_template2' if is_minimal else 'template2'
        fmt2 = self.template.get('{}_{}'.format(basename, postfix))

        for test in self.lst_of_tests:
            test_name = test[0]
            method_def = fmt2.format(test_name=test_name)
            method_def = indent(method_def, ' ' * 4)
            if method_def not in lst:
                lst.append(method_def)
                lst.append('')

        # part 3
        postfix = 'minimal_template3' if is_minimal else 'template3'
        fmt3 = self.template.get('{}_{}'.format(basename, postfix))

        data_insertion = self.generate_data_insertion(is_minimal=is_minimal)
        data = fmt3.format(data_insertion=data_insertion,
                           test_cls_name=self.test_cls_name)
        lst.append('')
        lst.append(data)

        test_script = '\n'.join(lst)
        test_script = '\n'.join(l.rstrip() for l in test_script.splitlines())

        self.save_file(filename, test_script)

        return test_script

    def generate_pytest(self, author='', email='', company='',
                        is_minimal=True, filename='', **kwargs):
        """dynamically generate Python pytest script
        Parameters
        ----------
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: python pytest script
        """

        module_docstring = self.generate_docstring(
            test_framework='pytest',
            author=author, email=email, company=company, **kwargs
        )

        basename = 'regexapp_parametrize_item'
        postfix = 'minimal_fmt' if is_minimal else 'fmt'
        parametrize_item_fmt = self.template.get('{}_{}'.format(basename, postfix))

        lst = ['']
        placeholder_table = dict()
        for index, test in enumerate(self.lst_of_tests):
            _, test_data, prepared_data, pattern = test
            test_data = enclose_string(test_data)
            prepared_data = enclose_string(prepared_data)
            key1 = '__test_data_placeholder_{}__'.format(index)
            key2 = '__prepared_data_placeholder_{}__'.format(index)
            placeholder_table[key1] = test_data
            placeholder_table[key2] = prepared_data

            kw = dict(test_data=key1,
                      prepared_data=key2,
                      pattern=enclose_string(pattern))
            parametrize_item = parametrize_item_fmt.format(**kw)
            parametrize_item = indent(parametrize_item, ' ' * 8)
            lst.append(parametrize_item)

        parametrize_data = '\n'.join(lst)

        basename = 'pytest_parametrize_regexapp'
        postfix = 'minimal_template' if is_minimal else 'template'
        parametrize_template = self.template.get('{}_{}'.format(basename, postfix))

        ss = parametrize_template.format(parametrize_data=parametrize_data)
        parametrize_invocation = '\n'.join(['', indent(ss, ' ' * 4)])

        for key, value in placeholder_table.items():
            parametrize_invocation = parametrize_invocation.replace(key, value)

        test_name = self.test_name or 'test_generating_script'
        if not test_name.startswith('test_'):
            test_name = 'test_{}'.format(test_name)

        kw = dict(module_docstring=module_docstring,
                  test_cls_name=self.test_cls_name,
                  test_name=test_name,
                  parametrize_invocation=parametrize_invocation)

        basename = 'pytest_regexapp'
        postfix = 'minimal_template' if is_minimal else 'template'
        script_template = self.template.get('{}_{}'.format(basename, postfix))

        test_script = script_template.format(**kw)
        test_script = '\n'.join(l.rstrip() for l in test_script.splitlines())

        self.save_file(filename, test_script)

        return test_script

    def generate_rf_test(self, author='', email='', company='',
                         is_minimal=True, filename='', **kwargs):
        """dynamically generate Robotframework test script
        Parameters
        ----------
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: Robotframework test script
        """
        msg = 'TODO: need to implement generated_rf_test for robotframework'
        NotImplementedError(msg)

    def generate_python_test(self, author='', email='', company='',
                             is_minimal=True, filename='', **kwargs):
        """dynamically generate Python test script
        Parameters
        ----------
        author (str): author name.  Default is empty.
        email (str): author name.  Default is empty.
        company (str): company name.  Default is empty.
        is_minimal (bool): flag to generate a minimal script.  Default is True.
        filename (str): save a generated test script to file name.
        kwargs (str): custom keyword arguments for
                Pro Edition or Enterprise Edition.

        Returns
        -------
        str: a Python test script
        """
        module_docstring = self.generate_docstring(
            test_framework='test',
            author=author, email=email, company=company, **kwargs
        )
        if self.is_line:
            if isinstance(self.test_data, (list, tuple)):
                test_data = enclose_string('\n'.join(self.test_data))
            else:
                test_data = enclose_string(self.test_data)

            if len(self.patterns) == 1:
                template_ = self.template.get('snippet_template1')
                pattern = enclose_string(self.patterns[0])
                test_script = template_.format(
                    module_docstring=module_docstring,
                    test_data=test_data, pattern=pattern
                )
            else:
                template_ = self.template.get('snippet_template2')
                lst = []
                for pattern in self.patterns:
                    lst.append('r{}'.format(enclose_string(pattern)))
                patterns = indent(',\n'.join(lst), '    ').strip()
                test_script = template_.format(
                    module_docstring=module_docstring,
                    test_data=test_data, patterns=patterns
                )
        else:
            template_ = self.template.get('snippet_template3')
            if isinstance(self.test_data, (list, tuple)):
                test_data = enclose_string(self.test_data[0])
            else:
                test_data = enclose_string(self.test_data)

            pattern = enclose_string(self.patterns[0])
            test_script = template_.format(
                module_docstring=module_docstring,
                test_data=test_data, pattern=pattern
            )

        self.save_file(filename, test_script)
        return test_script
