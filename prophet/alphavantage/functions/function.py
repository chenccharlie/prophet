class Function:
  def get_name(self):
    """
    Return function name used to pass in the query url
    """
    raise NotImplementedError

  def get_configs(self):
    """
    Return a dict with additional function specific param names and values
    """
    raise NotImplementedError

  def parse_data(self, json_data):
    """
    Return a dict with following format:
    {
      "dates": [
        "2019-09-05",
        "2019-09-04",
        "2019-09-03",
        ...
      ],
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
