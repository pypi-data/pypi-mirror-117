import requests
import pandas as pd
from urllib.parse import urljoin
from . import settings

TOP_PACKAGE = settings.TOP_PACKAGE


def get_indicator_values(
    indicator_ids,
    host="",
    username="",
    password="",
    api_path="/api/v1/indicator_v2/export/dataframe_json",
):
    """

    Args:
        indicator_ids: ["indicator_id", ...]
        host: 例如 "localhost:8888"
        username:
        password:
        api_path:

    Returns:

    """
    host = host or settings.INDICATOR_SERVICE_HOST
    username = username or settings.INDICATOR_SERVICE_USERNAME
    password = password or settings.INDICATOR_SERVICE_PASSWORD

    if not host:
        raise TOP_PACKAGE.exceptions.NoConfigError

    if not host.startswith("http"):
        host = "http://{}".format(host)

    url = urljoin(host, api_path)

    deduplication_list = list(set(indicator_ids))
    #
    auth = ()
    if username and password:
        auth = (username, password)
    #
    response = requests.post(
        url, json=dict(indicator_ids=deduplication_list), auth=auth
    )
    response.raise_for_status()
    #
    res = []
    for indicator_id, indicator_data in response.json().items():
        df = pd.DataFrame.from_dict(indicator_data)
        df.name = indicator_id
        res.append(df)
    return res


if __name__ == "__main__":
    indicator_ids = ["all_indexpv_chain_rank_app_by_week_all"]
    result = get_indicator_values(indicator_ids)
    print(result)
