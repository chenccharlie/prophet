class Function:
  def get_name():
    """
    Return function name used to pass in the query url
    """
    raise NotImplementedError

  def get_configs():
    """
    Return a dict with additional function specific param names and values
    """
    raise NotImplementedError

  def parse_data(json_data):
    """
    Return a dict with following format:
    {
      "last_refresh": "2019-09-05",
      "data": {
        "title1": {
          "2019-09-05": "value",
          "2019-09-04": "value",
          ...
        },
        "title2": {
          "2019-09-05": "value",
          "2019-09-04": "value",
          ...
        },
        ...
      }
    }
    """
    raise NotImplementedError
