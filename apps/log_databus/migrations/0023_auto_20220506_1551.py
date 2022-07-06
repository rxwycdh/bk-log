# Generated by Django 3.2.5 on 2022-05-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("log_databus", "0022_alter_cleantemplate_visible_bk_biz_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="bkdataclean",
            name="etl_config",
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name="清洗配置"),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="bkbase_table_id",
            field=models.CharField(default=None, max_length=255, null=True, verbose_name="BKBASE结果表ID"),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="bkdata_biz_id",
            field=models.IntegerField(null=True, verbose_name="数据归属业务ID"),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="collector_plugin_id",
            field=models.BigIntegerField(db_index=True, null=True, verbose_name="采集插件ID"),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="etl_processor",
            field=models.CharField(
                choices=[("transfer", "Transfer"), ("bkbase", "数据平台")],
                default="transfer",
                max_length=32,
                verbose_name="数据处理引擎",
            ),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="is_display",
            field=models.BooleanField(default=True, verbose_name="采集项是否对用户可见"),
        ),
        migrations.AddField(
            model_name="collectorconfig",
            name="processing_id",
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="计算平台清洗id"),
        ),
        migrations.CreateModel(
            name="CollectorPlugin",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("is_deleted", models.BooleanField(default=False, verbose_name="是否删除")),
                ("deleted_at", models.DateTimeField(blank=True, null=True, verbose_name="删除时间")),
                ("deleted_by", models.CharField(blank=True, max_length=32, null=True, verbose_name="删除者")),
                ("bk_biz_id", models.BigIntegerField(verbose_name="业务ID")),
                ("bkdata_biz_id", models.BigIntegerField(blank=True, null=True, verbose_name="数据归属业务ID")),
                ("collector_plugin_id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="采集插件ID")),
                ("collector_plugin_name", models.CharField(max_length=64, verbose_name="采集插件名称")),
                ("collector_plugin_name_en", models.CharField(max_length=64, verbose_name="英文采集插件名称")),
                ("collector_scenario_id", models.CharField(max_length=64, verbose_name="采集场景ID")),
                ("description", models.CharField(max_length=64, verbose_name="插件描述")),
                ("category_id", models.CharField(max_length=64, verbose_name="数据分类")),
                ("data_encoding", models.CharField(default=None, max_length=30, null=True, verbose_name="日志字符集")),
                ("is_display_collector", models.BooleanField(default=False, verbose_name="采集项是否对用户可见")),
                ("is_allow_alone_data_id", models.BooleanField(default=True, verbose_name="是否允许使用独立DATAID")),
                ("bk_data_id", models.IntegerField(null=True, verbose_name="DATAID")),
                ("data_link_id", models.IntegerField(null=True, verbose_name="数据链路ID")),
                ("processing_id", models.CharField(blank=True, max_length=255, null=True, verbose_name="计算平台清洗id")),
                ("is_allow_alone_etl_config", models.BooleanField(default=True, verbose_name="是否允许独立配置清洗规则")),
                (
                    "etl_processor",
                    models.CharField(
                        choices=[("transfer", "Transfer"), ("bkbase", "数据平台")],
                        default="transfer",
                        max_length=32,
                        verbose_name="数据处理器",
                    ),
                ),
                (
                    "etl_config",
                    models.CharField(
                        choices=[
                            ("bk_log_text", "直接入库"),
                            ("bk_log_json", "Json"),
                            ("bk_log_delimiter", "分隔符"),
                            ("bk_log_regexp", "正则"),
                            ("custom", "自定义"),
                        ],
                        default=None,
                        max_length=32,
                        null=True,
                        verbose_name="清洗配置",
                    ),
                ),
                ("etl_params", models.JSONField(null=True, verbose_name="清洗参数")),
                ("fields", models.JSONField(null=True, verbose_name="清洗字段")),
                ("params", models.JSONField(default=dict, null=True, verbose_name="采集插件参数")),
                ("table_id", models.CharField(max_length=255, null=True, verbose_name="结果表ID")),
                ("bkbase_table_id", models.CharField(max_length=255, null=True, verbose_name="BKBASE结果表ID")),
                ("is_allow_alone_storage", models.BooleanField(default=True, verbose_name="是否允许独立存储")),
                ("storage_cluster_id", models.IntegerField(null=True, verbose_name="存储集群ID")),
                ("retention", models.IntegerField(null=True, verbose_name="数据有效时间")),
                ("allocation_min_days", models.IntegerField(null=True, verbose_name="冷热数据生效时间")),
                ("storage_replies", models.IntegerField(null=True, verbose_name="副本数量")),
                (
                    "storage_shards_nums",
                    models.IntegerField(blank=True, default=None, null=True, verbose_name="ES分片数量"),
                ),
                (
                    "storage_shards_size",
                    models.IntegerField(blank=True, default=None, null=True, verbose_name="单shards分片大小"),
                ),
            ],
            options={
                "verbose_name": "用户采集插件",
                "verbose_name_plural": "用户采集插件",
                "ordering": ("-updated_at",),
                "unique_together": {("collector_plugin_name", "bk_biz_id"), ("collector_plugin_name_en", "bk_biz_id")},
            },
        ),
    ]