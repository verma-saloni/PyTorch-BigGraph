#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE.txt file in the root directory of this source tree.


def get_torchbiggraph_config():

    config = dict(  # noqa
        # I/O data
        entity_path="data/politifact",
        edge_paths=["data/train_partitioned", "data/test_partitioned"],
        checkpoint_path="model/politifact",
        # Graph structure
        entities={"user": {"num_partitions": 1}, "article": {"num_partitions": 1}},
        relations=[
            {"name": "twitted", "lhs": "user", "rhs": "article", "operator": "none"},
            {"name": "follows", "lhs": "user", "rhs": "user", "operator": "none"}
        ],
        # Scoring model
        dimension=128,
        global_emb=False,
        # Training
        num_epochs=30,
        lr=0.001,
        # Misc
        hogwild_delay=2,
    )

    return config
