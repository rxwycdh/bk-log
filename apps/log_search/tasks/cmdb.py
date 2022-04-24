# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
License for BK-LOG 蓝鲸日志平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from concurrent.futures import ThreadPoolExecutor

from celery.schedules import crontab  # noqa
from celery.task import periodic_task  # noqa

from apps.log_search.handlers.biz import BizHandler
from apps.utils.log import logger


@periodic_task(run_every=crontab(minute="*/15"))
def refresh_cmdb():
    businesses = BizHandler.list()
    if not businesses:
        logger.error("[log_search][tasks]get business error")
        return False
    with ThreadPoolExecutor(max_workers=10) as executor:
        for business in businesses:
            biz_handler = BizHandler(business["bk_biz_id"])
            executor.submit(biz_handler.get_cache_hosts, bk_biz_id=business["bk_biz_id"], refresh=True)
    logger.info("[log_search][tasks]get business success, count: %s" % len(businesses))