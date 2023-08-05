#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
import inspect
import sys

from .aggregator import H2OAggregatorEstimator
from .coxph import H2OCoxProportionalHazardsEstimator
from .deeplearning import H2OAutoEncoderEstimator
from .deeplearning import H2ODeepLearningEstimator
from .estimator_base import H2OEstimator
from .gam import H2OGeneralizedAdditiveEstimator
from .gbm import H2OGradientBoostingEstimator
from .generic import H2OGenericEstimator
from .glm import H2OGeneralizedLinearEstimator
from .glrm import H2OGeneralizedLowRankEstimator
from .isolation_forest import H2OIsolationForestEstimator
from .kmeans import H2OKMeansEstimator
from .naive_bayes import H2ONaiveBayesEstimator
from .pca import H2OPrincipalComponentAnalysisEstimator
from .psvm import H2OSupportVectorMachineEstimator
from .random_forest import H2ORandomForestEstimator
from .rulefit import H2ORuleFitEstimator
from .stackedensemble import H2OStackedEnsembleEstimator
from .svd import H2OSingularValueDecompositionEstimator
from .targetencoder import H2OTargetEncoderEstimator
from .word2vec import H2OWord2vecEstimator
from .xgboost import H2OXGBoostEstimator


module = sys.modules[__name__]

def _algo_for_estimator_(shortname, cls):
    if shortname == 'H2OAutoEncoderEstimator':
        return 'autoencoder'
    return cls.algo

_estimator_cls_by_algo_ = {_algo_for_estimator_(name, cls): cls
                           for name, cls in inspect.getmembers(module, inspect.isclass)
                           if hasattr(cls, 'algo')}

def create_estimator(algo, **params):
    if algo not in _estimator_cls_by_algo_:
        raise ValueError("Unknown algo type: " + algo)
    return _estimator_cls_by_algo_[algo](**params)


__all__ = (
    "create_estimator",
    "H2OAggregatorEstimator", "H2OCoxProportionalHazardsEstimator", "H2OAutoEncoderEstimator",
    "H2ODeepLearningEstimator", "H2OEstimator", "H2OGeneralizedAdditiveEstimator", "H2OGradientBoostingEstimator",
    "H2OGenericEstimator", "H2OGeneralizedLinearEstimator", "H2OGeneralizedLowRankEstimator",
    "H2OIsolationForestEstimator", "H2OKMeansEstimator", "H2ONaiveBayesEstimator",
    "H2OPrincipalComponentAnalysisEstimator", "H2OSupportVectorMachineEstimator", "H2ORandomForestEstimator",
    "H2ORuleFitEstimator", "H2OStackedEnsembleEstimator", "H2OSingularValueDecompositionEstimator",
    "H2OTargetEncoderEstimator", "H2OWord2vecEstimator", "H2OXGBoostEstimator"
)
