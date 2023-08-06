import logging
import requests
import tempfile
import shutil

def release_model(api_key, model_hub_url, model_name,
    training_frame_name, module_id, project_id, version=None, sc=None, pipeline_model=None, df=None):

  params = {"trainingFrameName": training_frame_name, "moduleId": module_id,
            "projectId": project_id, "version": version}
  files = None

  if pipeline_model is not None:
    with tempfile.NamedTemporaryFile() as tmp:
      pipeline_model.write().overwrite().save(tmp.name)
      sc.parallelize([df.schema.json()]).coalesce(1).saveAsTextFile(tmp.name + "/schema-before")
      sc.parallelize([pipeline_model.transform(df).schema.json()]).coalesce(1).saveAsTextFile(tmp.name + "/schema-after")
      shutil.make_archive(tmp.name, 'zip', tmp.name)
    files = {'pipeline': open(tmp.name + ".zip", 'rb')}

  is_successful = False

  try:
    r = requests.post(
        model_hub_url + "/machine-learning/v1/models/" +
        model_name + "/release",
        headers={'Authorization': 'ApiKey ' + api_key}, params=params, files=files)
    r.raise_for_status()
    if r.status_code == 200:
      is_successful = True
  except requests.exceptions.HTTPError as e:
    logging.warning(e.response.text)

  return is_successful