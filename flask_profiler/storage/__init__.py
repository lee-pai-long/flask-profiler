# -*- coding: utf8 -*-

import os
import sys
import importlib
from contextlib import contextmanager

from .base import BaseStorage


@contextmanager
def cwd_in_path():

    cwd = os.getcwd()
    if cwd in sys.path:
        yield
    else:
        sys.path.insert(0, cwd)
        try:
            yield cwd
        finally:
            sys.path.remove(cwd)


def getCollection(conf):
    engine = conf.get("engine", "")
    # TODO: Remove useless nesting (when return no need to else)
    if engine.lower() == "mongodb":
        from .mongo import Mongo
        return Mongo(conf)
    elif engine.lower() == "sqlite":
        from .sqlite import Sqlite
        return Sqlite(conf)
    else:
        try:
            parts = engine.split('.')
            # NOTE: flake8 E261 (two space before inline comment)
            if len(parts) < 1: # engine must have at least module name and class
                raise ImportError

            module_name = '.'.join(parts[:-1])
            # NOTE: No need to use a k for class when appending the variable name
            klass_name = parts[-1]

            # we need to make sure that it will be able to find module in your
            # project directory
            with cwd_in_path():
                module = importlib.import_module(module_name)

            storage = getattr(module, klass_name)
            if not issubclass(storage, BaseStorage):
                raise ImportError

        except ImportError:
            raise ValueError(
                ("flask-profiler requires a valid storage engine but it is"
                    " missing or wrong. provided engine: {}".format(engine)))

        return storage(conf)
