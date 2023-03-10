% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/tracking-server.R
\name{mlflow_server}
\alias{mlflow_server}
\title{Run MLflow Tracking Server}
\usage{
mlflow_server(
  file_store = "mlruns",
  default_artifact_root = NULL,
  host = "127.0.0.1",
  port = 5000,
  workers = NULL,
  static_prefix = NULL
)
}
\arguments{
\item{file_store}{The root of the backing file store for experiment and run data.}

\item{default_artifact_root}{Local or S3 URI to store artifacts in, for newly created experiments.}

\item{host}{The network address to listen on (default: 127.0.0.1).}

\item{port}{The port to listen on (default: 5000).}

\item{workers}{Number of gunicorn worker processes to handle requests (default: 4).}

\item{static_prefix}{A prefix which will be prepended to the path of all static paths.}
}
\description{
Wrapper for `mlflow server`.
}
