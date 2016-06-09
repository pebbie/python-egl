from distutils.core import setup, Extension

module1 = Extension('egl',
            sources = ['eglmodule.c'],
            libraries = ['GLESv2', 'EGL','X11']
            )

setup (name = 'egl',
    version = '0.1',
    description = 'EGL module',
    ext_modules = [module1]
    )
