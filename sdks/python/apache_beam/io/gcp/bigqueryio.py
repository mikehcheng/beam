"""TODO(mikehcheng): DO NOT SUBMIT without one-line documentation for bigqueryio.

TODO(mikehcheng): DO NOT SUBMIT without a detailed description of bigqueryio.
"""

import json
import uuid

from apache_beam.internal.gcp import auth
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.io.iobase import BoundedSource
from apache_beam.transforms import DoFn
from apache_beam.transforms import ParDo
from apache_beam.transforms import PTransform


class ReadFromBigQuery(PTransform):
  def __init__(self, **kwargs):
    super(ReadFromBigQuerySource, self).__init__(**kwargs)
    # TODO

  def expand(self, pcoll):
    pass # TODO


class BigQuerySourceBase(BoundedSource):
  def __init__(self, extract_uuid, client=None):
    self.extract_uuid = extract_uuid
    self.client = client or bigquery.BigqueryV2(
        credentials=auth.get_service_credentials())
    self.extracted_files = None
    # TODO determine options here or split? also size or nah

  def estimate_size(self):
    return None # TODO

  def split(self, desired_bundle_size, start_position=None, stop_position=None):
    if self.extracted_files is None:
      table_ref = self._get_table_to_extract()


  def _get_table_to_extract(self):
    raise NotImplementedError


