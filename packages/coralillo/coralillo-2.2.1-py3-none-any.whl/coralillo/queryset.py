import coralillo.fields
from coralillo.datamodel import debyte_string

# these return false if the value is null
NULL_AFFECTED_FILTERS = ['lt', 'lte', 'gt', 'gte', 'startswith', 'endswith', 'in']

# these ones don't give a shit about null values
FILTERS = ['eq', 'ne'] + NULL_AFFECTED_FILTERS

# these work with json fields
JSON_FILTERS = ['isnull'] + FILTERS


def deref_multi(data, keys):
    if not keys:
        return data

    k_0 = keys[0]
    if k_0.isdigit():
        k_0 = int(k_0)

    return deref_multi(data[k_0], keys[1:])


class QuerySet:

    def __init__(self, cls, iterator):
        self.iterator = iterator
        self.filters = []
        self.cls = cls

    def __iter__(self):
        return self

    def __next__(self):
        for item in self.iterator:
            obj = self.cls.get(debyte_string(item))

            if self.matches_filters(obj):
                return obj

        raise StopIteration

    def matches_filters(self, item):
        for filt in self.filters:
            if not filt(item):
                return False

        return True

    def make_filter(self, fieldname, query_func, expct_value):
        ''' makes a filter that will be appliead to an object's property based
        on query_func '''

        def actual_filter(item):
            value = getattr(item, fieldname)

            if query_func in NULL_AFFECTED_FILTERS and value is None:
                return False

            if query_func == 'eq':
                return value == expct_value
            elif query_func == 'ne':
                return value != expct_value
            elif query_func == 'lt':
                return value < expct_value
            elif query_func == 'lte':
                return value <= expct_value
            elif query_func == 'gt':
                return value > expct_value
            elif query_func == 'gte':
                return value >= expct_value
            elif query_func == 'startswith':
                return value.startswith(expct_value)
            elif query_func == 'endswith':
                return value.endswith(expct_value)
            elif query_func == 'in':
                return value in expct_value

        actual_filter.__doc__ = '{} {} {}'.format('val', query_func, expct_value)

        return actual_filter

    def make_json_filter(self, fieldname, queries, expct_value):
        ''' makes a filter that will be appliead to an object's property based
        on queries '''

        def actual_filter(item):
            obj = getattr(item, fieldname)

            query_func = queries[-1]

            try:
                value = deref_multi(obj, queries[:-1])
            except (KeyError, TypeError):
                return query_func == 'isnull' and expct_value

            if query_func in NULL_AFFECTED_FILTERS and value is None:
                return False

            if query_func == 'eq':
                return value == expct_value
            elif query_func == 'ne':
                return value != expct_value
            elif query_func == 'lt':
                return value < expct_value
            elif query_func == 'lte':
                return value <= expct_value
            elif query_func == 'gt':
                return value > expct_value
            elif query_func == 'gte':
                return value >= expct_value
            elif query_func == 'startswith':
                return value.startswith(expct_value)
            elif query_func == 'endswith':
                return value.endswith(expct_value)
            elif query_func == 'isnull':
                return not expct_value

        actual_filter.__doc__ = '{} {} {}'.format(
            '.'.join(['val'] + queries[:-1]),
            queries[-1],
            expct_value,
        )

        return actual_filter

    def filter(self, **kwargs):
        for key, value in kwargs.items():
            try:
                fieldname, query_func = key.split('__', 1)
            except ValueError:
                fieldname, query_func = key, 'eq'

            if not hasattr(self.cls, fieldname):
                raise AttributeError('Model {} does not have field {}'.format(
                    self.cls.__name__,
                    fieldname,
                ))

            is_json_field = isinstance(getattr(
                self.cls,
                fieldname,
            ), coralillo.fields.Json)

            if is_json_field:
                queries = query_func.split('__')
                if queries[-1] not in JSON_FILTERS:
                    queries.append('eq')

                intersection = set(queries[:-1]).intersection(set(JSON_FILTERS))
                if len(intersection):
                    raise AttributeError('Filter {} is reserved'.format(list(intersection)[0]))

                self.filters.append(self.make_json_filter(fieldname, queries, value))

            else:
                if not is_json_field and query_func not in FILTERS:
                    raise AttributeError('Filter {} does not exist'.format(query_func))

                self.filters.append(self.make_filter(fieldname, query_func, value))

        return self

    def one(self):
        return next(self)

    def all(self):
        return list(self)
