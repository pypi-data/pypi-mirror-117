import collections
import urllib
import pandas as pd
import requests
from io import StringIO
import functools

cache_size = 5


def sort(df, sort_primary=None, sort_secondary=None):
    if sort_primary is not None:
        val, asc = sort_primary if isinstance(sort_primary, tuple) else (sort_primary, True)
        ascending = [asc]
        sort_by = [val.replace("_", " ").title().strip()]
        if sort_secondary is not None:
            val, asc = sort_secondary if isinstance(sort_secondary, tuple) else (sort_secondary, True)
            ascending.append(asc)
            sort_by.append(val.replace("_", " ").title().strip())

        return df.sort_values(sort_by, ascending=ascending)
    return df


class RfqViewer:

    def __init__(self, host_url, cache_last_x_calls=5):
        if '/api' not in host_url:
            self.root_url = host_url + "api" if host_url[-1] == '/' else host_url + "/api"
        else:
            self.root_url = host_url[:-1] if host_url[-1] == '/' else host_url

        global cache_size
        cache_size = cache_last_x_calls

    @functools.lru_cache(cache_size)
    def __query_csv(self, url, timestamp_index=False):
        request = requests.get(url)
        csv = request.content.decode("utf-8")
        index_col = "Timestamp" if timestamp_index else False
        return pd.read_csv(StringIO(csv), index_col=index_col)

    def query_rfq(self, timestamp_index=False, sort_primary=None, sort_secondary=None, **kwargs):
        params = collections.OrderedDict()
        for key in sorted(kwargs.keys()):
            params[key[1:] if key[0] == "_" else key] = ','.join(sorted(kwargs[key].split(",")))

        params["select"] = "id,timestamp,source,response_code,symbol,side,price_type,reference_price," \
                           "quantity,tick_size,instrument_id,requester,final_state"

        encoded = urllib.parse.urlencode(params)
        df = self.__query_csv(self.root_url + "/rfqs?" + encoded, timestamp_index=timestamp_index)
        headers = kwargs['select'] if 'select' in kwargs else params['select']
        headers = [header.strip() for header in headers.replace("_", " ").title().split(",")]

        return sort(df, sort_primary=sort_primary, sort_secondary=sort_secondary)[headers]

    @functools.lru_cache(cache_size)
    def __query_by_ids(self, encoded_ids, api_type, timestamp_index=False, select=None):
        df = self.__query_csv(self.root_url + "/" + api_type + "?" + encoded_ids, timestamp_index=timestamp_index)
        headers = df.columns
        if select is not None:
            headers = [header.strip() for header in select.replace("_", " ").title().split(",")]
        return df[headers]

    def query_quotes(self, rfqs_dataframe, timestamp_index=False, select=None, sort_primary=None, sort_secondary=None):
        assert "Id" in rfqs_dataframe, "The RFQs dataframe must have an ID column to identify RFQs."

        ids = sorted(rfqs_dataframe["Id"].tolist())
        params = collections.OrderedDict({"id": ','.join([str(_id) for _id in ids])})
        encoded = urllib.parse.urlencode(params)

        df = self.__query_by_ids(encoded, "quotes", timestamp_index=timestamp_index, select=select)
        return sort(df, sort_primary=sort_primary, sort_secondary=sort_secondary)

    def query_fills(self, rfqs_dataframe, timestamp_index=False, select=None, sort_primary=None, sort_secondary=None):
        assert "Id" in rfqs_dataframe, "The RFQs dataframe must have an ID column to identify RFQs."

        ids = sorted(rfqs_dataframe["Id"].tolist())
        params = collections.OrderedDict({"id": ','.join([str(_id) for _id in ids])})
        encoded = urllib.parse.urlencode(params)

        df = self.__query_by_ids(encoded, "fills", timestamp_index=timestamp_index, select=select)
        return sort(df, sort_primary=sort_primary, sort_secondary=sort_secondary)

    def query_state_updates(self, rfqs_dataframe, timestamp_index=False, select=None, sort_primary=None, sort_secondary=None):
        assert "Id" in rfqs_dataframe, "The RFQs dataframe must have an ID column to identify RFQs."

        ids = sorted(rfqs_dataframe["Id"].tolist())
        params = collections.OrderedDict({"id": ','.join([str(_id) for _id in ids])})
        encoded = urllib.parse.urlencode(params)

        df = self.__query_by_ids(encoded, "state_updates", timestamp_index=timestamp_index, select=select)
        return sort(df, sort_primary=sort_primary, sort_secondary=sort_secondary)


if __name__ == "__main__":
    rfqViewer = RfqViewer("http://lnvlp-intern3:8000/")

    rfqs = rfqViewer.query_rfq(_from="2021-08-02", source="BBG", to="2021-08-18", side="BID,ASK",
                               sort_primary=("final_state", False), sort_secondary="Requester")
    print(rfqs)
    quotes = rfqViewer.query_quotes(rfqs, select="id, bid price", sort_primary="Id", sort_secondary="Bid PRice")
    print(quotes)
    fills = rfqViewer.query_fills(rfqs, sort_primary=("Side", False))
    print(fills)
    state_updates = rfqViewer.query_state_updates(rfqs)
    print(state_updates)