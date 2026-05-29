import os
import platform


if os.name == 'nt':
    _platform_arch = os.environ.get('PROCESSOR_ARCHITECTURE', 'AMD64')
    platform.machine = lambda: _platform_arch
    platform.processor = lambda: _platform_arch
    platform.system = lambda: 'Windows'
    platform.platform = lambda *args, **kwargs: f'Windows-{_platform_arch}'
    platform.win32_ver = lambda: ('10', '', '', '')
    platform.uname = lambda: platform.uname_result(
        'Windows',
        os.environ.get('COMPUTERNAME', 'localhost'),
        os.environ.get('OS', 'Windows_NT'),
        '',
        _platform_arch,
    )
