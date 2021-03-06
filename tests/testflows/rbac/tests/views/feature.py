from testflows.core import *

from rbac.helper.common import *

@TestFeature
@Name("views")
def feature(self):

    tasks = []
    pool = Pool(3)

    try:
        try:
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.views.view", "feature")), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.views.live_view", "feature")), {})
            run_scenario(pool, tasks, Feature(test=load("rbac.tests.views.materialized_view", "feature")), {})
        finally:
            join(tasks)
    finally:
        pool.close()