==========================
Integer Sequence Generator
==========================

This module provides integer sequences which are consistent over multiple
processes.

.. note::

    It is important to enable dynamic scripting in elasticsearch.
    Add this to your yaml configuration file:
    
        script.disable_dynamic: false

    For elasticsearch version > 1.6:

        script.engine.groovy.inline.update: on

The sequences must be assigned to an elasticsearch client instance::

    >>> from elasticsearch import Elasticsearch
    >>> es_client = Elasticsearch(['localhost:%s' % crate_port])

To globally assign the client to all sequences in the application the client
can be assigned to the class property `ES`::

    >>> from lovely.essequence import Sequence
    >>> Sequence.ES = es_client


Usage
=====

There is a `Sequence` class::

    >>> from lovely.essequence import Sequence

It must be instantiated with the name of a sequence::

    >>> s1 = Sequence('s1')

Now the iids can be requested::

    >>> s1.next()
    1
    >>> s1.next()
    2

Multiple sequence instances for the same sequence name use the same bulk::

    >>> s2 = Sequence('s1', bulk_size=100)
    >>> s2.next()
    3

After the bulk size has been consumed the request of the next bulk is
transparently handled inside the `next` method::
Consume all the cached ids from s1::

    >>> for i in range(10): s1.next()
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13

Multiple independed sequences can be used::

    >>> other = Sequence('other')
    >>> other.next()
    1


Transforming the provided iid
=============================

A transformation function can be provided to transform the provided integer
value into something else when calling next::

    >>> asstring = Sequence('other', transform=str)
    >>> isinstance(asstring.next(), str)
    True

    >>> def transformer(iid):
    ...     return {'iid': iid}
    >>> Sequence('other', transform=transformer).next()
    {'iid': 3}


Resetting a Sequence
====================

For testing purposes it is possible to reset a sequence.

.. note::

    Resetting a sequence will not work correct if multiple processes use the
    same sequence. This is for testing only.

    >>> s1 = Sequence('reset')
    >>> s2 = Sequence('reset')
    >>> s1.next()
    1
    >>> s2.next()
    2

    >>> from lovely.essequence.sequence import testing_reset_sequences
    >>> testing_reset_sequences()

    >>> s2.next()
    1
    >>> s1.next()
    2
