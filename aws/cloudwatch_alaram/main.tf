

resource "aws_sns_topic" "cloudwatch_logs_alarm_sns" {
  name = var.sns_topic_name
}


# metric creation for the cloudwatch logs
resource "aws_cloudwatch_log_metric_filter" "metric_filter" {
  name           = var.log_metric_filter_name
  log_group_name = var.log_group_name
  pattern        = var.pattern
  metric_transformation {
    name      = var.metric_name
    namespace = var.metric_namespace
    value     = "1"
  }
}

# cloudwatch alarm for the metric
resource "aws_cloudwatch_metric_alarm" "cloudwatch_logs_alarm" {
 
  alarm_name         = var.metric_alarm_name
  alarm_description  = var.metric_alarm_description
  alarm_actions       = [aws_sns_topic.cloudwatch_logs_alarm_sns.arn]
  treat_missing_data = "missing"

  metric_name         = lookup(aws_cloudwatch_log_metric_filter.metric_filter.metric_transformation[0], "name")
  threshold           = "10"
  statistic           = "Sum"
  comparison_operator = "GreaterThanThreshold"
  datapoints_to_alarm = "1"
  evaluation_periods  = "1"
  period              = "300"
  namespace           = lookup(aws_cloudwatch_log_metric_filter.metric_filter.metric_transformation[0], "namespace")

  tags = var.tags
}