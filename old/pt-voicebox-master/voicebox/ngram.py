from __future__ import absolute_import
import six
from six.moves import range
__author__ = 'jamiebrew'


class Ngram(object):
    """information about a unique string within a corpus"""

    def __init__(self, string, after_distance=0, before_distance=0):
        self.string = string
        self.count = 1
        self.after = [{} for _ in range(after_distance)]
        self.before = [{} for _ in range(before_distance)]
        self.frequency = 0              # normalized rate of occurrence
        self.sig_score = 0              # significance score
        self.rhymes = {}

    def __str__(self):
        return self.string+"\ncount: "+str(self.count)+"\nfreq: "+str(self.frequency)+"\nsig: "+str(self.sig_score)+'\n'

    def __repr__(self):
        return self.string

    def __len__(self):
        return len(self.string)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_after(self, distance=1, n=20, sort_attribute="count"):
        """returns top n words occuring distance after this ngram"""
        return self._get_ngram_and_attribute(distance, n, sort_attribute, True)

    def get_before(self, distance=1, n=20, sort_attribute="count"):
        """returns top n words occuring distance before this ngram"""
        return self._get_ngram_and_attribute(distance, n, sort_attribute, False)

    def _get_ngram_and_attribute(self, distance, n, sort_attribute, is_after):
        distance -= 1
        dictionary = self.after[distance] if is_after else self.before[distance]

        return list(
            reversed(
                sorted(
                    [(
                            string_ngram[0],
                            getattr(string_ngram[1], sort_attribute)
                        ) for string_ngram in six.iteritems(dictionary)],
                    key=lambda tuple: tuple[1]
                )
            )
        )[0:n]
